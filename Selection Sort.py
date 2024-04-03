# The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
# The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.
# How it works:

# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array.

# An array with values to sort.
# An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with 
# n
#  values, this outer loop must run n-1 times


my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n=len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index=j
    min_value=my_array.pop(min_index)
    my_array.insert(i,min_value)

print(my_array)



# lowest value element is removed, and then inserted in front of the array
# shifting operation takes a lot of time
# Instead of all the shifting, swap the lowest value  with the first value 

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index=j
    my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
print(my_array)

