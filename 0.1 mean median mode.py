# Find Mean, median and Mode:


def findMean(arr):
    l = len(arr)
    mean = sum(arr)/l
    return mean


def findMedian(arr):
    n = len(arr) 
    arr.sort() 
      
    if n % 2 == 0: 
        median1 = n_num[n//2] 
        median2 = n_num[n//2 - 1] 
        median = (median1 + median2)/float(2)
    else: 
        median = n_num[n//2] 
    return median
    

def findMode1(num_list):
    import collections
       
    # calculate the frequency of each item
    data = collections.Counter(num_list)
    data_list = dict(data)
    
    # Print the items with frequency
    
    # Find the highest frequency
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    return mode_val

def findMode(n_num):
    dic = {}
    for i in n_num:
        if i not in dic:
            dic[i] = 1
        else:
            for key, val in dic.items():
                if key == i:
                    dic[key] += 1
    mod = [k for k, v in dic.items() if v == max(list(dic.values()))]
    return mod


n_num = [1, 2, 3, 4,5,6, 6, 5] 

print 'Mean :', findMean(n_num)
print 'Median:', findMedian(n_num)
print 'Mode:', findMode(n_num)
print 'Mode1:', findMode1(n_num)
