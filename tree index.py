MAX_SIZE = 10
  

def sortArrayUsingCounts(arr, n):
  
    
    count = [0]*MAX_SIZE
    for i in range(n):
        count[arr[i]] += 1
  
    index = 0
    for i in range(MAX_SIZE):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
  
  

def removeAndPrintResult(arr, n, ind1, ind2=-1):
    for i in range(n-1, -1, -1):
        if i != ind1 and i != ind2:
            print(arr[i], end="")
  
  

def largest3Multiple(arr, n):
  
    
    s = sum(arr)
  
    
    if s % 3 == 0:
        return True
  
    
    sortArrayUsingCounts(arr, n)
  
    
    remainder = s % 3
  
    
    if remainder == 1:
        rem_2 = [0]*2
        rem_2[0] = -1; rem_2[1] = -1
  
        
        for i in range(n):
  
            
            if arr[i] % 3 == 1:
                removeAndPrintResult(arr, n, i)
                return True
  
            if arr[i] % 3 == 2:
  
                
                if rem_2[0] == -1:
                    rem_2[0] = i
  
                
                elif rem_2[1] == -1:
                    rem_2[1] = i
  
        if rem_2[0] != -1 and rem_2[1] != -1:
            removeAndPrintResult(arr, n, rem_2[0], rem_2[1])
            return True
  
    
    elif remainder == 2:
        rem_1 = [0]*2
        rem_1[0] = -1; rem_1[1] = -1
  
        
        for i in range(n):
  
            
            if arr[i] % 3 == 2:
                removeAndPrintResult(arr, n, i)
                return True
  
            if arr[i] % 3 == 1:
  
               
                if rem_1[0] == -1:
                    rem_1[0] = i
                  
                
                elif rem_1[1] == -1:
                    rem_1[1] = i
                      
        if rem_1[0] != -1 and rem_1[1] != -1:
            removeAndPrintResult(arr, n, rem_1[0], rem_1[1])
            return True
  
    print("Not possible")
    return False
  
  
arr = [5,4,3,1,1]
n = len(arr)
largest3Multiple(arr, n)
