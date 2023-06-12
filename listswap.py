# Python Program to Swap Two Elements in a List 

NumList = []

Number = int(input("How many elements in list : "))

for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " % i))
    NumList.append(value)

print("\nList before swapping of elements :-\n", NumList)

position1 = int(input("Enter the position 1 of element, which you want to swap : "))
position2 = int(input("Enter the position 1 of element, which you want to swap : "))


# Swap function 
def swap_positions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


print("List after swapping of elements :\n", swap_positions(NumList, position1 - 1, position2 - 1))
