from math import factorial



def combinatoria(n,r):
    comb = float(factorial(n) / (factorial(r) * (factorial(n - r))))
    return comb

def binomialFDP(p,n,x):
    comb = combinatoria(n,x)
    p1 = float(p**x)
    p2 = float((1-p)**(n-x))
    prob = comb*p1*p2
    return prob
'''
# esperanza de una hipergeometrica
w= 0
r = 4
n = 3
N = 10
for i in range(4):
    w += i*(combinatoria(r,i)*combinatoria(N-r,n-i))/combinatoria(N,n)
print w
print (combinatoria(4,1)*combinatoria(6,2))/combinatoria(10,3)
exit()
'''


w = 0
N= 30
p= float(1)/6
for r in range(4):
    #print binomialFDP(0.2, 25, i)
    w += binomialFDP(p, N, r)
    print w
print w