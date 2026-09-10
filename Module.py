'''
#Every python file --> Module --> import
import Sep10
print(dir(Sep10)) #dir --> directory will return all available methods,attributes
print(type(Sep10.employees))
print(type(Sep10.details))

Sep10.employees("Layatri",designation = "Trainee",
                location = "Vizag")

#print(Sep10.details.keys())
print(Sep10.details['Organization'])

Sep10.details.update({'batches':['PFS','JFS','DA','AAA','DS'],
                     'employees':240})
print(Sep10.details)

#from keyword

from Sep10 import employees,details

details.update({'batches':['PFS','JFS','DA','AAA','DS'],
                     'employees':240})

print(details)
print(Sep10.__doc__)

'''
#Built-in modules --> math,random,os,time,datetime

#we download modules --> pypi (python package Index)

#Build a QRCode Scanner using Python --> Linkendin URL
#pyqrcode,png
#pip install pyqrcode
#pip install pypng

import pyqrcode
import png
#create a QRCode by giving a link

link = "https://www.linkedin.com/in/layatri-murakada-86403a296/?skipRedirect=true"
qr = pyqrcode.create(link)
#print(qr)
qr.png("myqr.png",scale=10)

#Personal Card --> Name, Mobile number, email_id, github 







































