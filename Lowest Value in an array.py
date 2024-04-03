my_array=[2,3,4,5,6,78,1,2,3,0]
low_value=my_array[0]
for i in my_array:
    if i < low_value:
        low_value=i
print(low_value)