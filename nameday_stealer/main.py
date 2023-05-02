import time
import json
import datetime
import requests
import pandas as pd
import pyodbc

c = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server}; Server=GEPHAZ;  Database=MagazineSub;  UID=pythonacc; PWD=asd1234", autocommit=True)


sql_query3 = pd.read_sql("Select FirstName from DictFirstName;", c)
df_firstname = pd.DataFrame(sql_query3, columns=['FirstName'])
df = pd.DataFrame(columns=["ID", "Name", "Day"])
counter = 0


for name in df_firstname['FirstName']:
    file = requests.get(f'https://api.nevnapok.eu/nev/{name}')
    time.sleep(5)
    next_name = file.json()
    if next_name:
        print(name)
        for k in next_name[name]:
            counter += 1
            df.loc[len(df.index)] = [counter, name, k]
    else:
        with open("rossz.txt", "a") as file_object:
            file_object.write(f'{name}, \n')

df.to_json('nevnapok.json', orient= 'table', index=False)

