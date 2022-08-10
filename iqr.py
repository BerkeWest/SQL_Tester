import pandas as pd
def IQR_filter(df):
    xl=["Prices","Amounts","Leftover"]
    for j in range(0,3):
        q1=df[xl[j]].quantile(0.25)
        q3=df[xl[j]].quantile(0.75)
        IQR=q3-q1

        lowrange = q1 - (1.5*IQR)
        highrange = q3 + (1.5*IQR)
        df1 = df[xl[j]]
    
        df1.iloc[df1>highrange] = highrange
        df1.iloc[df1<lowrange] = lowrange
