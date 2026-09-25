'''
OOP - Encapsulation, Inheritance, Polymorphism, Abstraction


#Abstraction - It is the process of hiding necessary details and display / access relevant  iinformation only
#Module abc

import abc
#print(dir(abc))  #It  returns available methods, classes.......

from abc import ABC, abstractmethod

#Now we will create some base classes to have abstraction applied for all classes
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass
class Photo(Content):
    """This dervied class will have upload features"""
    def upload(self):
        print("Photo is uploaded successfully")
        print("Photo is compressed and edited as per filters choosen")
        print("Photo is posted")
class Video(Content):
    """This is dervied class will have video upload features"""
    def upload(self):
        print("Encoding the video")
        print("Cmpressed and filters are added")
        print("Edited video is published successfully")
class Reel(Content):
    """This dervied class will have reel uploading features"""
    def upload(self):
        print("Timing and content is choosen")
        print("Reel content is mapped with time and audience")
        print("Reel is edited and uploaded successfully")
    
content_ = [Photo(), Video(), Reel()]
#print(content_)
for content in content_:
    content.upload()



#List Compprohensions - Optimized way of creating and using lists

Syntax - [expression for var in collection / function]




list_ = [1, 2, 3, 4]
for i in range(1, len(list_) +  1):
    l = i ** 2
    list_.append(l)
print(list_)

list_ = [1, 2, 3, 4]
for i in list_:
    l = i ** 2
    list_.append(l)
    print(list_)


#In above it gets into infinite and also limits be exceeded
lst = []
for i in range(10):
    lst.append(i)
    print(lst) #In this case it prints for every iteration
print(lst)



'''
list_ = [i ** 3 for i in range(1, 20)]
print(list_)



#To access desired elements and make change

data = ["meena", "dedeepya", "ankitha", "meghana"]
new_data = []
#Change every name to uppercase
for i in data:
    new_data.append(i.upper())
print(new_data)

#Using List compression
new_data = [i.title() for i in data]
print(new_data)

#To update each value in a list

marks = [14, 15, 12, 13]
d = [i + 30 for i in marks]
print(d)


#Every list comprehension can be converted to loops, but every loop cannot be converted to list comprehension















