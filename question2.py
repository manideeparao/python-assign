
def Sort_Tuple(tup):  
    tup.sort(key = lambda x: x[1])  
    return tup  
  
# Driver Code  
tup = input("Enter the tuples")
print(Sort_Tuple(tup)) 


