from sys import argv
print(argv)


# 讓使⽤者直接在執行檔案的時候輸入自己的名字並且印出來
# 同時檢查使⽤者是否有輸入名字，沒有的話印出Guest
if len(argv) == 2:
    print("Guest is "+argv[1])
