import pandas as pd
import pymysql

host="aurora-mysql-cluster.cluster-cuhaoqm7vput.us-east-1.rds.amazonaws.com"
port=3306
dbname="testdatabase"
user="admin"
password="adminadmin"

conn = pymysql.connect(host=host, user=user,port=port,passwd=password, db=dbname)
print( 'database connection created successfully' )
