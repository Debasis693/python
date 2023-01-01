from numpy import*
a = array([[1,2,3,4],[10,20,30,40]])
#for i in a:
#    for n in i:
#        print(n)
#    print()
n = len(a)
i = 0
while i<n:
    j = 0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
    print()
