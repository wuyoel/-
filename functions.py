
'''
def functionName(a,b):
	print(a-b)

functionName(5, 2)
'''

'''
globalV = "3";

def iAmAFunction():
	localeV = "10"
	print("")
	print("Inside the function,")
	print("I can see the golbal variable is " + globalV)
	print("I can also see the locale variable is " + localeV)

iAmAFunction()
print("")
print("Outside the function,")
print("I can see the golbal variable is " + globalV)
print("However I can't see the locale variable " + localeV)
'''


# Exercise
# 請設計一個函數 sum() ,傳入一個正整數p,並回傳 1 到p 之間所有正整數的和
# 請設計一個函式 factorial() ,傳入一個正整數p,並計算p的階層值
# 請設計一個函式 fibonacci() ,傳入一個正整數p,並回傳費氏數列第p個元素的值

# Exercise
# 請寫一個猜數字的程式，程式隨機產生一個介於1~100的數字
# 撰寫一個函式判斷使⽤者猜的數字是否正確，⽽且使⽤者每次猜錯時都要提⽰他正確答案比他猜的還大或是還⼩

'''
import random
ans = random.randint(0,100)

def checkIfCorrect(guess):
	if(guess == ans):
		return 0  # correct
	elif (guess > ans):
		return 1 # too high
	else:
		return -1 # loo low

while True:
	g = int(input("Please enter your guess (between 0 and 100): "))
# Write the remaining code here


'''		


