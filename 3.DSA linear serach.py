#initil providing value for pos as -1
pos=-1
#defining a search function uing list and n attributes 
def search(list,n):
    #using for loop to find the element we can alo use for loop
    for i in range (len(list)):
        if list[i]==n:
            #using globals()['pos'] to edit the global variable by changing the local variable and storing i in the pos 
            globals()['pos']=i
            return True 
     # return true if present else Fase        return True 
    return False
#create a list named list
list=[1,2,3,4,5,6,7]
#element we want to search is stored in a variable n
n=2
#using if else if preent print found and the position else prints not found
if search(list,n):
    print("Found",pos)
else:
    print("Not Found")

#output will be Found 1
 
