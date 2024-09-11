def selectionSort(arr):
   n = len(arr)
   for i in range(n):
       lowestIndex = i
       for j in range(n):
           if arr[j] < arr[lowestIndex]:
               lowestIndex = j


       print("lowest index ", lowestIndex) # what index contains the lowest value?
       print("i ", i) # where in the array should the ith smallest value be?
       print("n ", n) # where are we considering the end of the array?


       print("before ", arr) # what is array state before we swap anything?
       arr[lowestIndex] = arr[i]
       print("first ", arr) # what is array state after the first write?
       arr[i] = arr[lowestIndex]
       print("final", arr) # what is array state after the second write?
       n = n - 1


   return arr

arr_in = [5, 3, 2, 1, 8, 10, 11, 9, 23]

arr_out = selectionSort(arr_in)

print(arr_out)
