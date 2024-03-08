# The assert statement takes a boolean condition as input.
# When the condition is true, nothing happens, and execution proceeds normally.
# If the condition evaluates to false, an optional error message can be provided along with the AssertionError.

a = 4
b = 0
print("The value of a / b is:")
assert b != 0
print(a / b)

# In this example, the program checks whether b is not equal to zero before performing a division operation.
# Since b is zero, the assert statement fails, raising an AssertionError. The program terminates without executing the subsequent print statement1.



a = 4
b = 0
print("The value of a / b is:")
assert b != 0, "Zero Division Error"
print(a / b)

# Here, the assert statement includes an error message.
# If b were zero, the assertion would fail, and an AssertionError with the message “Zero Division Error” would be raised1.

a = "hello"
b = 42
assert isinstance(a, str), "a should be a string"
assert isinstance(b, int), "b should be an integer"
print("Values of a and b:", a, b)

# You can also use assert to check variable types. For instance:


