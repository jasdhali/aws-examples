import pandas as pd
import pymysql

host="very.long.endpoint.definition.amazonaws.com"
port=3306
dbname="your_database_name"
user="your_user_name"
password="your_password"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)