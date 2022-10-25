# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# def countdown(num):
#     num_list=[]
#     for x in range(num,-1,-1): 
#         num_list.append(x)
#     return num_list
# countdown(9)
# print(countdown(9))

# # Example: countdown(5) should return [5,4,3,2,1,0]

# # Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# # Example: print_and_return([1,2]) should print 1 and return 2

# def list2(x_list):
#     print(x_list[0])
#     return x_list[1]

# print(list2([2,3]))
# new_list=['no','yes']
# print(list2(new_list))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# def sum_of(a_list):
#     result = len(a_list) + int(a_list[0])
#     return result
# sum_of(['2', '3'])
# print(sum_of(['2', '3']))

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# def acepted_list(some_list):
#     new_list=[]
#     for i in range (len(some_list)):
#         if some_list[i] > some_list[1]:
#             new_list.append(some_list[i])
#     return new_list
# acepted_list([2,3,4,5,6,7,8])
# print(acepted_list([2,3,4,5,6,7,8]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# def create_list(size, value):
#     some_list=[]
#     for i in range(size):
#         some_list.append(value)
#     return some_list
# print(create_list(5,3))
