# list
grades = [80, 90, 40, 70, 89, 100, 'A', 'A', 'B', 'C', 'A', 'B', 'C']
print(grades[0])
print(grades[5])
print(grades[6])
print(len(grades))

grades.append('F')
print(grades)

grades.insert(6, 95)
print(grades)

high_index = grades.index(100)
print(high_index)

grades.pop()
print(grades)


grades2 = [80, 90, 40, 70, 89, 100]
grades2.sort()
print(grades2)

# tuple
grades3 = (80, 90, 40, 70, 89, 100, 'A', 'A', 'B', 'C', 'A', 'B', 'C')
print(grades3)

# set
set1 = {1, 2, 3, 4, 1, 4, 6, 8, 6}
set2 = {1, 2, 3, 4, 6, 8}
set3 = {8, 6, 4, 3, 2, 1}
print(set1 == set2)
print(set2 == set3)

print(set1 is set2)
print(id(set1), id(set2))

# dictionary
grades = {'01':80, '02':90, '03':40, '04':70, '05':89, '06':100, '07':'A', '08':'A', '09':'B'
, '10':'C', '11':'A', '12':'B', '13':'C'}
grades['05']

grades['05']=90
grades['05']

grades['14']='A'
print(grades)

grades.pop('01')
print(grades)

print(len(grades))
