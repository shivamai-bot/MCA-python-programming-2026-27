terms = int(input("Enter the number of terms: "))

first = 0
second = 1
series_sum = 0

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(first, end=" ")
        series_sum = series_sum + first
        
        next_term = first + second
        first = second
        second = next_term

    print()
    print("Sum of the generated terms:", series_sum)
