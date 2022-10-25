num1 = 42 #variable declaration of int 
num2 = 2.3#variable declaration float
boolean = True # variable declaration of a boolean that is true
string = 'Hello World' #assignning a sstring to a variable call string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #assignning a list to the variable call pizza_toppings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #this is a dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) # printing the data type of fruit
print(pizza_toppings[1])# printing the second value in the list
pizza_toppings.append('Mushrooms') #adding mushrooms to the list of pizza_toppings
print(person['name']) # printing the person dictionary at the key of [name]
person['name'] = 'George'# adding a value in the key of name
person['eye_color'] = 'blue'# adding another entry to the dictionary    
print(fruit[2]) #printing the third indexes of the fruit tuple

if num1 > 45:#conditional
    print("It's greater")#will print a string after the conditional is met
else:
    print("It's lower")# action of what to do wen conditional has not been met

if len(string) < 5:#checking the length of the string 
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):#loop
    print(x)
for x in range(2,5):#loop
    print(x)
for x in range(2,10,3):#loop
    print(x)
x = 0 #variable
while(x < 5):#while loop
    print(x)
    x += 1

pizza_toppings.pop()#removing the last value in the list
pizza_toppings.pop(1)#removing second value of the list

print(person)
person.pop('eye_color')#removing the eye_color dict entry
print(person)

for topping in pizza_toppings:#iteratting throught the list values
    if topping == 'Pepperoni':#parameter checking if its a 'pepperoni'
        continue
    print('After 1st if statement')#printing after parameter is met
    if topping == 'Olives':
        break# exiting the loop

def print_hello_ten_times():#function that prints hello ten times
    for num in range(10):#iteratting 
        print('Hello')

print_hello_ten_times()#calling function one

def print_hello_x_times(x):#function prints hello wen 2 variables are pass down num,x
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #calling function 4 times

def print_hello_x_or_ten_times(x = 10):#function that prints hello
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#calling function
print_hello_x_or_ten_times(4)#calling function 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
# print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)