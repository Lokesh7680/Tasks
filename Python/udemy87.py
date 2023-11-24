'''Do all of this in a .py file in Pycharm.

Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]

Access the first list from the list of lists in step 1 by index then print it.

Access the 14 from the list in step 1 then print it.

Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]

Use a negative integer to access "chair" from the variable in step 4 by index then print it.

Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.

Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]

Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.

Print the slice [8.76, 6.54] from the variable you created in step 7.

Print the slice [0.98, 8.76] from the variable you created in step 7.'''

a=[[0,2],[4,6],[8,10],[12,14]]

print(a[0])

print(a[3][1])

string=["chair","table","desk","lamp","bed"]

print(string[-5])

print("chair" in string)

#Print "Most people own at least 2 chairs." by concatenating the 2 fr
# om the list in step 1 and the "chair" 
# from the list in step 4 with "Most people own at least ", a space, and a period.

print("Most people own at least " + str(a[0][1]) + string[-5])

floatt = [0.98, 8.76, 6.54, 4.32]

print(floatt[1:])

print(floatt[1:3])

print(floatt[0:2])