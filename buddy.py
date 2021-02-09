import psycopg2

def DataBase():
    try:
        mydb = psycopg2.connect(
            host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
        )
        mycursor = mydb.cursor()

        print(mydb.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        mycursor.execute("SELECT version();")
        record = mycursor.fetchone()
        print("You are connected to - ", record, "\n")

        # update_table = '''ALTER TABLE sendmsg ADD status BIGINT;'''
        #
        # mycursor.execute(update_table)
        #
        # mydb.commit()

        # create_table_query = '''CREATE TABLE sendservice
        #           (ID SERIAL PRIMARY KEY,
        #           NAME           VARCHAR(3000)    NOT NULL,
        #           COMP_IND           VARCHAR(3000)    NOT NULL,
        #           EMAIL           VARCHAR(3000)    NOT NULL,
        #           PHONE           VARCHAR(3000)    NOT NULL,
        #           PROJECT           VARCHAR(3000)    NOT NULL,
        #           DESCRIPTION           VARCHAR(5000)    NOT NULL); '''
        #
        # mycursor.execute(create_table_query)

        # create_table_query = '''CREATE TABLE sendmsg
        #           (ID SERIAL PRIMARY KEY,
        #           NAME           VARCHAR(3000)    NOT NULL,
        #           EMAIL           VARCHAR(3000)    NOT NULL,
        #           PHONE           VARCHAR(3000)    NOT NULL,
        #           MESSAGE           VARCHAR(5000)    NOT NULL); '''
        #
        # mycursor.execute(create_table_query)

        # create_table_query = '''CREATE TABLE stats
        #           (ID SERIAL PRIMARY KEY,
        #           VISITORS           BIGINT    NOT NULL); '''
        #
        # mycursor.execute(create_table_query)

        # create_table_query = '''CREATE TABLE unique_visitors
        #           (ID SERIAL PRIMARY KEY,
        #           DATE_VISITORS   DATE,
        #           IP_ADDR    VARCHAR(3000)    NOT NULL); '''
        #
        # mycursor.execute(create_table_query)

        # create_table_query = '''CREATE TABLE subs
        #           (ID SERIAL PRIMARY KEY,
        #           EMAIL           VARCHAR(3000)    NOT NULL); '''
        #
        # mycursor.execute(create_table_query)

        # sql = "INSERT INTO stats(ID, VISITORS) VALUES     (1, 4000);"
        # mycursor.execute(sql)

        # sql = "DELETE FROM subs;"
        # mycursor.execute(sql)

        # sql = "DROP TABLE stats;"
        # mycursor.execute(sql)

        # sql = "UPDATE sendservice SET status = 0 WHERE id = 44"
        # mycursor.execute(sql)
        #
        # mydb.commit()

        # sql = "SELECT * FROM sendservice"
        # mycursor.execute(sql)
        # mobile_records = mycursor.fetchall()
        #
        # print("Print each row and it's columns values")
        # for row in mobile_records:
        #     print("Id = ", row[0], )
        #     print("NAME  = ", row[1], "\n")
        #     print("c/i  = ", row[2], "\n")
        #     print("EMAIL  = ", row[3], "\n")
        #     print("PHONE  = ", row[4], "\n")
        #     print("Project  = ", row[5], "\n")
        #     print("MSG  = ", row[6], "\n")
        #     print("Stat  = ", row[7], "\n")
        #
        # mydb.commit()

        # sql = "SELECT * FROM unique_visitors"
        # mycursor.execute(sql)
        # mobile_records = mycursor.fetchall()
        #
        # print("Print each row and it's columns values")
        # for row in mobile_records:
        #     print("Id = ", row[0])
        #     print("DATE  = ", row[1])
        #     print("IP  = ", row[2])
        #     print()

        # sql = "UPDATE subs SET status = 0 WHERE id = 12"
        # mycursor.execute(sql)
        #
        # mydb.commit()

        # sql = "SELECT * FROM subs"
        # mycursor.execute(sql)
        # mobile_records = mycursor.fetchall()
        #
        # print("Print each row and it's columns values")
        # for row in mobile_records:
        #     print("Id = ", row[0])
        #     print("DATE  = ", row[1])
        #     print("STAT = ", row[2])

        # sql = "UPDATE sendmsg SET status = 1"
        # mycursor.execute(sql)
        #
        # mydb.commit()

        sql = "SELECT * FROM sendmsg"
        mycursor.execute(sql)
        mobile_records = mycursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("Id = ", row[0])
            print("Name  = ", row[1])
            print("Email  = ", row[2])
            print("Phone  = ", row[3])
            print("Msg  = ", row[4])
            print("Stat  = ", row[5])

        mydb.commit()



    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (mydb):
            mycursor.close()
            mydb.close()
            print("PostgreSQL connection is closed")
DataBase()
