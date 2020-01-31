studentNo = int(input("Enter number of students = "))
# number of students as input
weightInLB = [(int(input("Enter weight for student :"))) for x in range(studentNo)]
print(weightInLB);
# age of students in lbs as input
weightInKG = [("{: .2f}".format(float(weightInLB[i] * 0.453592))) for i in range(studentNo)]
# convert the age in lbs to kgs
print(weightInKG)