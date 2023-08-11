def  number_range_checker():
    try:
    number =int(input("Enter number:"))
    if 0 <=  number  <=  10:
        print("Low range")
    elif 11 <=  number <= 50:
        print("Medium range")
    elif 51 <= number <=100:
        print("High range")
    else:
        print("out of range")

except ValueError:
    print("Invalid input . please enter a valid number")

