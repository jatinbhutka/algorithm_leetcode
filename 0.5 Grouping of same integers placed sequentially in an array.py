# Group multiple occurrence of array elements ordered by first occurrence



########## Method 1: ###############

def orderm(arr):
    hM = {}
    
    for i in range(len(arr)):
        hM[arr[i]] = hM.get(arr[i],0) + 1
#    print hM
    
    
    for i in range(len(arr)):
        
        c = hM.get(arr[i], None)
        if c != None:
            for j in range(0,c):
                print arr[i]," ",
            del hM[arr[i]] 
        
arr = [10, 5, 3, 10, 10, 4, 1, 3] 
orderm(arr)




########## Method 2: ###############

# A simple Python 3 program to 
# group multiple occurrences of 
# individual array elements 
  
# A simple method to group all 
# occurrences of individual elements 
def groupElements(arr, n): 
  
    # Initialize all elements 
    # as not visited 
    visited = [False] * n 
    #print visited

    # Traverse all elements 
    for i in range(0, n): 
      
        # Check if this is first occurrence 
        if (visited[i] == False): 
          
            # If yes, print it and  
            # all subsequent occurrences 
            print arr[i], " ",
            for j in range(i + 1, n): 
              
                if (arr[i] == arr[j]): 
                  
                    print arr[i]," ",
                    visited[j] = True
              
# Driver Code 
arr = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4] 
n = len(arr) 
groupElements(arr, n) 
