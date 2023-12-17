Topic: List Based Practice Problem :
------------------------------------

1. Create a list with integers from 1 to 10.

//code:
ls = []
for i in range(1,11):
  ls.append(i)
print(ls)

//o/p:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


2. Find the length of a list without using the `len()` function.

//code:
ls = ["apple", "grapes","mango","banana"]
count = 0
for i in ls:
  count+=1
print("Length of list: ",count)

//o/p:
Length of list:  4


3. Append an element to the end of a list.

//code:
ls = ["apple", "grapes","mango","banana"]
print("list: ", ls)
ls.append("pineapple")
print("List after appending: ",ls)

//o/p:
ist:  ['apple', 'grapes', 'mango', 'banana']
List after appending:  ['apple', 'grapes', 'mango', 'banana', 'pineapple']


4. Insert an element at a specific index in a list.

//code:
ls = ["apple", "grapes","mango","banana"]
print("list: ", ls)
ls.insert(2,"pineapple")
print("List after appending: ",ls)

//o/p:
list:  ['apple', 'grapes', 'mango', 'banana']
List after appending:  ['apple', 'grapes', 'pineapple', 'mango', 'banana']


5. Remove an element from a list by its value.

//code:
ls = ["apple", "grapes","mango","banana"]
print("list: ", ls)
ls.remove("grapes")
print("List after appending: ",ls)

//o/p:
list:  ['apple', 'grapes', 'mango', 'banana']
List after appending:  ['apple', 'mango', 'banana']


6. Remove an element from a list by its index.

//code:
ls = ["apple", "grapes","mango","banana"]
print("list: ", ls)
ls.pop(2)
print("List after appending: ",ls)

//o/p:
list:  ['apple', 'grapes', 'mango', 'banana']
List after appending:  ['apple', 'grapes', 'banana']


7. Check if an element exists in a list.

//code:
ls = ["apple", "grapes","mango","banana"]
search = input("Enter the element to search: ")
if search in ls :
  print("Element is present in the list")
else: 
  print("Element is not present in the list")

//o/p:
Enter the element to search: mango
Element is present in the list

Enter the element to search: pineapple
Element is not present in the list


8. Find the index of the first occurrence of an element in a list.

//code:
METHOD:1
--------
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
element = int(input("Enter the element need to check: "))
for i in ls:
  if i == element:
    print(f"first occurence of the '{element}': ",ls.index(i))
    break;
 
METHOD:2
--------   
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
element = int(input("Enter the element need to check: "))
occurence = ls.index(element)
print(f"first occurence of the '{element}': ",occurence)

//o/p:
List:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
Enter the element need to check: 1
first occurrence of the '1':  7


9. Count the occurrences of an element in a list.

//code:
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
element = int(input("Enter the element need to check: "))
occurence = ls.count(element)
print("Count of occurrence of '{element}': ",occurence)

//o/p:
List:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
Enter the element need to check: 2
Count of occurrence of '{element}':  3


10. Reverse the order of elements in a list.

//code:
ls = [6,9,2,1,4,3,8,5]
print("List: ",ls)
rev_ls = ls[::-1]
print("List in reverse order: ",rev_ls)

//o/p:
List:  [6, 9, 2, 1, 4, 3, 8, 5]
List in reverse order:  [5, 8, 3, 4, 1, 2, 9, 6]


11. Sort a list in ascending order.

//code:
METHOD:1
--------
ls = [6,9,2,1,4,3,8,5]
print("List: ",ls)
asc_ls = sorted(ls)
print("List in ascending order: ",asc_ls)

METHOD:2
--------
ls = [6,9,2,1,4,3,8,5]
print("List: ",ls)
ls.sort()
print("List in ascending order: ",ls)

//o/p:
List:  [6, 9, 2, 1, 4, 3, 8, 5]
List in ascending order:  [1, 2, 3, 4, 5, 6, 8, 9]


12. Sort a list in descending order.

//code:
METHOD:1
--------
ls = ["apple", "grapes","mango","banana"]
print("List: ",ls)
desc_ls = sorted(ls,reverse=True)
print("List in descending order: ",desc_ls)

METHOD:2
--------
ls = ["apple", "grapes","mango","banana"]
print("List: ",ls)
ls.sort(reverse=True)
print("List in descending order: ",ls)

//o/p:
List:  ['apple', 'grapes', 'mango', 'banana']
List in ascending order:  ['mango', 'grapes', 'banana', 'apple']


13. Create a list of even numbers from 1 to 20.

//code:
ls = []
print("List of even number from 1 to 20: ")
for i in range(2,21,2):
  ls.append(i)
print(ls)

//o/p:
List of even number from 1 to 20: 
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


14. Create a list of odd numbers from 1 to 20.

//code:
ls = []
print("List of odd number from 1 to 20: ")
for i in range(1,20,2):
  ls.append(i)
print(ls)

//o/p:
List of odd number from 1 to 20: 
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


15. Find the sum of all elements in a list.

//code:
ls = [2,3,5,7,8,1,9,1]
print("List: ",ls)
sum = 0 
for i in ls:
  sum+=i
print("Sum: ",sum)

//o/p:
List:  [2, 3, 5, 7, 8, 1, 9, 1]
Sum:  36


16. Find the maximum value in a list.

//code:
ls = [2,3,5,7,8,1,9,1]
print("List: ",ls)
value = max(ls)
print("Maximum value: ",value)

//o/p:
List:  [2, 3, 5, 7, 8, 1, 9, 1]
Maximum value:  9


17. Find the minimum value in a list.

//code:
ls = [2,3,5,7,8,1,9,1]
print("List: ",ls)
value = min(ls)
print("Minimum value: ",value)

//o/p:
List:  [2, 3, 5, 7, 8, 1, 9, 1]
Minimum value:  1


18. Create a list of squares of numbers from 1 to 10.

//code:
ls = []
print("List of square of number from 1 to 10: ")
for i in range(1,11):
  ls.append(i*i)
print(ls)

//o/p:
List of square of number from 1 to 10: 
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


19. Create a list of random numbers.

//code:
import random
ls = []
print("List of randum numbers: ")
for i in range(5):
  num = random.randint(1,100)
  ls.append(num)
print(ls)

//o/p:
List of randum numbers: 
[74, 100, 69, 11, 19]


20. Remove duplicates from a list.

//code:
METHOD:1:
---------
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
newls = []
for i in ls:
  if i not in newls:
    newls.append(i)
print("List after removing the dublicates: ",newls)

METHOD:2:
---------
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
newls = list(set(ls))
print("List after removing the dublicates: ",newls)

//o/p:
List:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
List after removing the dublicates:  [2, 3, 5, 7, 8, 1, 9]


21. Find the common elements between two lists.

//code:
ls1 = [2,3,5,7,2,3,8,1,9,1,7,9,2]
ls2 = [1,2,4,6,9,0,3,11,34]
newls = list(set(ls1).intersection(ls2))
print("List1: ",ls1)
print("List2: ",ls2)
print("Common elements: ",newls)

//o/p:
List1:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
List2:  [1, 2, 4, 6, 9, 0, 3, 11, 34]
Common elements:  [1, 2, 3, 9]


22. Find the difference between two lists.

//code:
ls1 = [2,3,5,7,2,3,8,1,9,1,7,9,2]
ls2 = [1,2,4,6,9,0,3,11,34]
newls = list(set(ls1).difference(ls2))
print("List1: ",ls1)
print("List2: ",ls2)
print("different elements: ",newls)

//o/p:
List1:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
List2:  [1, 2, 4, 6, 9, 0, 3, 11, 34]
different elements:  [5, 7, 8]


23. Merge two lists.

//code:
ls1 = [2,3,5,7,2,3,8,1,9,1,7,9,2]
ls2 = [1,2,4,6,9,0,3,11,34]
newls = ls1 + ls2
print("List1: ",ls1)
print("List2: ",ls2)
print("merge list: ",newls)

//o/p:
List1:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
List2:  [1, 2, 4, 6, 9, 0, 3, 11, 34]
merge list:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2, 1, 2, 4, 6, 9, 0, 3, 11, 34]


24. Multiply all elements in a list by 2.

//code:
ls = [2,3,5,7,8,1,9,1]
print("List: ",ls)
print("List multiplied by 2: ")
for i in ls:
  print(i*2)

//o/p:
List:  [2, 3, 5, 7, 8, 1, 9, 1]
List multiplied by 2: 
4
6
10
14
16
2
18
2


25. Filter out all even numbers from a list.

//code:
ls = [2,3,5,7,2,3,8,1,9,1,7,9,2]
print("List: ",ls)
newls = []
for i in ls:
  if i%2 != 0:
    newls.append(i)
print("List after removing even numbers: ",newls)

//o/p:
List:  [2, 3, 5, 7, 2, 3, 8, 1, 9, 1, 7, 9, 2]
List after removing even numbers:  [3, 5, 7, 3, 1, 9, 1, 7, 9]



