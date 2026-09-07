'''
name = "codegnan"
batch = 23
email_id = "saketh@codegnan.com"
print(email_id[7:15])


email_ids = ['saketh@codegnan.com','layatri@gmail.com','sindhusha@gmail.com','laya@gmail.com']
#print(len(email_ids))
print(email_ids[1])
print(email_ids[-2])

#Store 3 more mail_ids into above at a time
email_ids = ['saketh@codegnan.com','layatri@gmail.com','sindhusha@gmail.com']
email_ids.extend(['laya@gmail.com'])
print(email_ids)


#Access each mail id one by one --> loops
email_ids = ['saketh@codegnan.com','layatri@gmail.com','sindhusha@gmail.com','laya@gmail.com']
for mail in email_ids:
    #print(mail)
    print(f"Mail_id of a person is {mail}")

#Store the email_ids with relevant user names
email_ids = ['saketh@codegnan.com','layatri@gmail.com','sindhusha@gmail.com','laya@gmail.com']
users = {}
users = dict.fromkeys(email_ids)
print(users)
users['layatri@gmail.com'] = 2345
print(users)

#All python built-in datatypes are built-in functions
#(int,float,str,list,tuple,set,dict,bool)
'''

email_ids = ['saketh@codegnan.com','layatri@gmail.com','sindhusha@gmail.com','laya@gmail.com']
users = {}
print(users)
for i in range(len(email_ids)):
    #print(i,email_ids[i])
    users[i+1] = email_ids[i]
print(users)

#enumerate --> It provides by default a counter object (you can store in desired collection)
data = dict(enumerate(email_ids,1))
print(data)
