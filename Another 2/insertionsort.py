""" 
Time Complexity: O(n*2)

Auxiliary Space: O(1)

Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted
in reverse order. And it takes minimum time (Order of n) when elements are 
already sorted.

Algorithmic Paradigm: Incremental Approach

Sorting In Place: Yes

Stable: Yes

Online: Yes

Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

What is Binary Insertion Sort?
We can use binary search to reduce the number of comparisons in normal insertion 
sort. Binary Insertion Sort uses binary search to find the proper location to 
insert the selected item at each iteration. In normal insertion, sorting takes 
O(i) (at ith iteration) in worst case. We can reduce it to O(logi) by using 
binary search. The algorithm, as a whole, still has a running worst case running 
time of O(n2) because of the series of swaps required for each insertion. Refer 
this for implementation. 
"""

def insertionsort(arr):
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key   
        
size = input("Enter size of the array : ")
arr = list()

print("Enter elements of array : ")
for i in range(int(size)):
    c = input()
    arr.append(c)

print("Entered array is : ")
print(arr)

insertionsort(arr)

print("Sorted array is : ")
print(arr)            
        
            
            
