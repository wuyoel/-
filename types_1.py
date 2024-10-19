# Test of integer and float
a = 10
b = 5
c1 = a / b
c2 = a // b
print("c1 = {0}, type of c1 is {1}".format(c1, type(c1)) )
print("c2 = {0}, type of c2 is {1}".format(c2, type(c2)) )

# Test of string
x = 5
print("黃三益教授排行第"+str(x))

# Test of List
Grade = [ 5 , 6 , 7 , 8 , 9 , 10 , '資訊管理學系' , 9.54 ]
Grade.append('last')
Grade.extend(['e1','e2', 6])
print(Grade)
print(Grade.count(6))
print(Grade.index(6))
print(Grade.index(6, 3))
Grade.insert(2, 5.5)
print(Grade)
Grade.pop(2)
print(Grade)
Grade.remove(6)
print(Grade)
Grade.reverse
print(Grade)
Numbers = [3, 5, 1, 5, 7, 2, 3, 9]
print(Numbers)
Numbers.sort()
print(Numbers)
Numbers.sort(reverse=True)
print(Numbers)

#Test of Set
s1 = {1, 1, 2, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5}
print(s1 == s2)
print(s1 is s2)
print('id of s1 = {0}'.format(id(s1)))
print('id of s2 = {0}'.format(id(s2)))

#Test of dic
scores = {'張三': 100, '李四': 70, '王五': 90}
print(scores['李四'])
scores['李四'] = 75
del scores['王五']
print(scores)
print(len(scores))
print(scores.keys())
print(scores.values())
print(scores.items())

#Test of escape characters
print("李強\t\t", 80)
print("習近平\t\t", 90)
print("瓦歷斯諾幹\t", 100)