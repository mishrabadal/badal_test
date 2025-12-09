# old_age=input("input your age : ")
# new_age=int(old_age)+2
# print("your new age is "+str(new_age))

#if else practise
# x=4
# if(x==6):
#     print("yes equal")
# elif(x>6):
#     print("greater than 6")
# else:
#     print("smaller than 6")

#squaring practise
# from math import sqrt
# print(sqrt(4))

# i=1
# while i<=5:
#     print(i)
#     i=i+1

# for i in range(5):
#     print(i+1)

# name="badal kumar"
# print(name.find('k'))
# print(name.replace('badal','shubham'))

# i=1
# while i<=5:
#     print(i*"*")
#     i=i+1

# i=5
# while i>=0:
#     print(i*"*")
#     i=i-1

#---------list in python----------------
# marks =[97,87,65,54]
# marks.append(99)
# marks.insert(0,88)
# print(marks)
# marks.clear();
# print(marks)
# for score in marks:
#     print(score)


# students=["ram","badal","shubham","shyam","mohan"]
# for student in students:
#     if(student=="shyam"):
#         continue
#     print(student)

#tuple in python---(not mutable lists)-------------
# marks={97,87,64,84,48,83,98}
# for score in marks:
#     print(score)

#sets in python(not accept duplicate values)
# marks={"name":"badal","class":6,"branch":"cse"}
# print(marks["branch"]).

#fuction declaration in python-----------
# def print_sum(first,second):
#     print(first+second)

# print_sum(5,7)

# for i in range(5,10):
#     print(i,"😂")

# print(5**2)
# count=1
# while count<=5:
#     print(count)
#     count+=1

#inheritance example
# class person:
#     name="badal"
#     def hello(self):
#         print("hello world")

# class animal:
#     def speak(self):
#         print("animal speak")

# class dog(animal):
#     def bark(self):
#         print("dogs is barking")       
# obj=dog()
# obj.speak()
# obj.bark()

#constructor
# class person:
#     def __init__(self):
#         print("namste bharat")
# obj = person()

#polymorphism

class bird:
    def sound(self):
        print("chirp")

class duck(bird):
    def sound(self):
        super().sound()
        print("quack")

d=duck()
d.sound()