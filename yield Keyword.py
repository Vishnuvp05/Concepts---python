# yield keyword

# Definition and Purpose:
# The yield keyword is used to create a generator function.
# A generator function is a type of function that is memory-efficient and can be used like an iterator object.
# When you use yield, it turns any expression associated with it into a generator object and returns it to the caller.
# Unlike a regular function that uses return, a generator function doesn’t execute all at once. Instead, it pauses its execution and resumes when needed.

# Difference Between return and yield:
# return:
# Terminates the execution of the function.
# Returns a value directly.
# yield:
# Only pauses the execution of the function.
# Returns a generator object.
# Execution res

# Advantages of yield:
# Memory Efficiency:
# Execution happens only when the caller iterates over the generator object.
# Variables’ states are saved, allowing pausing and resuming from the same point.
# Disadvantages of yield:
# Code flow can be complex due to multiple value returns.
# Proper handling of generator function calls is essential to avoid errors.


#Examples: a. Generator Functions and yield:

def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"

obj = fun_generator()
print(type(obj))  # Output: <class 'generator'>
print(next(obj))  # Output: Hello world!!
print(next(obj))  # Output: Geeksforgeeks


#Generating an Infinite Sequence:

def inf_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in inf_sequence():
    print(i, end=" ")
# Output: 0 1 2 3 4 5 6 7 8 ... (infinite sequence)

#Note: The num += 1 is executed after yield, unlike a return statement.