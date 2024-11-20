import psycopg2
import private

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = private.password
DATABASE = 'Public'
PORT = 5433

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE, port=PORT)

cursor = connection.cursor()
#
query = "DROP TABLE IF EXISTS random_countries"
#
cursor.execute(query)
#
create_table_q = f'''CREATE TABLE random_countries(
                  id SERIAL PRIMARY KEY,
                  name VARCHAR(25) NOT NULL,
                  capital VARCHAR(25) NOT NULL,
                  flag_code VARCHAR(25),
                  population INTEGER NOT NULL
                  )'''
cursor.execute(create_table_q)
connection.commit()
# results = cursor.fetchall()
#
connection.close()

# for item in results:
#     print(item)
