import pymysql

def connect():
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 database='mydb',
                                 user='root',
                                 password='beefymoo',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection