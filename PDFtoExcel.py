import pdfplumber
import pandas as pd

print("请先把PDF文件放入该程序所处文件夹中\n最终输出文件为data.xlsx，存放在该程序所处文件夹中")
path = input("请输入待转换的PDF文件名（记得带上后缀.pdf）：")

with pdfplumber.open(path) as pdf:
    totalPages = len(pdf.pages)
    df = pd.DataFrame()
    for pageNumber in range(totalPages):
        page = pdf.pages[pageNumber]
        table = page.extract_table()
        dfPage = pd.DataFrame(table)
        df = pd.concat([df, dfPage], ignore_index = True)
        #print(dfPage)
    df.to_excel('data.xlsx', index = False)