# Method 1:
def multyOftherThanNumber(a):
    ret = [None] * len(a)
    for i in range(len(a)):
        mul = 1
        for j in range(len(a)):
            if i != j:
                mul *= a[j]
        ret[i] = mul
    return ret
print("Method 1:",multyOftherThanNumber([1,2,3,4]))


# Method 2:
def multyOftherThanNumber1(a):
    mul = 1
    ret = [None] * len(a)
    for i in range(len(a)):
        mul *= a[i]
    for i in range(len(a)):
        ret[i] = mul//a[i]
    return ret
print("Method 2:",multyOftherThanNumber1([1,2,3,4]))


# Method 3:
def multyOftherThanNumber3(a):
    mul = 1
    ret_lef = [None] * len(a)
    ret_right = [None] * len(a)
    ret = [None] * len(a)

    left = 1
    ret_lef[0] = 1
    for i in range(1,len(a),1):
        ret_lef[i]  = left * a[i-1]
        left = ret_lef[i]
    print("\tLeft Multi:",ret_lef)

    right = 1
    ret_right[len(a)-1] = 1
    for i in range(len(a)-2, -1, -1):
        ret_right[i] = right * a[i+1]
        right = ret_right[i]

    print("\tRight multy:",ret_right)

    for i in range(len(a)):
        ret[i] = ret_right[i] * ret_lef[i]
    return ret
print("Method 3:", multyOftherThanNumber3([1,2,3,4]))




# Method 4:
def multyOftherThanNumber4(a):
    prod = [None] * len(a)

    left = 1
    for i,n in enumerate(a):
        prod[i] = left
        left *= n

    right = 1
    for i in range(len(a)-1, -1, -1):
        prod[i] *= right
        right *= a[i]
    return prod
print("Method 4:", multyOftherThanNumber4([1,2,3,4]))
