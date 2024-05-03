# Basic operations
def operation():
    num1 =int(input("Entetr the first number"))
    num2 = int(input("Entetr the second number"))
    print(f"The summation is {num1+num2}")
    print(f"The subtration is {num1-num2}")
    print(num1*num2)
    print(num1/num2)
    print(num1%num2) # reminder
    print(num1//num2) # floor division
    print(num1**num2)

def num_spr():
    num = input("Enter the number ")
    first = num[1]
    second = num[0]
    print(f" The first number is {first} and the second number is {second}")

def num_spr2():
    num = int(input("Enter the number "))
    first = num%10
    second = num//10
    print(f" The first number is {first} and the second number is {second}")

def main():
    
    
    colors =["BLACK"]
    for color in colors:
        print(color)
main()

# name = "Ahmad is Excellent"30
# print(name[-3:])




# def welcome_message():
    
#     name = "Basem"
#     print("My name is  "+ name)



def welcome_message():
    
    name = input("enter your name ")
    age = float(input("Enter your age "))
    print(f"My name is  {name} My age is  {age} ")

# welcome_message()

# name = "Ahmad is Excellent"
# print("is" not in name)
    


# print("My name is  "+ name)

















# def welcoming():
#     global name
#     name = 3
#     print(f"I love python and my name is {name} ")
#     print("Hi")




# welcoming()
















# print(name)
# name = "ahmad"
# txt= "hello, world" 
# print(txt[-8:-2])
    
welcome_message()