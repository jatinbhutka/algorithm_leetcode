import pandas as pd
import sqlalchemy as sc



engine = sc.create_engine('postgresql://postgres:98!965@@39J@PANk@localhost:5432/I590 SQL NoSQL' )



"""
engine connection_path: 'postgresql://username:password@localhost:5432/Database_name'

Following SQL Query is use to get username in postgres query tool:
    SELECT usename
    FROM pg_user;a

    https://www.techonthenet.com/postgresql/questions/find_users.phpa

    pg_user in postgresql contains the information about the users
"""


#Read entire table in a dataframe using read_sql_table
print("Read Student Table:")
df = pd.read_sql_table('student',engine)
"""
    pd.read_sql_table ('table_name', engin_connection)
"""

print(df, "\n\n")


print("Read book table")
#Read entire table in a dataframe using read_sql_table
df = pd.read_sql_table('book',engine)
"""
    pd.read_sql_table ('table_name', engin_connection)
"""
print(df, "\n\n")


print("Read perticular columns in book table")
#Read only selected columns:
df_by_col = pd.read_sql_table("book", engine,  columns = ['title'])
print(df_by_col, "\n\n")


print("Execute query and get result")
#Join two tables and read them in a dataframe using read_sql_query
df_join_table = pd.read_sql_query("SELECT * FROM student, book", engine)
print(df_join_table, "\n\n")



# Write complex query:
print("Student and book info they bought")
query = ''' SELECT s.sid, s.sname, b.bookno, b.title
        FROM student s inner join buys bs on s.sid = bs.sid 
        inner join book b on b.bookno =  bs.bookno
    '''
df = pd.read_sql_query(query,engine)
print(df,"\n\n\n")


print("Data to be inserted:")
data_to_insert = {"sid": [12341, 19876],
      "sname": ["Test11", "Test21"]}
df = pd.DataFrame(data_to_insert)
print(df)
print("\n\n\n")

df.to_sql(name="student",  con= engine, if_exists = 'append', index = False)


print("Read Student Tabl after inserting records:")
df = pd.read_sql_table('student',engine)
print(df,"\n\n\n\n")




import psycopg2

def deleteData(mobileId):
    try:
       connection = psycopg2.connect(user="postgres",
                                      password="98!965@@39J@PANk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="I590 SQL NoSQL")
       cursor = connection.cursor()
       sql_delete_query = "Delete from student where sid = %s"
       cursor.execute(sql_delete_query, (mobileId, ))
       connection.commit()
       count = cursor.rowcount
       print(count, "Record deleted successfully ", "\n\n\n")
    
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

deleteData(12341)
deleteData(19876)

print("Read Student Tabl after inserting records:")
df = pd.read_sql_table('student',engine)
print(df,"\n\n\n\n")

