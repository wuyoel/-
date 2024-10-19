'''
print("Use read()")
f = open("name.txt")
content = f.read()
print(content)
'''

'''
print("\nUse readline()")
f = open("name.txt")
content = f.readline()
print(content, end="")
content = f.readline()
print(content, end="")
content = f.readline()
print(content, end="")
'''

'''
print("\n\nUse readline() and strip()")
f = open("name.txt")
content = f.readline().strip()
print(content, end="")
content = f.readline().strip()
print(content, end="")
content = f.readline().strip()
print(content, end="")
'''

'''
print("\n\nUse seek()")
f = open("name.txt")
content = f.readline()
print(content, end="")
content = f.readline()
print(content, end="")
# use seek here
f.seek(0)
content = f.readline()
print(content, end="")
'''

'''
f = open("name.txt")
print("\nUse for loop")
for line in f:
    print(line.strip())
f.close()
'''

'''
print("\nUse with...as..")
with open("name.txt") as f:
    for line in f:
        print(line.strip())
'''

# Open for writing
'''
lst = "Hello World!"
with open('helloWorld.txt', 'w') as f:
    f.write(lst+'\n')
'''

# 試著把下⾯的list寫進一個叫做country.txt的檔案中，每印出一個城市名字就換 一行
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
i=0
with open('country.txt','w') as f:
    for i in range(0,len(country)):
        print(f.write(country[i]+'\n'))


# 請先把下⾯這兩個list組合成一個dict
# country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
# mayor= ["柯⽂哲","侯友宜","張善政","盧秀燕","黃偉哲","陳其邁"]
# 然後把這個dict寫進剛剛的country.txt，不可以覆蓋剛剛已經存在的內容，把新的內容加在原本內容的後⾯



