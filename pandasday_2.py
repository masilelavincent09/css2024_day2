# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:56:53 2024

@author: 27736
"""




"""
absolute path:
    
    C:/Users/27736/css2024day_2/data_02/iris.csv
    
    relative path:
data_02/iris.csv
"""

import pandas as pd

"""
file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")      

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
print(file)
"""

file_1 = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

_2 = pd.read_excel("data_02/residentdoctors.xlsx")


file_3 = pd.read_json("data_02/student_data.json")
print(file_3)

df = pd.read_csv("data_02/country_data_index.csv")

print(df)

df = pd.read_csv("data_02/country_data_index.csv", index_col=0)
print(df)

df = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())
df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())

df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
print(df.info())

"""
working with dates
"""

file = pd.read_csv("data_02/time_series_data.csv", index_col=0)
print(file.info())


file['Date'] = pd.to_datetime(file['Date'], format= "%Y-%m-%d")

file['Date'] = pd.to_datetime(file['Date'])

print(file.info())

file['Year'] = file['Date'].dt.year
file['month'] = file['Date'].dt.month
file['day'] = file['Date'].dt.day
print(file)

df = pd.read_csv("data_02/patient_data_dates.csv")

df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

df.drop(index=26, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
#to replace
df.dropna(inplace = True)
df.loc[7, 'Duration'] = 45

print(df)


#Data Transformations

df = pd.read_csv("data_02/iris.csv")

col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2
df["sepal_length_sq_2"]= df["sepal_length"].apply(lambda x: x**2)

grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)

 

#######
df1= pd.read_csv("data_02/person_split1.csv")
df2= pd.read_csv("data_02/person_split2.csv")
 
df = pd.concat([df1,df2], ignore_index=True)
print(df)

###########

df1= pd.read_csv("data_02/person_education.csv")
df2= pd.read_csv("data_02/person_work.csv")

#inner join

df_merge_inner = pd.merge(df1,df2, on="id")

print(df_merge_inner)

df = pd.read_csv("data_02/iris.csv")
df['class'] = df['class'].str.replace('Iris-', '')

df = df[df['sepal_length'] >5]

df = df[df["class"] == "virginica"]

print(df)

#df.to_csv("pulsar.csv")


#solutions
"""
runfile('C:/Users/27736/css2024day_2/pandasday_2.py', wdir='C:/Users/27736/css2024day_2')
   id                   field  ... amount_of_students  campus
0   1        Computer Science  ...               3000       A
1   2  Biomedical Engineering  ...               4000       B
2   3                 Physics  ...               2000       A
3   4             Mathematics  ...               3100       C

[4 rows x 5 columns]
    Unnamed: 0  Age Gender       Country
0            0   39      M  South Africa
1            1   25      M      Botswana
2            2   29      F  South Africa
3            3   46      M  South Africa
4            4   22      F         Kenya
5            5   35      F    Mozambique
6            6   22      F       Lesotho
7            7   49      M         Kenya
8            8   30      M         Kenya
9            9   40      F         Egypt
10          10   30      M         Sudan
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 9 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
dtypes: float64(5), int64(2), object(2)
memory usage: 11.4+ KB
None
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    object 
dtypes: float64(5), int64(2), object(3)
memory usage: 12.7+ KB
None
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    int32  
dtypes: float64(5), int32(1), int64(2), object(2)
memory usage: 12.1+ KB
None
<class 'pandas.core.frame.DataFrame'>
Index: 366 entries, 0 to 365
Data columns (total 2 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Date         366 non-null    object 
 1   Temperature  366 non-null    float64
dtypes: float64(1), object(1)
memory usage: 8.6+ KB
None
<class 'pandas.core.frame.DataFrame'>
Index: 366 entries, 0 to 365
Data columns (total 2 columns):
 #   Column       Non-Null Count  Dtype         
---  ------       --------------  -----         
 0   Date         366 non-null    datetime64[ns]
 1   Temperature  366 non-null    float64       
dtypes: datetime64[ns](1), float64(1)
memory usage: 8.6 KB
None
          Date  Temperature  Year  month  day
0   2020-01-01    27.483571  2020      1    1
1   2020-01-02    24.308678  2020      1    2
2   2020-01-03    28.238443  2020      1    3
3   2020-01-04    32.615149  2020      1    4
4   2020-01-05    23.829233  2020      1    5
..         ...          ...   ...    ...  ...
361 2020-12-27    32.663695  2020     12   27
362 2020-12-28    24.456199  2020     12   28
363 2020-12-29    27.008559  2020     12   29
364 2020-12-30    28.450720  2020     12   30
365 2020-12-31    22.993898  2020     12   31

[366 rows x 5 columns]
       Duration       Date  Pulse  Maxpulse  Calories
Index                                                
0            60 2020-12-01    110       130     409.1
1            60 2020-12-02    117       145     479.0
2            60 2020-12-03    103       135     340.0
3            45 2020-12-04    109       175     282.4
4            45 2020-12-05    117       148     406.0
5            60 2020-12-06    102       127     300.0
6            60 2020-12-07    110       136     374.0
7            45 2020-12-08    104       134     253.3
8            30 2020-12-09    109       133     195.1
9            60 2020-12-10     98       124     269.0
10           60 2020-12-11    103       147     329.3
11           60 2020-12-12    100       120     250.7
12           60 2020-12-12    100       120     250.7
13           60 2020-12-13    106       128     345.3
14           60 2020-12-14    104       132     379.3
15           60 2020-12-15     98       123     275.0
16           60 2020-12-16     98       120     215.2
17           60 2020-12-17    100       120     300.0
19           60 2020-12-19    103       123     323.0
20           45 2020-12-20     97       125     243.0
21           60 2020-12-21    108       131     364.2
23           60 2020-12-23    130       101     300.0
24           45 2020-12-24    105       132     246.0
25           60 2020-12-25    102       126     334.5
27           60 2020-12-27     92       118     241.0
29           60 2020-12-29    100       132     280.0
30           60 2020-12-30    102       129     380.3
31           60 2020-12-31     92       115     243.0
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
class
Iris-setosa        25.1818
Iris-versicolor    35.4972
Iris-virginica     43.7980
Name: sepal_length_sq, dtype: float64
    id first_name     last_name                          email       ip_address
0    1      Ozzie    Everington   oeverington0@marketwatch.com    50.218.126.57
1    2   Sharlene     Bearsmore      sbearsmore1@shinystat.com   117.146.130.90
2    3    Yolanda        Adamou                 yadamou2@ow.ly    241.32.63.240
3    4    Myranda        Kloser         mkloser3@parallels.com    74.193.226.83
4    5    Winonah     Sandeford  wsandeford4@timesonline.co.uk  239.251.207.237
5    6      Ivory       Wingatt              iwingatt5@com.com    116.87.10.137
6    7       Egor  De Beauchamp        edebeauchamp6@wufoo.com   151.131.138.28
7    8      Jobie       Pashler              jpashler7@sun.com   188.154.228.79
8    9    Charity         Libby           clibby8@edublogs.org   47.216.160.225
9   10      Sadye       Poacher               spoacher9@nhs.uk    29.57.154.142
10  10      Sadye       Poacher               spoacher9@nhs.uk    29.57.154.142
11  11      Jaime       McGrill         jmcgrilla@virginia.edu      22.65.19.34
12  12      Perla      McKevany         pmckevanyb@yahoo.co.jp     182.44.72.83
13  13     Mickey        Domico          mdomicoc@stanford.edu   204.200.186.61
14  14     Brigid      Plaschke           bplaschked@yahoo.com   33.247.110.109
15  15     Vinita        Rapley          vrapleye@marriott.com   145.114.16.112
16  16   Gennifer        Coupar               gcouparf@gnu.org  250.228.216.206
17  17     Dorita     Wilbraham         dwilbrahamg@uol.com.br    103.54.57.216
18  18    Thaxter         Gunby            tgunbyh@skyrock.com  175.214.186.108
19  19    Iseabal        Cabble          icabblei@netvibes.com    111.74.212.26
20  20     Darcey        Bissex              dbissexj@blog.com   62.197.134.253
     id  ...                 Skill
0     1  ...   Process Engineering
1     2  ...                   GTK
2     3  ...  Juvenile Delinquency
3     4  ...                 UTRAN
4     5  ...                  Zmap
..  ...  ...                   ...
95   96  ...          Microbiology
96   97  ...             Brain Gym
97   98  ...                 Visio
98   99  ...     Employee Benefits
99  100  ...      NIR Spectroscopy

[100 rows x 6 columns]
     sepal_length  sepal_width  petal_length  petal_width      class
100           6.3          3.3           6.0          2.5  virginica
101           5.8          2.7           5.1          1.9  virginica
102           7.1          3.0           5.9          2.1  virginica
103           6.3          2.9           5.6          1.8  virginica
104           6.5          3.0           5.8          2.2  virginica
105           7.6          3.0           6.6          2.1  virginica
107           7.3          2.9           6.3          1.8  virginica
108           6.7          2.5           5.8          1.8  virginica
109           7.2          3.6           6.1          2.5  virginica
110           6.5          3.2           5.1          2.0  virginica
111           6.4          2.7           5.3          1.9  virginica
112           6.8          3.0           5.5          2.1  virginica
113           5.7          2.5           5.0          2.0  virginica
114           5.8          2.8           5.1          2.4  virginica
115           6.4          3.2           5.3          2.3  virginica
116           6.5          3.0           5.5          1.8  virginica
117           7.7          3.8           6.7          2.2  virginica
118           7.7          2.6           6.9          2.3  virginica
119           6.0          2.2           5.0          1.5  virginica
120           6.9          3.2           5.7          2.3  virginica
121           5.6          2.8           4.9          2.0  virginica
122           7.7          2.8           6.7          2.0  virginica
123           6.3          2.7           4.9          1.8  virginica
124           6.7          3.3           5.7          2.1  virginica
125           7.2          3.2           6.0          1.8  virginica
126           6.2          2.8           4.8          1.8  virginica
127           6.1          3.0           4.9          1.8  virginica
128           6.4          2.8           5.6          2.1  virginica
129           7.2          3.0           5.8          1.6  virginica
130           7.4          2.8           6.1          1.9  virginica
131           7.9          3.8           6.4          2.0  virginica
132           6.4          2.8           5.6          2.2  virginica
133           6.3          2.8           5.1          1.5  virginica
134           6.1          2.6           5.6          1.4  virginica
135           7.7          3.0           6.1          2.3  virginica
136           6.3          3.4           5.6          2.4  virginica
137           6.4          3.1           5.5          1.8  virginica
138           6.0          3.0           4.8          1.8  virginica
139           6.9          3.1           5.4          2.1  virginica
140           6.7          3.1           5.6          2.4  virginica
141           6.9          3.1           5.1          2.3  virginica
142           5.8          2.7           5.1          1.9  virginica
143           6.8          3.2           5.9          2.3  virginica
144           6.7          3.3           5.7          2.5  virginica
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

"""
 