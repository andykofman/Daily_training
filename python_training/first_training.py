
# 1. Number Analyzer
# Write a program that asks the user to enter a sequence of numbers (one per line), ending with 'done'. It should print the:
# 
# Total count of numbers entered
# 
# Their sum
# 
# Average
# 
# Maximum and minimum


numbers = []

def count_numbers(numbers):
    count =0
    for i in numbers:
        count = count +1
    return count

def sum_numbers(numbers):
    sum = 0
    for i in  numbers:
        sum = sum + i
    return sum
    
def average(sum, count):
    average = sum / count
    return average

def maximum(numbers):
    largest = None
    for i in numbers:
        if largest is None or i > largest:
            largest = i 
    return largest
    
def minimum(numbers):
    smallest = None
    for i in numbers:
        if smallest is None or i < smallest:
            smallest = i
    return smallest

while True: 

    User_input = input('Please Enter the numbers, when finished enter done:')
    if User_input == 'done':
        print (numbers)
        count = count_numbers(numbers)
        sum = sum_numbers(numbers)
        average = average(sum, count)
        largest = maximum(numbers)
        smallest = minimum(numbers)
        print ('count is:', count)
        print ('the sum is:',sum)
        print ('average is', average)
        print ('Largest is', largest)
        print ('smallest is', smallest)
        break
    else:
        
        try: 
            value = int(User_input)
            numbers.append(value)
        
        except ValueError:
             print('please Enter numbers only')
