import psycopg2

def create_table():

    conn = psycopg2.connect(dbname = 'studentdb',user='postgres',password='abc@123',host='localhost', port="5432")

    cur = conn.cursor()

    cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")

    print("Studet Database created...")
    conn.commit()
    conn.close()

def inster_data():
    # Code to accept data from user
    name = input("Enter the name.. ")
    address = input("Enter the Address.. ")
    age =  int(input("Enter your age.... "))
    number = input("Enter your phone number... ")
    conn = psycopg2.connect(dbname = 'studentdb',user='postgres',password='abc@123',host='localhost', port="5432")

    cur = conn.cursor()

    cur.execute("insert into students (name, address, age, number) values (%s, %s, %s, %s);",(name,address,age,number))

    print("Data added in students table ....")
    conn.commit()
    conn.close()

inster_data()

 