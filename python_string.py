TOPIC: String Based Questions
-----------------------------

1. Write a Python program that takes a string as input and prints the length of the string.

//code:
st = input("Enter a string: ")
count=0
for char in st: 
  count+=1
print("length of the string is: ",count)

//o/p:
Enter a string: hello world
length of the string is:  11


2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.

//code:
st = input("Enter a sentence: ")
vowel=0
for char in st:
  if char in set("aeiouAEIOU"):
    vowel+=1
print("Count of vowels: ",vowel)

//o/p:
Enter a sentence: I like to eat banana
Count of vowels:  9

3. Given a string, reverse the order of characters using string slicing and print the reversed string.

//code:
txt="Hello world"
rev = txt[::-1]
print("string: ",txt)
print("Reverse string: ",rev)

//o/p:
string:  Hello world
Reverse string:  dlrow olleH


4. Write a program that takes a string as input and checks if it is a palindrome
(reads the same forwards and backwards).

//code:
txt = input("Enter a string: ")
rev = txt[::-1]
if txt == rev :
  print("The string is a pallindrome")
else:
  print("The string is not a pallindrome")

//o/p:
Enter a string: malayalam
The string is a pallindrome

Enter a string: hello
The string is not a pallindrome


5. Create a program that takes a string as input and removes all the spaces from it. 
Print the modified string without spaces.

//code:
txt = input("Enter a string: ")
newtxt = ''.join(txt.split())
print("String: ",txt)
print("String without space: ",newtxt)

//o/p:
Enter a string: Hello how are you
String:  Hello how are you
String without space:  Hellohowareyou


