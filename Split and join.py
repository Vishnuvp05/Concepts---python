n="Vishnu"
a=list(n) #['V', 'i', 's', 'h', 'n', 'u']
b=".".join(a)  #V.i.s.h.n.u
print(b)  


#Splitting a string into words using a space as the separator:
txt = "welcome to the jungle"
words = txt.split()
print(words)
# Output: ['welcome', 'to', 'the', 'jungle']

#Using a comma followed by a space as the separator:
txt = "hello, my name is Peter, I am 26 years old"
info = txt.split(", ")
print(info)
# Output: ['hello', 'my name is Peter', 'I am 26 years old']

#Splitting a string into a list with a maximum of 2 items:
txt = "apple#banana#cherry#orange"
fruits = txt.split("#", 1)
print(fruits)
# Output: ['apple', 'banana#cherry#orange']

