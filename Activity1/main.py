print("1.Bubble Sort Ascending order")
arr1 = [12, 78, 91, 34, 62]
print("Before Bubble Sort")
print(arr1)
for i in range(len(arr1)):
    for j in range(0, len(arr1) - i - 1):
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
print("After Bubble Sort")
print(arr1)
print()
print("2.Insertion Sort Ascending order")
arr2=[12, 78, 91, 34, 62]
print("Before")
print(arr2)
for i in range(1, len(arr2)):
    key = arr2[i]
    j = i - 1
    while j >= 0 and key > arr2[j]:
        arr2[j + 1] = arr2[j]
        j -= 1
    arr2[j + 1] = key
print("After")
print(arr2)
print()
print("3.Selection Sort Descending Order")
print("Before")
arr3=[5, 99, 48, 15, 67]
print(arr2)
for i in range(len(arr3)):
    min_idx = i
    for j in range(i + 1, len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
print("After")
print(arr3)
print()
print("4.Insertion Sort Descending order")
arr4 = [38, 82, 25, 74, 13]
print("Before")
print(arr4)
for i in range(1, len(arr4)):
    key = arr4[i]
    j = i - 1
    while j >= 0 and key > arr4[j]:
        arr4[j + 1] = arr4[j]
        j -= 1
    arr4[j + 1] = key
print("After")
print(arr4)
print()
print("5.Copying values of the second and third index")
print("Second and third index are:",[62,78,62,34,48,15,38,25])
arr5 = [62,78,62,34,48,15,38,25]
print("Ascending Order")
for i in range(1, len(arr4)):
    key = arr5[i]
    j = i - 1
    while j >= 0 and key < arr5[j]:
        arr5[j + 1] = arr5[j]
        j -= 1
    arr5[j + 1] = key
print (arr5)
print("Descending Order")
for i in range(1, len(arr4)):
    key = arr5[i]
    j = i - 1
    while j >= 0 and key > arr5[j]:
        arr5[j + 1] = arr5[j]
        j -= 1
    arr5[j + 1] = key
print(arr5)
print()
print("6.Creating a new list of arrays copying all values from items 1-4")
print("Implementing Selection Sort in Ascending Order")
arr6=[23,89, 7, 56, 44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
print("Before")
print(arr6)
for i in range(len(arr6)):
    min_idx = i
    for j in range(i + 1, len(arr6)):
        if arr6[min_idx] > arr6[j]:
         min_idx = j
    arr6[i], arr6[min_idx] = arr6[min_idx], arr6[i]
print("After")
print(arr6)
print()
print("7.Odd and Even")
arr7=[23,89, 7, 56, 44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
print(arr7)
evenNum=[num for num in arr7 if num % 2==0]
oddNum=[num for num in arr7 if num % 2 != 0]
print("Even Numbers: ", evenNum)
print("Odd Numbers: ",oddNum)