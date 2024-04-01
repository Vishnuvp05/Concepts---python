#Binary search needs the array to be sorted 
#only in the sorted array can be able to do binary search
#The binary search creates two variable one is left takes initial index value and right takkes last index value 
#takes the middle element of the array if it is the rquires returns the value 
#if the values is greater than the middle value it searches the right side of the mid by incrementing the left to mid+1
#if the value is smaller then the mid value it searches the left side by decrementing the right to mid-1
#searching continues until the required value found or the area becomes empty

def binaryseach(arr,targetval):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==targetval:
            return mid
        if targetval>arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[1,2,3,4,5,6,7,8]
targetval = 7
result=binaryseach(arr,targetval)
print(result)
