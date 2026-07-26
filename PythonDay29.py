
     -: MatPlotlib :-
        ==========

--> Matplotlib library is an python library that provides functionality to charts , graphs , bar and data visualization.

Ex:-
--
#1.
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]
plt.plot(x,y)
plt.show()


#2.
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.plot(x,y)
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()

#3.
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]

plt.bar(x,y, color = 'yellow',edgecolor='blue')
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of Cars')
plt.show()


#4.
import matplotlib.pyplot as plt
subjects_ = ['Python', 'Java', 'C', 'C++', 'MySQL']
stu_ = [88, 153, 190, 67, 23]
plt.pie(stu_,labels=subjects_,autopct='%1.1f%%')
plt.legend(subjects_)
plt.title('Courses')
plt.show()


#5.
import matplotlib.pyplot as plt
subjects = ['Python', 'Java', 'C', 'C++', 'MySQL']
stu_ = [88, 153, 190, 67, 23]
plt.scatter(subjects, stu_, color = 'skyblue')
plt.legend(subjects)
plt.title('Courses')
plt.show()

#6.
import matplotlib.pyplot as plt
y = [10,40,20,50]
plt.hist(y,bins=20)
plt.title('Car Saless')
plt.xlabel('year')
plt.ylabel('Number of Cars')
plt.show()

'''






































































