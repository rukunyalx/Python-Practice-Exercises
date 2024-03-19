string1 = input("enter a string")

character1 = input("enter a character")
print (character1)

count = 0

for char in string1.lower():
    if char == character1.lower():
        count += 1
print (count)


