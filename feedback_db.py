import mysql.connector as myc
mycon = myc.connect(host = "localhost", user = "root", passwd = "Anubhav@2007", database = " feedback_db")
if mycon.is_connected() == False:
    print("Error connecting!!")
else:
    cur = mycon.cursor()
    cur.execute("CREATE TABLE contact (id INTEGER PRIMARY KEY AUTO_INCREMENT,name varchar(50) NOT NULL,email varchar(50) NOT NULL, phone int(10) NOT NULL)");
    name = input("enter name : ")
    email = input("enter email :")
    rating =input("enter rating :")
    comment =input("enter comment :")
    cur.execute('INSERT INTO contact (name, email, rating, comment) VALUES (%s,%s,%s,%s)',(name, email, rating, comment));
    mycon.commit()
mycon.close()

