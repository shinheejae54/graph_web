import os
from flask import Flask 
import pymysql

conn = pymysql.connect(host='localhost', db='food_data',user='root', password='selfishsql54' , charset='utf8')
#mysql를 연결했음 

cur = conn.cursor()

cur.execute("""select column_name
from INFORMATION_SCHEMA.columns
where TABLE_SCHEMA= 'food_data'
and TABLE_NAME='newtable';""")
value = cur.fetchall()
value = list(value[:19])
year = []
for i in value:
  i = list(i)[0]
  year.append(i)
#list로 가져오고 필요없는 데이터는 누락 시켰음
#year = 연도에 대한 데이터  

cur.execute("""select *
from food_data.newtable n 
;""")
name = cur.fetchall()
name = list(name)
#name = 외식업 종류  





cur.execute("""select *
from food_data.food_columns fc
where `local` ='특성별(1)';""")
columns = cur.fetchall()
columns = list(columns[0][2:])
#colums = 외식업 종류

cur.execute("""select *
from food_data.food_columns fc
where `local` ='전체';""")
food_value = cur.fetchall()
food_value = list(food_value[0][2:])
#food_value = 외식업 종류에 대한 값



