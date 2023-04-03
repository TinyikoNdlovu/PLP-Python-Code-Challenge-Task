input_string = input("Enter a list of numbers separated by space: ")
list  = input_string.split()
print("Calculating sum of all the numbers in the input list")
sum = 0
for num in list:
    sum += int (num)
print("Sum =",sum)
