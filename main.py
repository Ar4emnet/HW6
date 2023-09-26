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
list1 = []
for i in range(10):
    list1.append(randint(-100,100))
print(list1)
print("product list ",product_list(list1))
print("min list ",min_list(list1))