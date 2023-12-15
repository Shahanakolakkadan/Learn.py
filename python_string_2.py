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
txt = input("Enter a string: ")
search = input("Enter the word need to check: ")
words = txt.split()
count=0
for word in words:
  if word.lower() == search:
    count+=1
print("Count of occurence of the word: ",count)

//o/p:
Enter a string: Hello hi hello hi hello how are you
Enter the word need to check: hello
Count of occurence of the word:  3


12. Find the first occurrence of a word in a string.

//code:
txt = input("Enter a string: ")
word = input("Enter the word to be check: ")
index = txt.find(word)
if index != -1:
  print(f"The first occurence of the word '{word}'is at: '{index}' ")

//o/p:
Enter a string: Hello world Hello world
Enter the word to be check: Hello
The first occurence of the word 'Hello'is at: '0' 


13. Find the last occurrence of a word in a string.

//code:
txt = input("Enter a string: ")
word = input("Enter the word to be check: ")
index = txt.rfind(word)
if index != -1:
  print(f"The first occurence of the word '{word}'is at: '{index}' ")

//o/p:
output
Enter a string: Hello world Hello world
Enter the word to be check: Hello
The first occurence of the word 'Hello'is at: '12'


14. Split a string into a list of words.

//code:
txt = input("Enter a string: ")
ls = []
words = txt.split()
for word in words: 
  ls.append(word)
print(ls)

//o/p:
Enter a string: hello hi world
['hello', 'hi', 'world']


15. Join a list of words into a string.

//code:
ls = ["hello","hi","world"]
print("list: ",ls)
for x in ls: 
  st = ''.join(ls)
print("after joining: ", st)

//o/p:
list:  ['hello', 'hi', 'world']
after joining: hellohiworld


16. Convert a string where words are separated by spaces to one where words
are separated by underscores.

//code:
txt = input("Enter a string: ")
new_txt = txt.replace(" ","_")
print("String after replacing with underscore: ", new_txt)

//o/p:
Enter a string: Hello world
String after replacing with underscore:  Hello_world


17. Check if a string starts with a specific word or phrase.

//code:
txt = input("Enter a string: ")
word = input("Enter the word to be check: ")

if txt.startswith(word):
    print(f"The string starts with '{word}'")
else:
    print(f"The string does not start with '{word}'")

//o/p:
Enter a string: Hello world
Enter the word to be check: Hello
The string starts with 'Hello'

Enter a string: Hello world
Enter the word to be check: world
The string does not start with 'world'


18. Check if a string ends with a specific word or phrase.

//code:
txt = input("Enter a string: ")
word = input("Enter the word to be check: ")

if txt.endswith(word):
    print(f"The string ends with '{word}'")
else:
    print(f"The string does not end with '{word}'")

//o/p:
Enter a string: Hello world
Enter the word to be check: world
The string ends with 'world'

Enter a string: Hello world
Enter the word to be check: Hello
The string does not end with 'Hello'


19. Convert a string to title case (e.g., "hello world" to "Hello World").

//code:
txt = input("Enter a string: ")
print("string in Ttilecase: ",txt.title())

//o/p:
Enter a string: hello world
string in Ttilecase:  Hello World


20. Find the longest word in a string.

//code:
txt = input("Enter a string: ")
words = txt.split()
long_word = ""
for word in words:
  if len(word) > len(long_word):
    long_word = word
print("Longest word: ",long_word)

//o/p:
Enter a string: Hello i am python
Longest word:  python


21. Find the shortest word in a string.

//code:
txt = input("Enter a string: ")
words = txt.split()
short_word = min(words, key=len)
print("Shortest word: ",short_word)

//o/p:
Enter a string: Hello I am python
Shortest word:  I

22. Reverse the order of words in a string.

//code:
txt = input("Enter a string: ")
words = txt.split()
rev_words = words[::-1]
rev_txt = ' '.join(rev_words)
print("String in reversed order: ", rev_txt)

//o/p:
Enter a string: Hello world
String in reversed order:  world Hello


23. Check if a string is alphanumeric.

//code:
txt = input("Enter a string: ")
if txt.isalnum():
    print("The string is Alphanumeric")
else:
    print("The string is not Alphanumeric")

//o/p:
Enter a string: Hello123
The string is Alphanumeric

Enter a string: Hello@world
The string is not Alphanumeric


24. Extract all digits from a string.

//code:
txt = input("Enter a string: ")
digit = ""
for char in txt:
  if char.isdigit():
    digit += char
print("Digits in the string: ",digit)

//o/p:
Enter a string: 123Hello456World678
Digits in the string:  123456678


25. Extract all alphabets from a string.

//code:
txt = input("Enter a string: ")
alpha = ""
for char in txt:
  if char.isalpha():
    alpha += char
print("Digits in the string: ",alpha)

//o/p:
Enter a string: 123Hello456World789
Digits in the string:  HelloWorld





