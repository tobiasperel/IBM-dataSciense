import pandas as pd
xlsx_path = 'canciones.xlsx'
df = pd.read_excel(xlsx_path)
#print(df)
laland = df[['Artist Name(s)','released']]
print(laland)
lala = df['Artist Name(s)'].unique() # lo que es extrearte todos los elementos y te saca los repetidos de la columna  realised
#print(lala)

#df['Duration (ms)']>=123456 # esto devuelve una lista de bool true o false indicando cada elemento
df1 = df[df['Duration (ms)']>=400000] # ahi guardo los que cumplen con la condicion
print(df1)
df1.to_csv('new_songes.xlsx')
