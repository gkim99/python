num1 = 42 
#variable declaration, number
num2 = 2.3 
#variable declaration, number
boolean = True 
#boolean
string = 'Hello World' 
#variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
#variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#variable declaration, dictionary 
fruit = ('blueberry', 'strawberry', 'banana')
#variable declaration, tuple
print(type(fruit))
#type check
print(pizza_toppings[1])
#access list value 
pizza_toppings.append('Mushrooms')
#add list value 
print(person['name'])
#access dictionary value 
person['name'] = 'George'
#change dictionary value 
person['eye_color'] = 'blue'
#add dictionary key and value 
print(fruit[2])
#access tuple value 
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional statement

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    #length check, conditional statement

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
#for loop

x = 0
while(x < 5):
    print(x)
    x += 1
#while loop

pizza_toppings.pop()
#delete last list value 
pizza_toppings.pop(1)
#delete list value at index 1

print(person)
person.pop('eye_color')
print(person)
#delete eye_color key/value in dictionary 

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#for loop, conditional statement, break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#funtion, for loop

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#funtion with parameter x, for loop

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
#funtion with parameter x = 10, for loop
print_hello_x_or_ten_times(4)
#funtion with parameter x = 10, for loop, argument of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)


hh