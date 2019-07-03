def binarysearch(array, left, right, element):
    if right >= left:
       mid = (left + right)//2
       if array[mid] == element: 
            return mid 
       elif array[mid] < element:
            return binarysearch(array, mid+1, right, element)
       else:
            return binarysearch(array, left, mid-1, element)
    else:
        return -1
array = [1,4,6,8,9,34,60]
element = 80
result = binarysearch(array, 0, len(array)-1, element)
if result == -1:
     raise Exception('Element not found')
else:
     print ("Element is found at position %d"%result)
