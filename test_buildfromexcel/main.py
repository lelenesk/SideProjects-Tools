from sqlalchemy import create_engine, text, exc
from sqlalchemy.orm import Session
from sqlalchemy.engine import URL
from sqlalchemy import Table, MetaData, Column, Integer
import pyodbc
import pandas as pd
import random

def db_handler(db_list):
    db_counter = 0

    for db in db_list:
        if db.startswith(f"dummy_database"):
            db_counter += 1
            print(db_counter)
        else:
            pass

    if db_counter == 0:
        cursor.execute(
            f'''
            CREATE database dummy_database_{db_counter + 1}
             '''
        )
        con.commit()

    elif db_counter > 0:
        cursor.execute(
            f'''
            CREATE database dummy_database_{db_counter +1}
             '''
        )
        con.commit()
    else:
        pass


chk = True
szinhaz_nevek = []
szinhaz_cimek = []
szerzok = []
eloadasok = []
mufajok_raw = []
mufajok = []
szamsor = []


def table_maker():

    def dummy_generator(needed_list):
        if "színház" in needed_list:
            file1 = open("dummydata/szinhazlista.txt", "r", encoding="utf-8")
            szinhaz_list = file1.readlines()
            for i in range(4):
                for szinhaz in szinhaz_list:
                    try:
                        splitted_row = szinhaz.split(',')
                        szinhaz_nevek.append(splitted_row[0])
                        szinhaz_cimek.append(str(splitted_row[1]).replace("\n", ""))
                    except:
                        szinhaz_nevek.append(szinhaz)
                        szinhaz_cimek.append("Képzeletbeli város")

        if "szerző" in needed_list or "előadás" in needed_list or "műfaj" in needed_list:
            file2 = open("dummydata/mufajlista.txt", "r", encoding="utf-8")
            mufaj_list = file2.readlines()
            for i in range(20):
                for mufaj in mufaj_list:
                    mufajok_raw.append(mufaj.replace("\n", ""))

            author_df = pd.read_excel("dummydata/szerzolista.xlsx")
            for row in author_df['author']:
                szerzok.append(row)
            for row in author_df['title']:
                eloadasok.append(row)
                mufajok.append(random.choice(mufajok_raw))

        if "randomszám" in needed_list:
            for i in range(1000):
                szamsor.append(i + 3500)

    def checkList(lst):
        global chk
        ele = lst[0]
        for item in lst:
            if ele != item:
                chk = False
                break

    sheets = pd.ExcelFile("table_config.xlsx").sheet_names

    for table_name in sheets:
        table= pd.read_excel("table_config.xlsx", sheet_name=table_name)

        column_names = []
        type = []
        other1 = []
        other2 = []
        other3 = []
        other4 = []
        dummy_type = []
        number = []

        cursor.execute(f'''CREATE TABLE {table_name}(t INT);''')

        for value in table['column_name']:
            column_names.append(value)
        for value in table['type']:
            type.append(value)
        for value in table['other1']:
            if value == "":
                pass
            else:
                other1.append(value)
        for value in table['other2']:
            if value == "":
                pass
            else:
                other2.append(value)
        for value in table['other3']:
            if value == "":
                other3.append("")
            else:
                other3.append(value)
        for value in table['other4']:
            if value == "":
                pass
            else:
                other4.append(value)
        for value in table['dummy_type']:
            dummy_type.append(value)
        for value in table['number']:
            number.append(value)

        for i in range(len(column_names)):
            cursor.execute(
                f'''ALTER TABLE {table_name} ADD {column_names[i]} {type[i]};''')
        cursor.execute(f'''ALTER TABLE {table_name} DROP COLUMN t;''')


        """
        {other1}
        {other2}
        {other3}
        {other4}
        """

# magic
        dummy_generator(dummy_type)

        checkList(number)
        global chk
        if chk:
            column_names_list = ""
            random_list = random.sample(range(1, 440), number[0])
            for v in column_names:
                column_names_list += str(v) + ", "
            values_list = ""
            for x in range(number[0]):
                for position_value in dummy_type:
                    if "színház" == position_value:
                        values_list += "'" + str(szinhaz_nevek[int(random_list[x])]).replace("'", "''") + "'" + ", "
                    if "műfaj" == position_value:
                        values_list += "'" + str(mufajok_raw[int(random_list[x])]).replace("'", "''") + "'" + ", "
                    if "előadás" == position_value:
                        values_list += "'" + str(eloadasok[int(random_list[x])]).replace("'", "''") + "'" + ", "
                    if "szerző" == position_value:
                        values_list += "'" + str(szerzok[int(random_list[x])]).replace("'", "''") + "'" + ", "
                    if "randomszám" == position_value:
                        values_list += "'" + str(szamsor[int(random_list[x])]).replace("'", "''") + "'" + ", "
                    if "valami" == position_value:
                        values_list += "'" + str(mufajok_raw[int(random_list[x])]).replace("'", "''") + "'" + ", "
                sql_query = f"""INSERT INTO {table_name} ({column_names_list[:-2]}) VALUES ({values_list[:-2]});"""
                values_list = ""
                print(sql_query)
                cursor.execute(sql_query)
        else:
            index = 0
            for i in range(len(dummy_type)):
                print(column_names[i])
                if dummy_type[i] == "színház":
                    random_list = random.sample(range(1, 440), number[index])
                    for x in range(number[i]):
                        cursor.execute(
                            f"""INSERT INTO {table_name} ({column_names[i]}) VALUES ({szinhaz_nevek[int(random_list[x])]});""")
                elif dummy_type[i] == "műfaj":
                    random_list = random.sample(range(1, 440), number[index])
                    for x in range(number[i]):
                        cursor.execute(
                            f"""INSERT INTO {table_name} ({column_names[i]}) VALUES ({mufajok_raw[int(random_list[x])]});""")
                elif dummy_type[i] == "előadás":
                    random_list = random.sample(range(1, 440), number[index])
                    for x in range(number[i]):
                        cursor.execute(
                            f"""INSERT INTO {table_name} ({column_names[i]}) VALUES ({eloadasok[int(random_list[x])]});""")
                elif dummy_type[i] == "szerző":
                    random_list = random.sample(range(1, 440), number[index])
                    for x in range(number[i]):
                        cursor.execute(
                            f"""INSERT INTO {table_name} ({column_names[i]}) VALUES ({szerzok[int(random_list[x])]});""")
                elif dummy_type[i] == "randomszám":
                    random_list = random.sample(range(1, 440), number[index])
                    for x in range(number[i]):
                       cursor.execute(
                        f"""INSERT INTO {table_name} ({column_names[i]}) VALUES ({szamsor[int(random_list[x])]});""")
                index += 1

if __name__ == '__main__':

    con_str2 = ("Driver={ODBC Driver 17 for SQL Server};"
                "Server=GEPHAZ;"
                "Database=startbase;"
                "Trusted_Connection=yes;")
    con2 = pyodbc.connect(con_str2, autocommit=True)
    cursor2 = con2.cursor()


    db_result = pd.read_sql("SELECT name FROM sys.databases;", con2)
    db_names = []
    for i in db_result['name']:
        db_names.append(i)

    con_database = ""
    con_database_list = []
    for db in db_names:
        if db.startswith(f"dummy_database"):
            con_database_list.append(db)
        else:
            con_database_list.append("dummy_database_1")
        con_database = con_database_list[- 1]
    cursor2.execute(
        f'''
                CREATE database {con_database}
             '''
    )
    con2.commit()
    cursor2.close()
    con2.close()

    con_str = (f"Driver={'ODBC Driver 17 for SQL Server'};"
               "Server=GEPHAZ;"
               f"Database={con_database};"
               "Trusted_Connection=yes;")

    con = pyodbc.connect(con_str, autocommit=True)
    cursor = con.cursor()

    #db_handler(db_names)
    table_maker()












