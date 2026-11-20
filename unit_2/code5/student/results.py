# Student Results Module

def calculate_result(*marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)

    return total, average, highest