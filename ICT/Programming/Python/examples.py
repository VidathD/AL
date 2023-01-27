#!/usr/bin/env python3

def example1():
    a=10
    b="Saman"
    print(a)
    print(b)
    a="10"
    print(a+b)

def example2():
    a=6
    a="Kamal"
    print(a)

def example3():
    x="a programming language"
    print("Python is " + x)

def example4():
    a=int (5)
    b=int (4.6)
    c=int ("2")
    print ("a = ", a)
    print ("b = ", b)
    print ("c = ", c)

def example5():
    a=float (2)
    b=float (3.8)
    c=float ("4")
    d=float ("5.2")
    print ("a = ", a)
    print ("b = ", b)
    print ("c = ", c)
    print ("d = ", d)

def example6():
    a=str ("NIE")
    b=str (4)
    c=str ("8.0")
    print ("a = ", a)
    print ("b = ", b)
    print ("c = ", c)

def example7():
    a = "Welcome to, Ice Age !'' World! "
    print(a[1])
    print(a[3:5])
    print(a.strip())
    print(len(a))
    print(a.lower())
    print(a.upper())
    print(a.replace("e","a"))
    print(a.split(" ",))

def example8():
    print("Enter your name :")
    a = input()
    print("Hello, " + a)

def example9():
    M1 = 7
    M2 = 8
    print("M1+M2 =", M1+M2)

def example10():
    a = 6
    b = "Ravi"
    print(a+b)

def example11():
    x = int(input("Enter your ICT marks :"))
    if x>=75:
        print("You are qualified for scholarship")