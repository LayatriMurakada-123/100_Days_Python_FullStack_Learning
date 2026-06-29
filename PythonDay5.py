'''
     DICTIONARY
     ----------

     
Dictionary: It is a key:value pair and separated by : ,
keys are unique ie no duplicates and values can be duplicated.
--> represented by using {} and dict is ordered
--> dict is mutable because we can update key values
methods:
keys()--> used to get all keys from the dict
syntax: var_name.keys()
values()--> used to get all the values from the dict
syntax: var_name.values()
items()---> we'll get both keys and values
clear()--> used to remove all the key:val from dict--> result is empty dict
get()--> returns specific key value and if key isnot present in dict it will returns None.
pop()-->removes a spe ific key

ICIC_details_ = {"name": "Deepika",
                 "mobile":1234567890,
                 "Adhar":"123456787654",
                 "AC num": 987652,
                 "ATM PIN":"7789",
                 "age": 22,
                 "Gender":"F"}
print(ICIC_details_)
print(type(ICIC_details_))
# dict methods
print(ICIC_details_.keys())
print(ICIC_details_.get("AC num"))
print(ICIC_details_.values())
print(ICIC_details_.items())
print(ICIC_details_ ["name"])# accessing values with keys
ICIC_details_.pop("age")
print(ICIC_details_)

#clearing a dict using clear() method
details_={
    "name":"Sumanth",
    "Age":25,
    "Gender": "M"}
print(details_)
#updating a dict
details_.update({"Name":"Rishikesh"})
details_.update({"Age":27})
details_.update({"mob":9347808977})
print(details_)
details_.clear()
print(details_)
'''


'''
    SETS
    ----
    
Set: set is a collection of unordered elements that are separated by ,
-->set is mutable
-->can remove duplicate value by itself
-->represented by {}
methods in set:
1. union()--> symbol- | --> used to combine the elements
2.intersection--> & --> gives common element from the both sets
3. symmetric_difference()--> removes common elements from the sets and return the combined set--> ^

4. add() --> used to add new element into set at the last position
5.update()-->adds multiple elements from a list,tuple or another set.
6. remove()--> to delete the element from the set based on element ie removes a specific element
if no element found then raises a key error
7. pop()--> removes last element from the set or an arbitary element
8.discard()-->removes an element if present but doesnt  raise an error if the element is absent
9.clear()-->revomes all elements and output is set()'''
sample_={1,2,3,4,5,6}
print(sample_)
print(type(sample_))
#set operations
sample_2={3,4,5,6,7,8,9}
print(sample_ | sample_2)
print(sample_.union(sample_2))
print(sample_2.union(sample_))
print(sample_.intersection(sample_2))
print(sample_2.intersection(sample_))
print(sample_ ^ sample_2)
print(sample_ - sample_2) #difference A-B
print(sample_2 - sample_) #B-A
print(sample_.symmetric_difference(sample_2))

go={1,2,3,4,4,4,5,2,1,2,3,3}
print(go) #prints unique values only no duplicates
colors_={"red","green","pink","black"}
print(colors_) #unordered ie output order may differ each time.
#built in functions in sets
so={1,2,5,3,6,4,9,8,7}
print(len(so))
print(max(so))
print(min(so))
print(sum(so))
print(type(so))
print(sorted(so))

fruits={"apples","banana","mango"}
print(fruits)
fruits.add("orange")
print(fruits)
fruits.update(["grapes","kiwi"]) #list
fruits.update({"cherry","watermelon"})#set
print(fruits)
fruits.remove("grapes")
print(fruits)
fruits.discard("orange")
fruits.discard("papaya")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)




