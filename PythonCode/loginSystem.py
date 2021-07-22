import pyinputplus, sqlite3

# CONNECT TO A DATABASE
sqlconnection = sqlite3.connect('login.db')

# CREATE A TABLE FOR THE FIRST TIME
table = ''' CREATE TABLE LoginSystem (
    id          INTEGER      PRIMARY KEY 
    AUTOINCREMENT NOT NULL,
    fullname VARCHAR (30),
    username    VARCHAR (20),
    email       VARCHAR (25) UNIQUE,
    password    VARCHAR (20),
    phone       INTEGER (20) UNIQUE,
    country     VARCHAR (20),
    gender      CHAR (1) )'''

cursor = sqlconnection.cursor()
# uncomment this to execute and create table for the first time
# sqlconnection.execute(table)
# print('Created table successfully')
sqlconnection.commit()

print('Welcome to pluto. Your all in One fantasies.')
print("Please login or sign up to begin ")
print()

prompt = pyinputplus.inputChoice(['Login', 'Sign up'], prompt="Enter 'Login' to login (for existing users) or 'Sign up' to create a new account if you're a new user: ").lower()
if prompt == 'sign up':
    name = input("Enter your full name: \n")
    username = input("Enter your username: \n")
    email = pyinputplus.inputEmail("Enter your email: \n")
    password = input("Enter password: ")
    phone = pyinputplus.inputNum("Enter your phone: \n")
    country = input("Enter you country: \n")
    gender = pyinputplus.inputChoice(['M', 'F'], "Enter gender 'M' for male and 'F' for female: \n")
    dataTuple = (name, username, email, password, phone, country, gender)
    query = "insert into LoginSystem (fullname, username, email, password, phone, country, gender) values(?,?,?,?,?,?,?) "
    cursor.execute(query, (dataTuple))
    sqlconnection.commit()
    print("Signed up successfully")

elif prompt == 'login':
    email = pyinputplus.inputEmail("Enter your email: \n")
    password = input("Enter your password: \n")
    dataTuple = (email)
    data = [(email, password)]
    query = "select email, password from LoginSystem where email = ?"
    cursor.execute(query, (dataTuple,))
    q = cursor.fetchall()
    Noaccount = []
    if q == Noaccount:
        print("No account is associated with the user provided")
        exit()
    if data == q:
        print('Login successful')
    else:
        print('invalid login credentials')