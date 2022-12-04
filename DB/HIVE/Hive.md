# DB 연결
from impala.dbapi import connect as hive_connect
hiveconn = hive_connect(host='IP',
               port=10000,
               user='n',
               password='n',
               auth_mechanism='PLAIN')
# SQL
sql='''
넣기
'''
#### Read sql from conn_imp
df = pd.read_sql( sql ,hiveconn)
#### Close Connection
hiveconn.close()
