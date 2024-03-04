def count_chars():
    print("enter * to exit..")
    lower = upper = numbers = 0
    while True:
        char = input("Enter any charcter ")
        if char == '*':
            break
        elif char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            numbers += 1
    return lower, upper, numbers

lower, upper, numbers = count_chars()
print("Total count of upper case:", upper)
print("Total count of lower case:", lower)
print("Total count of numbers:", numbers)
