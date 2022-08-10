import pandas as pd
import numpy as np
import warnings
import iqr
import add_dataframe
import sqlite3

warnings.filterwarnings("ignore")
df=pd.read_csv('.\\deneme.txt',sep="|")
iqr.IQR_filter(df)

con = sqlite3.connect('inventorylist.db')
df.to_sql(name="inventory",con=con,if_exists= "replace", index=False)
con.commit()

xlWriter = pd.ExcelWriter("inventorylist.xlsx",engine='xlsxwriter')
workbook  = xlWriter.book

add_dataframe.addframe(df,xlWriter)
workbook.close()
print(df)
