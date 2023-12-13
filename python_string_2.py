TOPIC: String Based Assignment Problem
--------------------------------------

1. Write a program to reverse a string.

METHOD 1:
---------
//code:
txt=input("Enter a string: ")
rev_txt = txt[::-1]
print(rev_txt)

//o/p:
Enter a string: Hello world
dlrow olleH

METHOD 2:
---------
//code:
txt = input("Enter a string: ")
rev_txt = ''.join(reversed(txt))
print(rev_txt)

//o/p:
Enter a string: Hello world
dlrow olleH


2. Check if a string is a palindrome.

//code:
txt = input("Enter a string: ")
rev_txt = ''.join(reversed(txt))
if txt == rev_txt: 
  print("String is a pallindrome")
else:
  print("String is not a pallindrome")

//o/p:
Enter a string: hello
String is not a pallindrome

Enter a string: malayalam
String is a pallindrome


3. Convert a string to uppercase.

//code:
txt = input("Enter a string: ")
print("string in Uppercase: ",txt.upper())

//o/p:
Enter a string: hello
string in Uppercase:  HELLO


4. Convert a string to lowercase.

//code:
txt = input("Enter a string: ")
print("string in Uppercase: ",txt.lower())

//o/p:
Enter a string: HELLO WORLD
string in Uppercase:  hello world


5. Count the number of vowels in a string.

//code:
txt = input("Enter a string: ")
count=0
vowels = set("aeiouAEIOU")
for char in txt:
  if char in vowels:
    count+=1
print("Count of vowels: ",count)

//o/p:
Enter a string: Hello world
Count of vowels:  3


6. Count the number of consonants in a string.

//code:
txt = input("Enter a string: ")
count=0
vowels = set("aeiouAEIOU")
for char in txt:
  if char not in vowels and char != " ":
    count+=1
print("Count of consonants: ",count)

//o/p:
Enter a string: Hello World
Count of consonants:  7


7. Remove all whitespaces from a string.

METHOD 1:
---------
//code:
txt = input("Enter a string: ")
new_txt = ''.join(txt.split())
print("String after removing the whitespace: ", new_txt)

//o/p:
Enter a string: hello hi how are you
String after removing the whitespace:  hellohihowareyou

METHOD 2:
---------
//code:
txt = input("Enter a string: ")
new_txt = txt.replace(" ","")
print("String after removing the whitespace: ", new_txt)

//o/p:
Enter a string: Hello hi how are you
String after removing the whitespace:  Hellohihowareyou


8. Find the length of a string without using the `len()` function.

//code:
txt = input("Enter a string: ")
count=0
for char in txt:
  if char == " ":
    continue
  count+=1
print("Length of the string: ",count)

//o/p:
Enter a string: Hello world
Length of the string:  10


9. Check if a string contains a specific word.

//code:
txt = input("Enter a string: ")
search = input("Enter the world to search: ")
word = txt.split()
if search in  word:
  print("The word is present in the string")
else:
  print("The word is not present in the string")

//o/p:
Enter a string: hello world
Enter the world to search: hello
The word is present in the string

Enter a string: hello world
Enter the world to search: hi
The word is not present in the string


10. Replace a word in a string with another word.

//code:
txt = input("Enter a string: ")
replace_txt = input("Enter a word to be replaced: ")
new_txt = txt.replace(replace_txt,"Hi")
print("String after replacing: ", new_txt)

//o/p:
Enter a string: Hello world
Enter a word to be replaced: Hello
String after replacing:  Hi world


11. Count the occurrences of a word in a string.

//code:


//o/p:



12. Find the first occurrence of a word in a string.

//code:


//o/p:



13. Find the last occurrence of a word in a string.

//code:


//o/p:



14. Split a string into a list of words.

//code:


//o/p:



15. Join a list of words into a string.

//code:


//o/p:



16. Convert a string where words are separated by spaces to one where words
are separated by underscores.

//code:


//o/p:



17. Check if a string starts with a specific word or phrase.

//code:


//o/p:



18. Check if a string ends with a specific word or phrase.

//code:


//o/p:



19. Convert a string to title case (e.g., "hello world" to "Hello World").

//code:


//o/p:



20. Find the longest word in a string.

//code:


//o/p:



21. Find the shortest word in a string.

//code:


//o/p:


22. Reverse the order of words in a string.

//code:


//o/p:



23. Check if a string is alphanumeric.

//code:


//o/p:



24. Extract all digits from a string.

//code:


//o/p:



25. Extract all alphabets from a string.

//code:


//o/p:






