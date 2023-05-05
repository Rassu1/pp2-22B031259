import psycopg2
con = psycopg2.connect(database="firstDB",
                                  user="postgres",
                                  password="2679528",
                                  host="localhost",
                                  port="5432")
current = con.cursor()
current.execute('''CREATE TABLE PhoneBook(name varchar, number varchar);''')
current.close()
con.commit()
con.close()