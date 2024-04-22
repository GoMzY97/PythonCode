#reverse string
string = "HEllo World"
reversed_string = string[::-1]
print(reversed_string)


#check if substring
string = "Hello world"
substring = "world"
if substring in string:
	print("Substring Found!")

#Find Max value
my_lisy = [1,6,3,9]
max_value = max(my_lisy)
print(max_value)

#Find index of max value
my_lisy = [1,6,3,9]
max_index = my_lisy.index(max(my_lisy))
print(max_index)

#Reversed a list
my_lisy = [1,6,3,9,4]
reversed_list = my_lisy[::-1]
print(reversed_list)

#sorting a dict
my_dict = {"apple": 3,"banana": 1,"orange": 2}
sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
print(sorted_dict)


#checking if file exists 
import os
if os.path.isfile("lmao.txt"):
	print("Files Exists")


#checking occurrences of an item in a list
my_list = [1,2,3,4,5,6,7,7,8,9]
count = my_list.count(7)
print(count)

#checking of all elemets  in a list are unique
my_list = [1,2,3,4,5]
if len(my_list) == len(set(my_list)):
	print("ALL elements are unique!")

#removing all occurrences of an item from a list
my_list = [1,2,3,4,5,6,5]
item = 2
my_list = [x for x in my_list if x != item]
print(my_list)

#Flattening a nested list
my_list = [[1,2], [3,4], [5,6]]
flat_list = [x for sublist in my_list for x in sublist]
print(flat_list)

#merging 2 dict
dict1 = {"apple": 3, "banana": 1}
dict2 = {"orange": 2,"pear": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)


#removing all white spaces
string = "     HELLO      World    "
new_str = "".join(string.split())
print(new_str)


#checking if a string is palindrome
string = "racecar"
if string == string[::-1]:
	print("String is PALINDROME!")

#removing Duplicates
string = "hello world"
new_str = "".join(set(string))
print(new_str)

#counting number os words in String
string = "HELLO WORLD"
word_count = len(string.split())
print(word_count)


#gen a random integer
import random
ran_no =  random.randint(1, 99)
print(ran_no)



#
