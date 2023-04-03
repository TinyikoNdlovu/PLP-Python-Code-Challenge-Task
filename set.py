setnum1 = input("Enter first list of numbers separated by space: ")

setnum2 = input("Enter second list of numbers separated by space: ")

newset = {}

# newset = setnum1.intersection(setnum2)
# print(newset)


for newset in setnum1:
    if newset in setnum2:
        print(newset)

