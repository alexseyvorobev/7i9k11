def PIP(n):
    if (n>0 & n<3021):
        if (n%4) == 0:
            if (n%100) == 0:
                 if (n%400) == 0:
                     print("Год не является високосным")
                 else: print("Год является високосным")
            else: print("Год является високосным")
        else: print("Год не является високосным")
    else: print("Введите другое число")
    a=0
    if (n%1000) == 0:
        a=(n//100)
        a=a+1
    else:
        a=(n//100)
        a=a+1
    print(a,"-век")
try:
    print("Введите год")
    n=int(input())
except ValueError:
    print("Incorrect value")
    exit()
PIP(n)        
