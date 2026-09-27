'''
List Comprehension --> Tuples

Generators,Exception Handling along with File handling

b = [i for i in range(1,10) if i>4]
print(b)
print(type(b))

#In python there is no Tuple Comprehension --> Generators
b = (i for i in range(1,10) if i>4)
print(b)
print(type(b))


#Generators --> Generators are also Special Functions in python which produces values one by one,which makes program memory efficient

def details():
    """Simple Function"""
    return f'Codegnan is in Vizag'
    return "Layatri is in Codegnan"
print(details())
#In the above case if we pass multiple return statements it doesn't return the results,whereas  a single return statement can pass multiple value

def details():
    """return with multiple values"""
    return 'Codegnan is in Vizag','Saketh is in Codegnan'
print(details())


def subjects():
    """Student subject details"""
    yield "Python"
    yield "MYSQL"
    yield "Aptitude"
    yield "Frontend"
#print(subjects()) #This becomes a generator object
subject = subjects()
print(subjects())
print(type(subject))
#As above function becomes a generator to access values from the function .we use next() keyword, or we prefer loop, or we can also use * to unpack values
#print(next(subject))
#print(next(subject))
#print(next(subject))
#print(next(subject))
#print(next(subject)) #raises StopIteration as all values are accessed 
for i in subject:
    print(i)
    #print(next(i)) #its not possible as already we have used for loop

#Once we use next() function loop usage is not needed
print(*subject) #it unpacks the values and return all at a time (side by side)

#Now no Tuple Comprehension --> Generator to access values
b = (i for i in range(1,10) if i>4)
#print(*b)
for i in b:
    print(f'Value is {i}')
#either we prefer *usage or loop usage
    
a,b = 3,5
a,*b,c = 3,'codegnan','python','vizag',25
print(a)
print(c)
print(b)

#Exception Handling --> Exception handling is the process of making the program or script to function (normally), it will avoid the program to crash
#we use keywords --> try,except,finally

try:
    #program to execute/conditions..it will also raise errors
except:
    #it will handle the error
finally:
    #irrespective of try,except it executes

#Base Exception handling
try:
    a,b = map(int,input("Enter the values : ").split(','))
    c = a//b
    print(c)
except Exception as e:
    print(e) #it returns the error message
#in above case we didn't specifically tell the error name

#syntax errors and logical errors --> user
#Runtime Error --> Machine (Exception handling)
#Multiple Exceptions
try:
    a,b = map(int,input("Enter the values : ").split(','))
    c = a//b
    print(c)
except ZeroDivisionError:
    print("Make sure the denominater value is only +ve/-ve not zero")
except ValueError:
    print("Invalid value type.Only enter integers")
except NameError:
    print("Sariga Chuskoo")

#For a part.usecase think of all possible error types
try:
    a = [34,5,2,4]
    print(a[3])
    a.append('codegnan')
    print(a)
except IndexError:
    print("Check the elements count properly")
except AttributeError:
    print("Do check the method names properly")
finally:
    print("Its done")
#Multiple Exceptions at a time

try:
    a = [34,5,2,4]
    print(a[3])
    a.append('codegnan')
    print(a)
except (IndexError,AttributeError,NameError)as e:
    print(e)
finally:
    print("Prepare well1")
'''
#file handling --> 'r' -->read() ,'w' ->write (),'a','r++'
#with keyword usage
#r+ --> read() and write()
with open ('sep26.txt','r+') as f:
    #print(f) #it returns a wrapper object
    #print(f.read()) #we can read the content
    #f.write("\n Prepare well,don't stress, dont panic, stay calm..All the best")
    f.write("Look at this")
    print(f.read())
























    
    

















