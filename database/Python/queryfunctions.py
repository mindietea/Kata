import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
connection = pymysql.connect(host='localhost',
                             user='copperstick6',
                             password=keys.sqlKey(),
                             db= "sys",
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
