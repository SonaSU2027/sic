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
def create_table():
   connection = connect_db()
   query="create table IF NOT EXISTS peoples(id int primary key, name varchar(32) not null,gender char check(gender in('m','M','f','F')),location varchar(32),dob datetime);"
   cursor = connection.cursor()
   cursor.execute(query)
   cursor.close()
   print('Table creation successfull!!!')
   disconnected_db(connection)
def read_person_details():
   name = input('Enter person name:')
   gender = input('Enter person gender')[0]
   location = input('Enter person location:')
   dob = input('Enter person date of birth(yyyy/mm/dd):')
   return (name,gender,location,dob)

def insert_row(): 
    connection = connect_db()  
    query = 'insert into peoples(name,gender,location,dob) values(%s,%s,%s,%s);'
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()  
    disconnected_db(connection)
insert_row()
