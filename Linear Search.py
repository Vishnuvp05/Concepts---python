#Go through the array value by value from start 
# if the desired value found return the index of the array 
#else return -1

def linearSearch(arr,targetval):
    for i in range(len(arr)):
        if arr[i]==targetval:
            return i
    return -1
arr=[1,9,4,5,6,7,4]
targetval=11
result=linearSearch(arr,targetval)
print(result)
