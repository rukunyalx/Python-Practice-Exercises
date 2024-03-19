def count_special_char (string):
    count = 0

    for char in string:
        if not (char.isalpha() and not char.isdigit() and not char.isspace()):
            count += 1

    return count 


string = "Alex##"
print (count_special_char(string))
