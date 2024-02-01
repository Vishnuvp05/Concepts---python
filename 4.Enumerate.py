#Enumerate in python is a built inn function that adds a counter to an iterable and returnsvallue in enumerate() it as a enumerate object
fruits=["apple","banana","cherry"]
for index,value in enumerate(fruits):
    print(index,value)

#it has a optional parameter start .The default value for start is 0
letters="abcde"
for i,value in enumerate(letters,start=1):
         print(i,value)