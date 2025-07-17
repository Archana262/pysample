# def square(num):
#     return num**2
# object_=square(6)
# print("the square of the given number is :",object_)

# def square(num):
#     print(num**2)
# square(6)

# def a_function(string):
#     return len(string)

# print(a_function("functions"))
# print(a_function("python"))


#with argument with return type
# def square (num):
#     return num*num
# result=square(5)
# print("square:",result)


#with argument without return type
# def greet (name):
#     print("hello",name + "!")
# greet("anu")

#without argument with rteturn type
# def get_message():
#     return "welcome to python programming!"
# msg=get_message()
# print(msg)

#without argument without return type
# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers()


#default argument
# def function(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("passing only one argument")
# function(30)


#keyword argument
# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("without using keyword")
# function(n2=50,n1=20)


# def fun(name,age):
#     print(f"my name is {name} i am {age} years old")

# fun(name="archana",age=20)


# def display(**a):
#     print(f"hi {a['name']} welcome to {a['course']}course")
# display(name="archana",course="python")



# def addition(x,y):
#     ans=x+y
#     print(ans)
# display(message=f"sum of{x} and{y} is",answer=ans)
# while True:

#     print("1.ADDITION")
#     print("2.SUBTRACTION")
#     print("3.MULTIPLICATION")
#     print("4.DIVISION")
    
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print("please enter your choice:\n1.addition \n2.subtraction \n3.multiplication \n4.division")
#     choice=int(input("enter your choice 1,2,3,4: "))
#     if choice==1:
#        addition(a,b)
#     elif choice==2:
#         sub=a-b
#         print(sub)
#     elif choice==3:
#         mul=a*b
#         print(mul)
#     elif choice==4:
#         div=a/b
#         print(div)
#     else:
#         print("please enter a valid input from the choice given")
#     c=input("do you wish to continiue (yes/no)?")
#     if c.lower()!="yes":

#         break


# while True:

#     print("1.ADDITION")
#     print("2.SUBTRACTION")
#     print("3.MULTIPLICATION")
#     print("4.DIVISION")
    
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print("please enter your choice:\n1.addition \n2.subtraction \n3.multiplication \n4.division")
#     choice=int(input("enter your choice 1,2,3,4: "))
#     if choice==1:
#       def addition(x,y):
#     ans=x+y
#     print(ans)
#     display(message=f"sum of{x} and{y} is",answer=ans)
#     elif choice==2:
#         sub=a-b
#         print(sub)
#     elif choice==3:
#         mul=a*b
#         print(mul)
#     elif choice==4:
#         div=a/b
#         print(div)
#     else:
#         print("please enter a valid input from the choice given")
#     c=input("do you wish to continiue (yes/no)?")
#     if c.lower()!="yes":

#         break





# for r in range(6):
#     for j in range(1,r+1):
#         print(j,end=" ")
        
#     print("")


# for r in range(1,6):
#     num=r
#     for st in range(1,r+1):
#         print(num,end=" ")
#         num+=r
#     print()

# for r in range(1,6):
    
#     for st in range(1,r+1):
#         print(st*r,end=" ")
        
#     print("")


# for r in range (5):
#     n=65
#     for j in range(r+1):
#         print(chr(n),end=" ")
#         n+=1
#     print("")


a=10
def b():
    global a
    a+=10
b(5):