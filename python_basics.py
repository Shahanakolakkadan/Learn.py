TOPIC: Python Basics Variable
-----------------------------

1. Declare two variables, `x` and `y`, and assign them integer values. 
Swap the values of these variables without using any temporary variable.

//code:
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
x=x+y
y=x-y
x=x-y
print("Value of x after swapping: ",x)
print("Value of y after swapping: ",y)

//o/p:
Enter the value of x: 40
Enter the value of y: 80
Value of x after swapping:  80
Value of y after swapping:  40


2. Create a program that calculates the area of a rectangle. Take the length and
width as inputs from the user and store them in variables. Calculate and display the area.

//code:
len = int(input("Enter the length of the rectangle: "))
wid = int(input("Enter the width of the rectangle: "))
area = len*wid
print("Area of rectangle is: ",area)

//o/p:
Enter the length of the rectangle: 10
Enter the width of the rectangle: 5
Area of rectangle is:  50


3. Write a Python program that converts temperatures from Celsius to Fahrenheit.
Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.

//code:
celc = int(input("Enter the temperature in celcius: "))
fahren = (9/5)*celc+32
print("Temperature in Fahrenheit: ",fahren)

//o/p:
Enter the temperature in celcius: 100
Temperature in Fahrenheit:  212.0







