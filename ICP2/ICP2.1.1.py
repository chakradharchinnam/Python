lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
print("Please enter",n,"no of weights")
# iterating till the range
for i in range(0, n):
    ele = int(input())
# adding the element
    lst.append(ele)
# printing the list
print("Given the list of weights in the lbs(pounds)",lst)
kgs = [i*0.45359237 for i in lst]
print("Convert list of weights in Kilograms",kgs)
# coverting from lbs to kgs