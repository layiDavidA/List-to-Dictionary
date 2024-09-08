# Conversion of two list into Dictionary Using Python

def litodi():
    list0 = input("enter list 1\t")
    list0 = list0.split()
    list0 = list(list0)
    list1 = input("enter list 2\t")
    list1 = list1.split()
    list1 = list(list1)

    conversion = dict(zip(list0, list1))
    print(conversion)


litodi()
