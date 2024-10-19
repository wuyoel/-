# import bank
import bank

accountProperty = {'margies':[], 'john':[]}

accountName = str(input("Please input the account name, margies or john? "))
propertyList = accountProperty[accountName]
bank.addProperty(propertyList, 30)
print(propertyList)
bank.addProperty(propertyList, 40)
print(propertyList)
bank.addProperty(propertyList, 50)
print(propertyList)

print(accountName, bank.accountTotal(propertyList))