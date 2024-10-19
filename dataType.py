# integer
print("\n",end='')
print("Thses are integers")
print("2 = ",end='')
print(2)
print("2 + 2 = ",end='')
print(2+2)
print("2 - 2 = ",end='')
print(2-2)
print("2 * 2 = ",end='')
print(2*2)
print("3 // 2 = ",end='')
print(3//2) #取除數
print("12 % 5 = ",end='')
print(12%5) #取餘數
print("2 ** 3 = ",end='')
print(2**3) #次方
print("\n",end='')


# float
print("Thses are floats")
print("0.2 = ",end='')
print(0.2)
print("1.3e4 = ",end='')
print(1.3e4)
print("0.2 + 2 = ",end='')
print(0.2+2)
print("0.2 - 2 = ",end='')
print(0.2-2)
print("0.2 * 2 = ",end='')
print(0.2*2)
print("3 / 2 = ",end='')
print(3/2)
print("4.2 % 3.2 = ",end='')
print(4.2%3.2)
print("0.5 ** 2 = ",end='')
print(0.5**2)
print("\n",end='')

# boolean
print("Thses are booleans")
print("Is 0.2 an interger? ")
print(0.2.is_integer())
print("Is 2.0 an interger? ")
print(2.0.is_integer())
print("\n",end='')

# string
print("I'm a string!")
String_a = 'h'
String_b = "ello"
print("String_a = " + String_a)
print("String_b = " + String_b)
print("String_a + String_b = " + String_a + String_b)
print("\n",end='')

print("跨行的字串")
String_c = """
First Line
Second Line
Third Line"""
print("Sring_c = " + String_c)
print("\n",end='')

print("格式化輸出")
string = 'My name is {0}, I am {1} years old.'.format('margies', 22)
print(string)
string = 'My name is {name}, I am {age} years old.'.format(name='margies', age=22)
print(string)
print("\n",end='')

# list
print("A list contains multiple elements")
list_a = ["margies", 22, 3.1415]
print(list_a)
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[-1])
print("\n",end='')

print("Adding an element into the list")
list_a.append("New element")
print(list_a)
print("\n",end='')

print("Poping an element out of the list")
list_a.pop(2)
print(list_a)
print("\n",end='')

print("Sort the list")
list_b = [12,4,7,2,3,1]
print(list_b)
list_b.sort()
print(list_b)
print("\n",end='')

# tuple
print("Tuple is like a list, however cannot be edit")
tuple_a = (1,2,3)
print(tuple_a)
print("\n",end='')

# dictionary
print("Dictionary contains key and value pair")
dic_a = {'name':'margies', 'age':22}
print(dic_a['name'])
print(dic_a['age'])
print("\n",end='')
print("Assign a new column to the dictionary")
dic_a['school'] = 'NSYSU'
print(dic_a)
print("\n",end='')

# set
print("Set is nonordinal and do not contains replicated element")
set_a = {"Justin", "Sam", "Sam", "Tom"}
print(set_a)
set_a.add("Carmen")
set_a.add("John")
set_a.remove("Sam")
print(set_a)
print("\n",end='')