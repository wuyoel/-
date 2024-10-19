# string
name = 'Maggie'
age = 22.0
text = 'My name is %s, and I am %s'%(name, age)
print(text)
text = 'My name is {0}, and I am {1}'.format(name, age)
print(text)
text = 'My name is {first}, and I am {second}'.format(first = name, second = age)
print(text)