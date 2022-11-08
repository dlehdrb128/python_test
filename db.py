import mariadb
import sys




config = {
    "user":"root",
    "password":"1234",
    "host":"localhost",
    "port":3307,
    "database":"aitrading_db"
}



try:
    db = mariadb.connect(**config)
    print( "마리아DB 연결" )
   
 
    cursor = db.cursor()
    SQL = 'SELECT * FROM companylist where name = %s'
    cursor.execute(SQL,('경방'))
    result = cursor.fetchone()
    print(result)
    # fetchone
    # print(result)

    # for( market ) in cursor:    #해당 컬럼명의 데이터들이 cursor안에 담겨져 나온다.
    #  print( market )


except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)





