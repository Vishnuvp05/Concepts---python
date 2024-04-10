# Merge Sort
# The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

# Divide: The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of one element.

# Conquer: The algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.

# The breaking down and building up of the array to sort the array is done recursively.

# In the animation above, each time the bars are pushed down represents a recursive call, splitting the array into smaller pieces. When the bars are lifted up, it means that two sub-arrays have been merged together.

# The Merge Sort algorithm can be described like this:

# How it works:

# Divide the unsorted array into two sub-arrays, half the size of the original.
# Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
# Merge two sub-arrays together by always putting the lowest value first.
# Keep merging until there are no sub-arrays left.

# Merge Sort Implementation
# To implement the Merge Sort algorithm we need:

# An array with values that needs to be sorted.
# A function that takes an array, splits it in two, and calls itself with each half of that array so that the arrays are split again and again recursively, until a sub-array only consist of one value.
# Another function that merges the sub-arrays back together in a sorted way.


def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]

    leftsorted=mergesort(lefthalf)
    rightsorted=mergesort(righthalf)

    return merge(leftsorted,rightsorted)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergesort(unsortedArr)
print("Sorted array:", sortedArr)




