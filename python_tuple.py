TOPIC: Tuple Based Practice Problem :
-------------------------------------

1. Create a tuple with integers from 1 to 5.

//code:
tp = tuple(range(1,6))
print("Tuple with integer from 1 to 5: ",tp)

//o/p:
Tuple with integer from 1 to 5:  (1, 2, 3, 4, 5)


2. Access the third element of a tuple.

//code:
tp = (2,5,6,9,1,4,0)
print("Tuple: ",tp)
print("Third element of the tuple: ",tp[2])

//o/p:
Tuple:  (2, 5, 6, 9, 1, 4, 0)
Third element of the tuple:  6


3. Find the length of a tuple without using the `len()` function.

//code:
tp = (2,5,6,9,1,4,0)
print("Tuple: ",tp)
count = 0
for i in tp:
  count+=1
print("Total element of the tuple: ",count)

//o/p:
Tuple:  (2, 5, 6, 9, 1, 4, 0)
Total element of the tuple:  7


4. Count the occurrences of an element in a tuple.

//code:
tp = (2,5,6,3,3,1,2,8,1,3,9,5)
print("Tuple: ",tp)
element = int(input("Enter the element need to check: "))
occurence = tp.count(element)
print("Count of occurence of '{element}': ",occurence)

//o/p:
Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)
Enter the element need to check: 9
Count of occurence of '{element}':  1


5. Find the index of the first occurrence of an element in a tuple.

//code:
tp = (2,5,6,3,3,1,2,8,1,3,9,5)
print("Tuple: ",tp)
element = int(input("Enter the element need to check: "))
occurence = tp.index(element)
print("first occurence of '{element}': ",occurence)

//o/p:
Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)
Enter the element need to check: 2
first occurence of '{element}':  0


6. Check if an element exists in a tuple.

//code:
tp = (2,5,6,3,3,1,2,8,1,3,9,5)
print("Tuple: ",tp)
element = int(input("Enter the element need to search: "))
if element in tp:
  print(f"the {element} is present in the tuple")
else:
  print(f"the {element} is not present in the tuple")

//o/p:
Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)
Enter the element need to search: 4
the 4 is not present in the tuple

Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)
Enter the element need to search: 1
the 1 is present in the tuple


7. Convert a tuple to a list.

//code:
METHOD:1
--------
tp = (2,5,6,3,3,1,2,8,1,3,9,5)
print("Tuple: ",tp)
ls = []
for i in tp:
  ls.append(i)
print("List: ",ls)

METHOD:2
--------
tp = (2,5,6,3,3,1,2,8,1,3,9,5)
print("Tuple: ",tp)
ls = list(tp)
print("List: ",ls)

//o/p:
Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)
List:  [2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5]


8. Convert a list to a tuple.

//code:
ls = [2,5,6,3,3,1,2,8,1,3,9,5]
print("List: ",ls)
tp = tuple(ls)
print("Tuple: ",tp)

//o/p:
List:  [2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5]
Tuple:  (2, 5, 6, 3, 3, 1, 2, 8, 1, 3, 9, 5)


9. Unpack the elements of a tuple into variables.

//code:
tp = (2,5,6)
print("Tuple: ",tp)
var1, var2, var3 = tp
print("Unpacked variables:", var1, var2, var3)

//o/p:
Tuple:  (2, 5, 6)
Unpacked variables: 2 5 6


10. Create a tuple of even numbers from 1 to 10.

//code:
tp = tuple(range(2,11,2))
print("Tuple with even numbers from 1 to 10: ",tp)

//o/p:
Tuple with even numbers from 1 to 10:  (2, 4, 6, 8, 10)


11. Create a tuple of odd numbers from 1 to 10.

//code:
tp = tuple(range(1,10,2))
print("Tuple with odd numbers from 1 to 10: ",tp)

//o/p:
Tuple with odd numbers from 1 to 10:  (1, 3, 5, 7, 9)


12. Concatenate two tuples.

//code:
tp1 = (2,5,6,3,3,0)
tp2 =(1,2,8,1,3,9,5)
newtp = tp1+tp2
print("Tuple1: ",tp1)
print("Tuple2: ",tp2)
print("New tuple: ",newtp)

//o/p:
Tuple1:  (2, 5, 6, 3, 3, 0)
Tuple2:  (1, 2, 8, 1, 3, 9, 5)
New tuple:  (2, 5, 6, 3, 3, 0, 1, 2, 8, 1, 3, 9, 5)


13. Repeat a tuple three times.

//code:
tp = (2,5,6,3,3,0)
print("Tuple: ",tp)
newtp = tp * 3
print("New tuple: ",newtp)

//o/p:
Tuple:  (2, 5, 6, 3, 3, 0)
New tuple:  (2, 5, 6, 3, 3, 0, 2, 5, 6, 3, 3, 0, 2, 5, 6, 3, 3, 0)


14. Check if a tuple is empty.

//code:
tp = ()
if not tp:
  print("Tuple is empty")
else:
  print("Tuple is not empty")

//o/p:
Tuple is empty


15. Create a nested tuple.

//code:
tp = ("a","b","c",(1,2,3),("ant","arrow"))
print("Tuple: ",tp)

//o/p:
Tuple:  ('a', 'b', 'c', (1, 2, 3), ('ant', 'arrow'))


16. Access the first element of a nested tuple.

//code:
tp = ("a","b","c",(1,2,3),("ant","arrow"))
first = tp[0]
print("First element: ",first)

//o/p:
First element:  a


17. Create a tuple with a single element.

//code:
tp = (1)
print("Tuple: ",tp)

//o/p:
Tuple:  1


18. Compare two tuples.

//code:
tp1 = (1,2,3,4,5)
tp2 = (2,4,6,8,4)
if tp1 == tp2:
  print("The two tuples are equal")
elif tp1 != tp2:
  print("The two tuples are not equal")

//o/p:
The two tuples are not equal


19. Delete a tuple.

//code:
tp = (2,5,6,3,3)
print("Tuple: ",tp)
del tp
try:
    print("Deleted Tuple:", tp)
except NameError as e:
    print(f"NameError: {e}")

//o/p:
Tuple:  (2, 5, 6, 3, 3)
NameError: name 'tp' is not defined


20. Slice a tuple.

//code:
tp = (2,5,6,3,3)
print("Tuple: ",tp)
newtp = tp[2:]
print("Sub tuple: ",newtp)

//o/p:
Tuple:  (2, 5, 6, 3, 3)
Sub tuple:  (6, 3, 3)


22. Find the minimum value in a tuple.

//code:
tp = (2,5,6,3,9)
print("Tuple: ",tp)
min_value = min(tp)
print("Minimum value: ",min_value)

//o/p:
Tuple:  (2, 5, 6, 3, 9)
Minimum value:  2


23. Convert a string to a tuple of characters.

//code:
st = "Hello How are you?"
words = st.split()
tp = tuple(words)
print("Tuple: ",tp)

//o/p:
Tuple:  ('Hello', 'How', 'are', 'you?')


24. Convert a tuple of characters to a string.

//code:
tp =  ('Hello', 'How', 'are', 'you?')
st = ' '.join(tp)
print("String: ",st)

//o/p:
String:  Hello How are you?


25. Create a tuple from multiple data types.

//code:
tp = (1, 'hello', 3.14, True, [5, 6, 7])
print("Mixed Data Type Tuple:", tp)

//o/p:
Mixed Data Type Tuple: (1, 'hello', 3.14, True, [5, 6, 7])



