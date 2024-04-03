#The bubble sort algorithm sort the values from lowest to highest
# The word 'bubble' comes from he algorithm how it works . it bubble up the highest values
# How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

# An array with values to sort.
# An inner loop that goes through the array and swaps values if the first value is higher than the next value. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with n values, this outer loop must run n-1 times.


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
print(my_array)


# If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, and we can stop the algorithm, like this:
my_array = [7, 3, 9, 12, 11]
n=len(my_array)
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
            swapped=True
    if not swapped:
        break
print(my_array)
