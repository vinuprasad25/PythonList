#Multiplying of Elements

List1 = [1, 2, 3]
List2 = [3, 2, 4]
#using traversal  way
def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

print(multiplyList(List1))
print(multiplyList(List2))

#using math library  function
import math

List1 = [1, 2, 3]
List2 = [3, 2, 4]

res1 = math.prod(List1)
res2 = math.prod(List2)
print(res1)
print(res2)