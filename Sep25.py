#List comprehension with if clause
#Syntax: [expression for var in collection/function if <condition>]
'''
g = [i for i in range(1,21) if i%2==0]
print(g)
h = [i**2 for i in range(1,21) if i%2==0]
print(h)

#write above two cases as functions

class Numbers:
    def even_numbers(self):
        g = [i for i in range(1, 21) if i % 2 == 0]
        print(g)
    def even_squares(self):
        h = [i**2 for i in range(1, 21) if i % 2 == 0]
        print(h)
        
obj = Numbers()
obj.even_numbers()
obj.even_squares()


num = int(input("Enter a number:"))
def fun(num):
    list_ = []
    for i in range(1,num):
        if num>0:
            if i%2==0:
                list_.append(i)
    return list_
print(fun(num))


#Same above case using filter
h = list(filter(lambda i:i%2==0,range(1,21)))
print(h)

names = ['codegnan','python','data','layatri']
k = list(filter(lambda x:len(x)>= 6, names))
print(k)

#in below case length of each object is returned in a new list
h = list(map(lambda x:len(x),names))
print(h)

#group of values --> map
j = list(map(int,input().split(','))) #comma seperated values
print(j)
a,b = map(int,input().split()) #space seperated values
print(f'Value of a is {a}, Value of b is {b}')


#multiple string values
name,place = input().split()
print(f'Name is {name},Place is {place}')


#Group of names
names = list(map(str,input("Enter the names:").split(',')))
print(names)


names = ['codegnan','python','data','layatri','vizag']
new_names = list(map(lambda x:x.upper(),names))
print(new_names)


prices = [2500,3500,5000,7500]
#create filtered prices by applying discount of 10% for each price
discount_price = list(map(lambda x:x-x*0.1,prices))
print(discount_price)


#list Comprehension with if-else usage
#Syntax --> [true_value if condition else false_valu for expression in collection/func]

#filter even odd values in given range
result = ["Even" if i%2==0 else "Odd" for i in range(1,21)]
print(result)
result = [i**2 if i%2==0 else i for i in range(1,21)]
print(result)


#Nested Loops with List  Comprehension
#Syntax --> [expression for item1 in iterable1 for item2 in iterable2]

colors = ['Green','Red','Blue']
sizes = ['S','M','L']
matching = [(i,j)  for i in colors for j in sizes]
print(matching)


marks = [25,25,24,20]
weekly = [35,30,45,48]
final = [mark+wmark for mark in marks for wmark in weekly]
print(final)
final_marks = list(map(lambda mark,wmark:(mark+wmark),marks,weekly))
print(final_marks)
'''

#Nested Comprehension with if-else combination 
#Syntax --> [true_value if <condition> else false_value for item1 in iterable1 for item2 in iterable2]

f = [i+4 if i>=j else i-3 for i in range(1,5) for j in range(1,5)]
print(f)
print(*f) #it unpacks value from above collection
for i in f:
    print(i,end=' ')

#TypeError,ValueError












