# SAP Interview

s = "Mary had a little lamb"
N = 3

#R = [‘Mary had a’, ‘had a little’, ‘a little lamb’]



def nGram(s, n):
    r = []
    s = s.split()
    for i in range(len(s)-n + 1):
        a = s[i: (i+n)]
        #print a
        a = ' '.join(a)
        r.append(a)
        #del a
    return r


print(nGram(s, N))


def nGram1(s, n):
    s = s.split()
    iterator = len(s) - n + 1
    r = []
    for i in range(iterator):
        a = s[i:i+n]
        a = ' '.join(a)
        r.append(a)
        a = []
    return r

print(nGram1(s, N))
    

"""
# In Interview - Google Docs:
S = ‘Mary had a little lamb’
N = 3

R = [‘Mary had a’, ‘had a little’, ‘a little lamb’]


s = s.split(“ ”)
def nGram(s, n):
	r = []
	For i in range(len(s)-(n)):
		a = s[i: (i+n)]
		a = ‘ ‘.join(a)
	r.append(a)
	return r


		
		


"""
