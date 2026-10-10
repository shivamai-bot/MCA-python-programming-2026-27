while True:
    print("\n--- MATHEMATICAL MENU ---")
    print("1. Check Prime Number")
    print("2. Check Palindrome Number")
    print("3. Check Armstrong Number")
    print("4. Calculate Factorial")
    print("5. Generate Fibonacci Series")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        num = int(input("Enter an integer: "))
        if num <= 1:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
            
    elif choice == 2:
        num = int(input("Enter an integer: "))
        if num < 0:
            print("Negative numbers are not palindromes.")
        else:
            original = num
            reversed_num = 0
            temp = num
            while temp > 0:
                remainder = temp % 10
                reversed_num = (reversed_num * 10) + remainder
                temp = temp // 10
            if original == reversed_num:
                print(original, "is a palindrome.")
            else:
                print(original, "is not a palindrome.")
                
    elif choice == 3:
        num = int(input("Enter an integer: "))
        if num < 0:
            print(num, "is not an Armstrong number.")
        else:
            temp = num
            count = 0
            while temp > 0:
                count = count + 1
                temp = temp // 10
            temp = num
            armstrong_sum = 0
            while temp > 0:
                digit = temp % 10
                armstrong_sum = armstrong_sum + (digit ** count)
                temp = temp // 10
            if num == armstrong_sum:
                print(num, "is an Armstrong number.")
            else:
                print(num, "is not an Armstrong number.")
                
    elif choice == 4:
        num = int(input("Enter an integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial = factorial * i
            print("Factorial of", num, "is", factorial)
            
    elif choice == 5:
        terms = int(input("Enter the number of terms: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            first = 0
            second = 1
            print("Fibonacci series:")
            for i in range(terms):
                print(first, end=" ")
                next_term = first + second
                first = second
                second = next_term
            print()
            
    elif choice == 6:
        print("Exiting the application. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a valid option between 1 and 6.")
