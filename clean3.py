import pandas as pd
import numpy as np

missing_val = ["NEW","-","None","Not rated","Opening","opening",np.nan]
df = pd.read_csv("C:/Users/hp1/Documents/regex project/integrated cities/kota1.csv",na_values = missing_val)
df.columns = map(str.lower , df.columns)
df1=df[df['rating'].isnull()]
df.dropna(inplace=True)
df['rating'].astype('float')
df.rename(columns={'cusine_category':'cuisine','cusine type':'cuisine_cat'},inplace= True)
df.replace('CafÃ©','Cafe')
#df=df.drop(df['cuisine_cat']=='none', inplace=True)
unique_cuisines=list(df.cuisine_cat.unique()) 

df2=df[['rating'],['cuisice_cat']]

#for i in unique_cuisines:
#    print (i)
#df2=df.where(df['cuisine_cat']=='Casual Dining')
#df2.dropna(inplace=True)
#df2.to_csv('C:/Users/hp1/Documents/regex project/integrated cities/kota2.csv')
#print(df2['rating'].mean(skipna= True))


#print(df.dtypes)
#print(df['rating'].mean())
#df.to_csv('C:/Users/hp1/Documents/regex project/integrated cities/kota2.csv')





#c=df['cuisine_cat'].value_counts()
#print(c.size)
#print(c[0][1])
#df.info()
#res=df[df['CUSINE TYPE']=='Casual Dining']#'RATING']]
#print(res[0][0])

#print(df['rating'].isnull().sum())

    
#print(df1)



#col1=df["RATING"]


#removing the rows with cuisine as none
#df.drop(df[df["CUSINE TYPE"]=="none"].index, inplace= True)
#print(df.iloc[[25]])

#calculate mean of column

#x=df["RATING"].mean(skipna='True')

#df.loc[:,(df=="NEW") and (df=="-")]=np.nan 

#df.replace('-','NaN')
#
#print(df.iloc[[18][0]])

#df.astype({'RATING':'int64'})


