'''
# method-1:-
from datetime import datetime
current_ = datetime.now()
print(current_)
print(current_.strftime('%Y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))
print(current_.strftime('%H:%M:%S'))


#method-2:-

from datetime import datetime, date
current_ = datetime.now()
today = date.today()
now = datetime.now()
print(today)
print(now)
print(current_.strftime('%d/%m/%Y %I:%H:%M:%S %p'))


%d --> day in the month
%m --> month in the year
%Y --> year
%H --> hour
%M --> minute
%S --> second
%I --> 12 hour clock
%p --> AM or PM


import calendar
print(calendar.calendar(2026))
print(calendar.month(2026,7))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2026))



Data Analysis :-
---- --------
--> It is used to clean the data
--> Transfer the data

1. What is Data Analysis?
   ---------------------
   Data Analysis is the process of inspecting , cleaning , transformation and modeling data to discover useful insights, support decision-making and identity patterns. IT is widely used in
   industries such as finance, healthcare, marketing and technology.



Types of Data analysis:-
----- -- ---- --------
1. Descriptive Analysis - Summarizing data
(e.g., average sales per month)

2. diagnostic Analysis - Understanding causes
(e.g., why sales dropped)

3. Predictive Analysis - Forecasting future outcomes
(e.g., predicating customer churn.)

4. Prescriptive Analysis - Suggesting actions based on data
(e.g., Best marketing Strategies.)


             -: "Numpy" :-
                -------
--> Numpy is a library in python which is known as numerical python
--> This Numpy have different dimensional arrays such as 1D,2D,3D
--> To used the Numpy we have to import library as import numpy as np

#Ex1:-
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_1)



Indexing in array:-
-------- -- -----
--> As we used indexing in the list or tuple, here the way it works
--> By calling index position from array, we will get the value
--> And Negative indexing also will work

ex: --> Negative indexing

import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1[1])

Eg:-
--
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())

import numpy as np
arr1_ = np.array([[1, 2, 3],[4, 5, 6]])
print(arr1_)
print(arr1_.reshape(3, 2))

arr2_ = np.array([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]])
print(arr2_)
print(arr2_.reshape(4, 3))




    -: Pandas :-
       ------
Pandas
------
--> Pandas is an powerful pythjon library and this is built on the top numpy
--> By used pandas data manipulation will be done..
--> Pandas have data structures like series and dataframes
--> To use this  we have import the library


import pandas as pd

Ex:-
--
import pandas as pd

Data = pd.Series(
    [2000,4000,7000],
    index = ['Earphone','Charger','Mobile']
)
print(Data)


ex2:-
--
import pandas as pd

df = {
    "Product" : ['Laptop','Charger','Mobile'],
    "Brand" : ['Mac','Realme','Iphone'],
    "Price" : [5700,1500,2500],
    "Stocks" : [5,15,9],
    "Sales" : ['Amazon','offline','Flipkart']
}
data = pd.DataFrame(df)
print(data)

'''











































































