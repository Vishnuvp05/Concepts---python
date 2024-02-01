class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size
    
    def __hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash + ord(letter)*23)%len(self.data_map)
        return my_hash
    #to print table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":",val)
    
    #to set items    
    def set_items(self,key,value):
        #assigning the adrress using key 
        index=self.__hash(key)
        #creating a list in that address if none 
        if self.data_map[index]==None:
            self.data_map[index]=[]
            #appendind data at  the address if list is created already
        self.data_map[index].append([key,value])

    def get_item(self,key):
        #assign address to th key
        index=self.__hash(key)
        #if the data at key is not None
        if self.data_map[index] is not None:
            #taking all the values in the address
            for i in range(len(self.data_map[index])):
                #if i,0 to check all first values if fisrt value is key then return second value that is value 
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        #if no data  return None
        return None
    
#to get the keys
    def keys(self):
     #creating a list named all_keys to store the keys
     all_keys=[]
     #to take all datas
     for i in range(len(self.data_map)):
        #if the data is None return none
        if self.data_map[i] is not None:
            #to to get into the list in specified address 
            for j in range(len(self.data_map[i])):
                #return the key
                 all_keys.append(self.data_map[i][j][0])
     return all_keys


my_hash_table=HashTable()
my_hash_table.set_items('bolts',1400)
my_hash_table.set_items('washers',50)
my_hash_table.set_items('lumber',70)
print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('vishnu'))

print(my_hash_table.keys())
my_hash_table.print_table()

