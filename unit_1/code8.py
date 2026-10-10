side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
        
    print("The sides form a valid", triangle_type, "triangle.")

else:
    print("The given sides do not form a valid triangle.")

