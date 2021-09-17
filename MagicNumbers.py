num = int(input("Enter a number: "))
iterator = 0
digits_list = []
rr = []

def check_eq(lst):
    first = lst[0]
    status = True

    for element in lst:
        if first != element:
            status = False
            break
        else:
            status = True
    return status


for i in range(1, num+1):
    if len(str(i)) == 1:
        iterator += 1
    else:
        digits_list = list(map(int, str(i)))
        if check_eq(digits_list):
            iterator += 1


print(check_eq(digits_list))




print(iterator)
#print(digits_list)





print("----------------------------------------------------")







# Python3 code to demonstrate
# conversion of number to list of integers
# using map()

# initializing number
num = 2019

# printing number
print ("The original number is " + str(num))

# using map()
# to convert number to list of integers
res = list(map(int, str(num)))

# printing result
print ("The list from number is " + str(res))
