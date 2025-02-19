import pymysql
def connect_db():
     try:
       connection = pymysql.Connect(host='localhost',
       port = 3306 , user = 'root', password = 'root123',
       database = 'sona_db',charset = 'utf8')
       print('DB connected')
       return connection
     except:
       print('connection failed')
def disconnected_db(connection):
     try:
       connection.close()
       print('Db dis-connected')
     except:
       print('error in disconnecting DB')
connection = connect_db()
if connection:
    disconnected_db(connection)
