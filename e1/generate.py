import pandas as pd
from faker import Faker
from faker.providers.person import Provider
import datetime
from datetime import datetime as dt
import random
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


fake = Faker(["hu_HU", "en_GB", "fr_FR"])
person = Provider

today = dt.now()
rng = np.random.default_rng()
no_of_rows = 10
db_name = 'ei'
server_name= 'GEPHAZ\GEPHAZ'

reci_struct = {'reci_id': [],
          'reci_name': [],
          'email_add': []}
reci_df = pd.DataFrame(reci_struct)

rep_struct = {'rep_id': [],
          'rep_name': [],
          'rep_des': []}
rep_df = pd.DataFrame(rep_struct)

rep_proc_struct = {'proc_id': [],
          'rep_id': [],
          'rep_code': [],
          'proc_des': [],
          'email_id': []}
rep_proc_df = pd.DataFrame(rep_proc_struct)

email_struct = {'email_id': [],
          'sub': [],
          'crt_date': []}
email_df = pd.DataFrame(email_struct)

email_reci_struct = {'reci_id': [],
          'email_id': [],
          'crt_by': [],
          'crt_date': [],
          'lastnm': [],
          'lastdm': []}
email_reci_df = pd.DataFrame(email_reci_struct)


def gen_tables(nor):
    for i in range(nor):
        reci_df.loc[len(reci_df.index)] = [20000 + i, fake.name(), fake.email()]
        rep_df.loc[len(rep_df.index)] = [30000 + i, f'{fake.day_of_week()} Report', f'Ez itt a(z){i + 1}számú riport']
        rep_proc_df.loc[len(rep_df.index)] = [600 + i, 30000 + i,
                        f'{fake.bothify(text="RiportCode-666###??-#?##??",letters="AVGHJTREWOPMQ")}-{30+i}',
                                              f'Report{fake.first_name()} Részére', 300 + i]
        email_df.loc[len(reci_df.index)] = [300 + i, fake.sentence(),
                                            today - datetime.timedelta(days=random.randint(90, 200))]
        email_reci_df.loc[len(reci_df.index)] = [20000 + i, 300 + i, 1,
                                                 today - datetime.timedelta(weeks=random.randint(90, 200)),
                                                 f'lics-locs{random.randint(20, 70)}',
                                                 today - datetime.timedelta(days=random.randint(1, 14))]

    reci_df.loc[len(reci_df.index)] = [1 + nor, 'teszt elek', 'colgate@megvagy.hu']
    reci_df.loc[len(reci_df.index)] = [1 + nor, 'teszt elek ugyanaz az ID', 'colgate@megvagy.hu']
    reci_df.loc[len(reci_df.index)] = [1 + nor + 1, 'teszt elek növekvő ID', 'colgate@megvagy.hu']
    reci_df.loc[len(reci_df.index)] = [20000 + nor + 333, 'mar hozza adva, email cim becsap', 'signal@megvagy.hu']

    rep_df.loc[len(rep_df.index)] = [30000 + nor, f'Ez kell nekem Report', f'Ez itt a szóban forgó riport']
    rep_proc_df.loc[len(rep_proc_df.index)] = [600 + nor, 30000 + nor,
                            f'{fake.bothify(text="RiportCode-666###??-123456", letters="AVGHJTREWOPMQ")}-{30 + nor}',
                            f'Report{fake.first_name()} Részére', 300 + nor]
    email_df.loc[len(email_df.index)] = [300 + nor, 'ez az a riport', today]

    email_reci_df.loc[len(email_reci_df.index) + 2] = [20000 + nor, 300 + nor, 1, today, 'lics-locs-én', today]
    email_reci_df.loc[len(email_reci_df.index) + 3] = [20000 + nor + 1, 300 + nor, 1, today, 'lics-locs-én', today]
    email_reci_df.loc[len(email_reci_df.index) + 4] = [20000 + nor + 333, 300 + nor, 1, today, 'kakukktojás', today]

    print(email_reci_df)
    print(reci_df)

gen_tables(no_of_rows)

reci_df.to_excel(f'reci_table.xlsx')
rep_df.to_excel(f'rep_table.xlsx')
rep_proc_df.to_excel(f'rep_proc_table.xlsx')
email_df.to_excel(f'email_table.xlsx')
email_reci_df.to_excel(f'email_reci_table.xlsx')


def sql():
    connection_string = f"DRIVER={'ODBC Driver 17 for SQL Server'};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes;"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

    with engine.connect() as con:
        reci_df.to_sql('reci', con, index=False)
        rep_df.to_sql('rep', con, index=False)
        rep_proc_df.to_sql('rep_proc', con, index=False)
        email_df.to_sql('email', con, index=False)
        email_reci_df.to_sql('email_reci', con, index=False)

sql()









