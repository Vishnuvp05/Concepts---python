n = 1000_000_000
print(n) #prints 1000000000 "_" will be ingoored by interpreter

n=1000000000
print(f"{n:_}") #1_000_000_000 "_" used as thousand seperator 
print(f"{n:,}") #1,000,000,000 "," used as thousand seperator 

#alining a variable 

a="vishnu"
print(f"{a:<20}:") #vishnu              :
print(f"{a:>20}:") #              vishnu:
print(f"{a:^20}:") #       vishnu       :
print(f"{a:$<20}:") #vishnu$$$$$$$$$$$$$$:
print(f"{a:_>20}")  #______________vishnu
print(f"{a:*^20}")  #*******vishnu*******

#date and time 

from datetime import datetime
now = datetime.now()
print(f"{now:%d.%m.%y (%H.%M.%S)}") #22.02.24 (17.29.33)
print(f"{now:%c}") #Thu Feb 22 17:31:23 2024
print(f"{now:%I.%p}") #05.PM


#float
j=1234.5678
print(j) #1234.5678
print(round(j,2)) #1234.57
print(f"{j:.2f}") #1234.57
print(f"{j:.0f}") #1235
print(f"{j:,.3f}") #1,234.568 in addition to thousand seperator


#debug using f string
a=10
b=20
var="hi bruh" 
print(f"{a + b = }") #a + b = 30
print(f"{bool(a)}") #true 
print(f"{var = }") #var = 'hi bruh'