# there are total 5 methods 
#   1. String to list of string 
#   2. string to list of characters 
#   3. List of string to List of Lists
#   4. CSV to List 
#   5. A string of integers to list of integers 



# 1. String to List of String

#given string
string1="Python is great"
#printing the string
print("Actual String: ",string1)
#gives us the type of string1
print("Type of string: ",type(string1))  
#prints the list given by split() 
print("String coverted to list :",string1.split()) 



# 2. String to list of characters

#given string
string1="AskPython"
#printing the string
print("Actual String: ",string1)
#confirming the type()
print("Type of string: ",type(string1))
#type-casting the string into list using list()
print("String coverted to list :\n",list(string1))



# 3.List of String to List of Lists 

#Given string
string1="This is Python"
print("The actual string:",string1) 
#converting string1 into a list of strings
string1=string1.split()
print("After split the string looks like :",string1)
#applying list method to the individual elements of the list string1
# list2= list(string1)
# print(list2)    this will print same like the line 43
list1=list(map(list,string1)) 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)



# 4.CSV (Comma Separated Values)to list 

#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
#spliting string1 into list with ',' as the parameter
print("CSV coverted to list :",string1.split(','))



# 5. A string consisting of integers to list of integers

#string with integers sepated by spaces
string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1))
#coverting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)