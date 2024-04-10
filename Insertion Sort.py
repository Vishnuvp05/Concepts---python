# The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values that are not sorted yet.

# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.
# How it works:

# Take the first value from the unsorted part of the array.
# Move the value into the correct place in the sorted part of the array.
# Go through the unsorted part of the array again as many times as there are values

# Insertion Sort Implementation
# To implement the Insertion Sort algorithm in a programming language, we need:

# An array with values to sort.
# An outer loop that picks a value to be sorted. For an array with 
# n
#  values, this outer loop skips the first value, and must run n-1
#  times.
# An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index 
# i, the sorted part of the array starts at index 0 and ends at index i-1

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array)
for i in range(1,n):
    insert_index=i
    current_value=my_array.pop(i)
    for j in range(1,-1,-1):
        if my_array[j]>current_value:
            insert_index=j
    my_array.insert(insert_index,current_value)

print(my_array)


# # The problem with this way of programming it is that when removing a value from the array, all elements above must be shifted one index place down:
# We can avoid most of these shift operations by only shifting the values necessary

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array)
for i in range(1,n):
    insert_index=i
    current_value=my_array[i]
    for j in range(i-1,-1,-1):
        if my_array[j]>current_value:
            my_array[j+1]=my_array[j]
            insert_index=j
        else:
            break
    my_array[insert_index]=current_value
print(my_array)

#In insertion sort we take one part of the array as sorted and another part as unsorted 
#we compare the fisrt value of unsorted with last value of sorted and if the unsorted s greater tha sorted does nothing if the unosrted is lesser than the sorted 
#we swap the values and moves towards the left side


arr=[2,3,5,1,4,5,32]
for i in range(1,len(arr)):
    j=i
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j+1]=arr[j],arr[j-1]
        j-=1
print(arr)





