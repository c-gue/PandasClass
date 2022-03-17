import pandas as pd

#pd.set_option("precision",2)

#Series = One Dimensional Array
#Dataframe = Two DImensional Array
    # Each column in a DF is a Series

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

eva = grades['Eva']

sam = grades.Sam

#using the loc and iloc methods

test2 = grades.loc["Test2"]

test1 = grades.iloc[0]

#For consecutive rows
# : = consecutive rows
    # need not be in list
test1_thru_test3 = grades.loc['Test1':'Test3']
# , = non-consecutive rows
    #[] - must be in list
test1_and_test3 = grades.loc[['Test1','Test3']]

test1_and_test2 = grades.iloc[0:2]

#View only Eva's and Katie's grades for Test1 and Test2
test1_and_test3_evakatie = grades.loc[:'Test2',['Eva','Katie']]
#print(test1_and_test3_evakatie)
#View only Sam's THRU Bob's grades for Test1 and Test 3
test1_thru_test3_sambob = grades.loc[['Test1','Test3'],'Sam':]
#print(test1_thru_test3_sambob)

#boolean Indexing
#select everyone with an A grade

grades_A = grades[grades>=90]

#create a dataframe for everyone with a B grade

grades_B = grades[(grades >= 80) & (grades < 90)]


#create a dataframe for everyone with an A or B grade

grades_A_or_B = grades[(grades >= 90) | (grades >= 80)]



#by student
print(grades.describe())

#by test
print(grades.T.describe())

#Exercise - Get the average of all the students grades on each test
print(grades.T.mean)

#sort rows by their indices (Test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column names (student names)
#axis = 1 indicates to sort by column indices
#axis = 0 indicates to sort by row indices
c_sorted_grades_i = grades.sort_index(axis=1, ascending=False)



print()