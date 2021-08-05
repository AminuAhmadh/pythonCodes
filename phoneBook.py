# A PhoneBook program that save and delete a phone book using the commandLine
# usage:
# .py save firstName secondName phone email
# .py delete full name
# By Aminu Ahmadh GITHUB @AminuAhmadh
# this program saves the data to a database


import sqlite3, sys
import pandas as pd


# connect to a database
SQLconnection = sqlite3.connect('phoneBook.db')
cursor = SQLconnection.cursor()
print('Connected to database successfully')
print()
# table = 'CREATE TABLE PHONEBOOK (ID INTEGER PRIMARY KEY, FULLNAME TEXT NOT NULL, PHONE INTEGER NOT NULL, EMAIL TEXT NOT NULL UNIQUE, DATE DATETIME);'
# cursor.execute(table)
# SQLconnection.commit()
# print('table created successfull')
if len(sys.argv) == 6  and sys.argv[1] == 'save':

    print('Saving contact...')

    name = sys.argv[2].lower() + ' ' + sys.argv[3].lower() 
    phone = sys.argv[4]
    email = sys.argv[5]

    dataTuple = (name, phone, email)
    cursor.execute('insert into PHONEBOOK (FULLNAME, PHONE, EMAIL) values(?, ?, ?)', dataTuple)
    SQLconnection.commit()
    print('Contact saved successfully')
    print('Inserted the data into the PHONEBOOK table in the phoneBook database')
    cursor.close()

elif len(sys.argv) == 5 and sys.argv[1] == 'save':
    name = sys.argv[2].lower() + ' ' + sys.argv[3].lower() 
    phone = sys.argv[4]
    dataTuple = (name, phone)
    query = ''' insert into PHONEBOOK (FULLNAME, PHONE) Values (?,?) '''
    cursor.execute(query, dataTuple)
    SQLconnection.commit()
    print('Contact saved successfully')
    print('Inserted the data into the PHONEBOOK table in the phoneBook database')
    cursor.close()


elif len(sys.argv) == 4 and sys.argv[1] == 'delete':
    name = sys.argv[2].lower() + ' ' + sys.argv[3].lower()
    print('selected the contact to delete...')
    dataTuple = (name)
    query = 'delete from PHONEBOOK where FULLNAME = ?'
    cursor.execute(query, (dataTuple,))
    SQLconnection.commit()
    print('Done. Deleted', name)
    cursor.close()

elif len(sys.argv) == 2 and sys.argv[1].lower() == 'show':
    # get the data
    all_data = 'select * from phonebook'
    ID = []
    fullName = []
    phone = []
    email = []
    rows = cursor.execute(all_data).fetchall()
    for row in rows:
        ID.append(row[0])
        fullName.append(row[1])
        phone.append(row[2])
        email.append(row[3])
    df = pd.DataFrame({'ID': ID, 
                        'FULL NAME': fullName,
                        'PHONE': phone,
                        'EMAIL': email
    })
    print(df)