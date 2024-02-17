# for i in range(1,11):
#     print(i)

# students = ['joy','faith','moyo','sola','pemi']
# for student in students:
#      print(student)
 
 # append add new item to the list (end of list)
# cocacola =['coke','fanta','7up','bigcola']
# cocacola.append('pepsi')
# print(cocacola)
 
 #insert add new item to a specify position
# bank = ['access','uba','unity','polaris']
# bank.insert(0, 'first-bank')
# print(bank)
 
 #sort arrange the list items alphabetically
# bank = ['access','uba','unity','polaris']
# bank.sort()
# print(bank)

# the below lines of code replace milky for item in(0)  

# cookies = ['speedy','wavers', 'spicy','chocobite']
# cookies[0] = 'milky'
# print(cookies)

#slice is used to cutoff some item from the list
# cookies = ['speedy','wavers', 'spicy','chocobite']
# cookies.sort(reverse=True)
# print(cookies[1:])

# name = input("what's your name? ")
# print(f"hello,  {name}")


# slice[:] is use to create copy of list items 
# my_fruit = ['banana', 'orange', 'pawpaw', 'apple']
# my_friends_fruit = my_fruit[:]
# my_fruit.append ('strawberry')
# print("my Favorite fruits are: ")
# print(my_fruit)
# print("\nmy friend's Favorite fruits are: ")
# print(my_friends_fruit)

# name = input("what's your name? ")
# house = input("where do you live? ")
# print(f"{name} from {house} ")

names = []
for _ in range (3):
    names.append(input("what is your name? "))
for name in sorted (names):
    print(f"hello, {name} ")




