import sqlite3

con = sqlite3.connect("users")

print("Enter user firstname")
fn = input()

print("Enter user lastname")
ln = input()

print("Enter user email")
em = input()

print("Enter user password")
ps = input()

#insert onto stud_info(sroll,sname,scity) values (15,,'ravi','mumbai')
query = "insert into UserLogin(Firstname,Lastname,Email,Password) values ('" + fn + "','" + ln + "','" + em +"','" + ps + "')"

con.execute(query)
con.commit()

con.close()

print("data saved....")