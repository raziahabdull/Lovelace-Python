# def add (x,y):
#     result = x + y
#     return result

# print(add(1000,200))

# def subtract (x,y):
#     result = x - y
#     return result 

# print(subtract(200,50) )

# def divide (m,n):
#     result = m/n
#     return result
# print(divide(50,2))

# def multiply (x,y):
#     result = x*y
#     return result
# print(multiply(3,4))

# def remainder (x,y):
#     result = x % y
#     return result
# print(remainder(7,2))

# def sum(*numbers):
#     total = 0
#     for number in numbers:
#        total += number
#     return total

# def multiply_many(* numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# def sum_and_greet(*args,**kwargs):
#     total = 0
#     for x in args:
#         total += x

#     f = kwargs["first_name"]
#     l = kwargs["last_name"]
#     greeting = f"Hello {f} {l} the sum of your numbers is {total}"
#     return greeting

# def greetings(*args,**kwargs):
#     l = 2024 - student.age
#     for student in students.values():
    
#     f = kwargs["name"]
# sentence = f "Hello {f} you were born in the year{l}"
# return sentence

def student_score(**scores):
    sum = 0
    for score in scores.values:
        sum += score
    print(sum)