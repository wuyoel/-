# while
# 一直接收輸入值並印出，直到一個負數為止
'''
n = int(input("Please input an integer: "))
while (n >= 0):
    print(n, " is no less than 0")
    n = int(input("Please input an integer: "))
print("The end")
'''

# break
'''

while True:
    n = int(input("Please input an integer: "))
    if (n<0):  break
    print(n, " is no less than 0")    
print("The end")
'''

# continue
'''
a = 0
while(a < 10):
    a += 1
    if(a == 5):
        continue
    print(a)
print("The end")    
'''


# 印出100以內11的倍數
lst = range(1,101)
print([i for i in lst if i%11==0])

‘’‘
lst = range(1,101)
multiple = []
for i in lst:
    if (i%11==0):
        multiple.append(i)
print(multiple)
'''