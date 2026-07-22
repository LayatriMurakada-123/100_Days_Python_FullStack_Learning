
         -: File Handling :-
            ==== ========

File handling is an object that gives mores options like creting , updating.

There are two ways to open a file...

1. Open():
   ------
syntax:- --> do = open('file name' , 'mode')
------       #statements
             close()
Ex:-
--
do = open('any.txt' , 'r')
print(do.read())
close()


2. with(keyword):
   ---- -------
syntax --> with open('file name' , 'mode') as do:

Ex:-
--
with open('any.txt' , 'r') as do:
    print(do.read())


Modes
-----

1. r-mode --> used to read the file , incase if the file is not present it will raise an error.

2. w-mode --> used to write the text inside the file and it will override the text inside the file , incase if the file is not present it will create a new file with the name given
   eg:-
   --
   with open ('demo.txt' , 'w') as do:
    print(do.write('we are using file handling'))


3. a-mode --> This is used to add the text at last position inside the file
   eg:-
   --
   with open ('demo.txt' , 'a') as do:
       print(do.write(' This is python module'))

4. x-mode --> It is used to create a new flie by adding inside the file , incase if the file is present it will raise an error...
   eg:-
   --
   with open('dot.txt' , 'x') as do:
       print(do.write('we are using file handling'))

   -: Functionalities :-
      ---------------

write()
------
--> This function is used to add the text inside a file or update a file with new text...
eg:-
--
with open('dot.txt' , 'w') as do:
    print(do.write('we are using file handling'))
with open('dot.txt' , 'a') as do:
    print(do.write('we are using file handling'))


read()
-----
--> This is used to read a file and this read() will read file chunk by chunk...
    we can also specify the size.
eg:-
--
with open('dot.txt' , 'r') as do:
    print(do.read(10))
    

readline()
---------
--> This readline() function will read only one line at a time..
eg:-
--
with open('dot.txt' , 'r') as do:
    print(do.readline())


readlines()
----------
--> This function will read whole file and give it in a list each line is one index in that list...
eg:-
--
with open('dot.txt' , 'r') as do:
    print(do.readlines())


























