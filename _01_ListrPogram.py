# Python program to find the sum of all the elements in the list.
# create initial  a list
List1 = [11, 5, 17, 18, 23]
print("the initial list=",List1)
count=0
#  add them in variable count
for ele in range(0, len(List1)):
    count = count + List1[ele]

# printing total count  value
print("Sum of all elements in given list: ", count)

#second approach
#USING while() loop

# create  a  initial list
List1ist1 = [11, 5, 17, 18, 23]
print("the initial list=:-",List1)
count = 0
ele = 0
# Iterate each element in list
#  add them in variable total
while (ele < len(List1)):
    count = count + List1[ele]
    ele += 1

# printing total value
print("Sum of all elements in given list: ", count)

#third Approach
#In recursive approach

# create  a list
List1 = [11, 5, 17, 18, 23]
print("the initial list",List1)

# Defining sum_list() function
def sumOfList(List1, size):
    if (size == 0):
        return 0
    else:
        return List1[size - 1] + sumOfList(List1, size - 1)

#Result is Stored in Count
count = sumOfList(List1, len(List1))

print("Sum of all elements in given list: ", count)

#Fourth Approach
#create initial List of elements
List1 = [11, 5, 17, 18, 23]
print("the initial list=",List1)

# using sum() function
total = sum(List1)

# printing sum of the all elements
print("Sum of all elements in given list: ", total)
