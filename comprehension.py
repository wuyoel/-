# Comprehension on list
lst = [1, 2, 3, 4, 5]
lst_sq_c = []
lst_sq_c = [num**2 for num in lst]
print(lst_sq_c)

#Comprehension on list with if
lst = [1, 2, 3, 4, 5]
lst_sq_c2 = []
lst_sq_c2 = [num**2 for num in lst if num%2==0]
print(lst_sq_c2)

# 請⽤comprehension的⽅式印出 1..101 中所有11的倍數

# Comprehension on dic
scores = [88, 90, 100, 65, 78]
score_dic = {student_id:score for student_id, score in enumerate(scores)}
print(score_dic)

names = ['caterpillar', 'justin', 'openhome']
passwds = [123456, 654321, 13579]
pairs = {name : passwd for name, passwd in zip(names, passwds)}
print(pairs)

# Exercise
country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
mayor= ["柯⽂哲","朱⽴倫","鄭⽂燦","林佳龍","賴清德","陳菊"]
# 請⽤comprehension的⽅式依照陣列裡的順序列出每個直轄市的市長，並存成 dictionary格式

