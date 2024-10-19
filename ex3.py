#使用者輸入階層數，印出聖誕樹

# '''
level = int(input("Please enter the number of levels: "))
for i in range(1, level+1):
    for j in range(0, i):
        print("*", end='')
    print("\n")
#'''



cities = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
mayors= ["柯⽂哲","侯友宜","張善政","盧秀燕","黃偉哲","陳其邁"]
# 請⽤for迴圈印出這個每個直轄市名稱
for c in cities:
    print(c)
# 請⽤for迴圈印出這個每個直轄市對應的市長名字, e.g.
# 台北市: 柯⽂哲
# 新北市: 侯友宜
# ...

