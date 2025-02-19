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
def create_db():
   connection = connect_db()
   query='create database IF NOT EXISTS sona_db;'
   cursor = connection.cursor()
   cursor.execute(query)
   cursor.close()
   disconnect_db(connection)


def insert_row():
    connection = connect_db()    

