# students marks calculation 
sub1=float(input("Enter science marks :"))
sub2=float(input("Enter math marks :"))
sub3=float(input("Enter hindi marks :"))
sub4=float(input("Enter english marks :"))
sub5=float(input("Enter marathi marks :"))

total_marks= sub1 + sub2 + sub3 + sub4 + sub5
average_marks= total_marks / 5
percentage=(total_marks / 500)* 100

print("total marks is :", total_marks)
print("average marks is :", average_marks)
print("percentage is :", percentage)


