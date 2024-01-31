#map Function
#It is a built in function that allows you to apply a given function to each item in an iterable such as list,Tuple 
#return new iterable with transformed items
#iterable is an object that can be looped using for loop

names=["Adolf","Vishnu"]
upper=map(str.upper,names)
print(list(upper))

#You can also use lambda functions with map() to create anonymous functions on the fly. 
#For example, you can use map() and lambda to square a list of numbers

n=[1,2,3,4,5,]
squared=map(lambda x:x**2,n)
print(list(squared))
    