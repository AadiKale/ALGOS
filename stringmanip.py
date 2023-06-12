str1 = input("Enter the string : ")
str2 = str1
print("The copied string is ", str2)
# length
n = len(str1)
print(n)
# reverse
print(str1[len(str1) - 1::-1])
# find substring
str = str1
sub_str1 = input("enter sub string to find :")
print(str.find(sub_str1))
if str.find(sub_str1) == -1:
    print("not found")
else:
    print("found")
# concat
a = str1 + str2
print(a)
# source to destination
string1 = input("Enter a string :")
string2 = ""
for i in string1:
    string2 = string2 + i

print("Copied string =", string2)

# find sub string
string = input("Enter a string : ")
substring = input("Enter a word to check : ")

if substring in string:
    print("Your substring is present in the string")
else:
    print("Your substring is not present in the string")
    