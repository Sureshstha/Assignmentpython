import datetime

# Write a function that inputs a list and returns the largest number in the list.

def maximum(x):
    x.sort()
    return x[-1]
n=int(input("Enter size of list"))
my_list=[]
for i in range(0,n):
    num=input("Enter elements")
    my_list.append(num)
print(list(my_list))
print("The largest number is",maximum(my_list))
#
#
#
# # Write a function that inputs a string and outputs the number of Upper case and Lower case characters in the string.
#
def check(s):
    d={"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"] += 1
        elif c.islower():
           d["LOWER_CASE"] += 1
        else:
           pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])
string = input("Enter the sentence with uppercase and lowercase")
check(string)


# Given a list [12, 21, 19, 28, 12, 20, 48, 19]. Remove all the duplicates from the list and display the filtered list.

set_list = [12, 21, 19, 28, 12, 20, 48, 19]
print(list(set(set_list)))

# Given you have a dictionary of post name with creation dates in Unix Time Stamp with format { post_name: timestamp }:
# dict = {'Post 1': '1484101485', 'Post 2': '1454301785', 'Post 3': '1494130145'}
# a. Display all the posts in dictionary.
# b. Create a function that converts the timestamp to readable format (Eg. 2018-02-12 10:00:00).
# c. Allow user to input the Post name (user enters post name) and display the related creation date using the created function. The message should say "Creation datetime of Post 1 is: 2017-01-11 08:09:45".

dict = {'Post 1': '1484101485', 'Post 2': '1454301785', 'Post 3': '1494130145'}
for key, value in dict.items():
    print(key)
for key, value in dict.items():
    readable = datetime.datetime.fromtimestamp(float(value))
    print(readable)

post = input("Enter the Post Name: ")
for key, value in dict.items():
    if key == post:
        readable = datetime.datetime.fromtimestamp(float(value))
        print("Creation datetime of {}".format(post) + "is ", readable)

