# Q1. String Operations and String Methods

# Accept sentence
text = input("Enter a sentence: ")

# String Length
print("Length:", len(text))

# Uppercase and Lowercase
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Remove leading and trailing spaces
print("After Removing Spaces:", text.strip())

# Replace a word
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After Replacement:", text.replace(old, new))

# Count character occurrences
ch = input("Enter a character to count: ")
print("Character Count:", text.count(ch))

# Check starting and ending substring
start = input("Enter starting substring: ")
end = input("Enter ending substring: ")

print("Starts With:", text.startswith(start))
print("Ends With:", text.endswith(end))

# Concatenation
print("Concatenation:", text + " Welcome!")

# Repetition
print("Repetition:", text * 2)

# Membership Operator
word = input("Enter word to search: ")
print("Word Present:", word in text)