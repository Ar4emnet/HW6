from random import randint

def product_list(list1):
    res = 1
    for number in list1:
        res *= number
    return res

def min_list(list1):
    res = list1[0]
    for number in list1[1:]:
        if res > number:
            res = number
    return res

def find_prime_number(list1):
    res = 0
    for number in list1:
        for i in range(number)[2:]:
            if (number % i) == 0:
                res += 1
    return res
def remove_number(list1):
    res = 0
    number = int(input("Write number for remove "))
    while number in list1:
        list1.remove(number)
        res += 1
    return "the number of deleted number "+str(res)
def plus_list(list1,list2):
    return list1+list2
def power_number(list1,):
    res = []
    numb = int(input("Write power for number "))
    for number in list1:
        number1 = number
        for i in range(numb-1):
            number1 *= number
        res.append(number1)
    return res
list1 = []
list2 = []
for i in range(10):
    list1.append(randint(-100,100))
    list2.append(randint(-100,100))
print(list1)
print("product list ",product_list(list1))
print("min list ",min_list(list1))
print("find primery numbers ",find_prime_number(list1))
print("list before remove number", end=" ")
print(list1)
print(remove_number(list1))
print("list after remove number", end=" ")
print(list1)
print("list1+list2", end=" ")
print(plus_list(list1, list2))
print(power_number(list1))