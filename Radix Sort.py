# Radix Sort
# The Radix Sort algorithm sorts an array by individual digits, starting with the least significant digit (the rightmost one).

# The radix (or base) is the number of unique digits in a number system. In the decimal system we normally use, there are 10 different digits from 0 till 9.

# Radix Sort uses the radix so that decimal values are put into 10 different buckets (or containers) corresponding to the digit that is in focus, then put back into the array before moving on to the next digit.

# Radix Sort is a non comparative algorithm that only works with non negative integers.

# The Radix Sort algorithm can be described like this:

# How it works:

# Start with the least significant digit (rightmost digit).
# Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
# Move to the next digit, and sort again, like in the step above, until there are no digits left.


# Stable Sorting
# Radix Sort must sort the elements in a stable way for the result to be sorted correctly.

# A stable sorting algorithm is an algorithm that keeps the order of elements with the same value before and after the sorting. Let's say we have two elements "K" and "L", where "K" comes before "L", and they both have value "3". A sorting algorithm is considered stable if element "K" still comes before "L" after the array is sorted.

# It makes little sense to talk about stable sorting algorithms for the previous algorithms we have looked at individually, because the result would be same if they are stable or not. But it is important for Radix Sort that the the sorting is done in a stable way because the elements are sorted by just one digit at a time.

# So after sorting the elements on the least significant digit and moving to the next digit, it is important to not destroy the sorting work that has already been done on the previous digit position, and that is why we need to take care that Radix Sort does the sorting on each digit position in a stable way.

# In the simulation below it is revealed how the underlying sorting into buckets is done. And to get a better understanding of how stable sorting works, you can also choose to sort in an unstable way, that will lead to an incorrect result. The sorting is made unstable by simply putting elements into buckets from the end of the array instead of from the start of the array.

# Radix Sort Implementation
# To implement the Radix Sort algorithm we need:

# An array with non negative integers that needs to be sorted.
# A two dimensional array with index 0 to 9 to hold values with the current radix in focus.
# A loop that takes values from the unsorted array and places them in the correct position in the two dimensional radix array.
# A loop that puts values back into the initial array from the radix array.
# An outer loop that runs as many times as there are digits in the highest value.



my_array=[1703737,493,2938,3093,30387,377]
radixArray=[[],[],[],[],[],[],[],[],[],[]]
maxi=max(my_array)
exp=1

while (maxi//exp)>0:
    while len(my_array)>0:
        val=my_array.pop()
        radixIndex=(val//exp)%10
        radixArray[radixIndex].append(val)
    for i in radixArray:
        while len(i)>0:

            val=i.pop()
            my_array.append(val)
    exp*=10


print(my_array)