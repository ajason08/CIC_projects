import numpy as np
import pandas as pd

'''
# conversors
def decimal2binary(x):
    return int(''.join(decimal2binary_rec(x,[])))
def decimal2binary_rec(x,aux):
    if x>2:
        decimal2binary_rec(x / 2,aux)
    else:
        aux.append(str(x/2))
    aux.append(str(x % 2))
    return aux

def binary2decimal(number_bin):
    number_bin = str(number_bin)
    lenght = len(number_bin)-1
    sum =0
    list_values = []
    for bin in number_bin:
        dec = int(bin)*(2**lenght)
        if dec:
            list_values.append(dec)
        sum+=dec
        lenght -=1
    return sum, list_values

# Binary operations
def binary_addition(x, y):
    x =str(x)
    y = str(y)
    max_len = max(len(x), len(y))
    # fill with zeros
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        sum = carry
        sum += int(x[i]) + int(y[i])

        # sum can be 0,1,2 or 3
        # if r==1 or r==3 then the bit == 1
        # if r==2 or r==3 then the carry  == 1

        bit = str(sum % 2)
        result = bit + result
        carry = 0 if sum < 2 else 1

    if carry:
        result = '1' + result

    return result

def binary_multiplication(x_n,y_n):
    x =str(x_n)
    y = str(y_n)
    lines = []
    zeros_count = len(y)-1
    for bit_y in y:
        if bit_y == "1":
            newlen = len(x) + zeros_count
            new_x= x.ljust(newlen, "0")
            lines.append(new_x)
        else:
            new_x = "".ljust(len(x), "0")
            lines.append(new_x)
        zeros_count -= 1

    full_addition = "0"
    for line in lines:
        full_addition = binary_addition(full_addition, line)
    return int(full_addition)

# Decimal operation
def multiplication_using_binary_methods(x,y):
    bin_x = decimal2binary(x)
    bin_y = decimal2binary(y)
    mult = binary_multiplication(bin_x,bin_y)
    return mult, binary2decimal(mult)

def addition_using_binary_methods(x,y):
    bin_x = decimal2binary(x)
    bin_y = decimal2binary(y)
    add = binary_addition(bin_x,bin_y)
    return add, binary2decimal(add)

def division_and_module(a,d):
    if d==0:
        return "indeterminado", "indeterminado"
    if d<0:
        a=-a
        d=-d
    q=0
    r = abs(a)
    while r >=d:
        r-=d
        q+=1
    if a<0 and r>0:
        r= d-r
        q = -(q+1)
    residuo = r
    cociente = q
    return cociente, residuo

def exponencial_modulo(base, exponente, modulo):
    exp_bin= decimal2binary(exponente)
    descomposition = binary2decimal(exp_bin)[1]
    list_for_product=[]
    for exp in descomposition:
        list_for_product.append(base**exp % modulo)
    return prod(list_for_product) % modulo


print "========== Operaciones en base 2 ========="
dec= 7
print "binario del decimal ", dec, ":", decimal2binary(dec)

bin = 111
print "decimal del binario ", bin, ":", binary2decimal(bin)[0]

print "sum:", binary_addition(1,111)
print "mult:", binary_multiplication(111011,111)


nro_1 = 7
nro_2 = 9
bin_add, dec_add = addition_using_binary_methods(nro_1,nro_2)
bin_mult, dec_mult = multiplication_using_binary_methods(nro_1,nro_2)

print "========== Operaciones usando base 2 ========="
print "usando los numeros ", nro_1, " y ", nro_2
print "suma en binario: ", bin_add
print "suma en decimal: ", dec_add[0]
print "multiplicacion en binario: ", bin_mult
print "multiplicacion en decimal: ", dec_mult[0]


print "\n"

dividendo = 63
divisor= 9
cociente, residuo = division_and_module(dividendo,divisor)

print "operando", dividendo,"/",divisor
print "cociente:", cociente," y ", "residuo:", residuo


base=3
exponente=128
modulo = 7
result_em = exponencial_modulo(base, exponente, modulo)

print "El residuo usando exponenciacion modular es:", result_em

# =========================================================================
'''
def gcd(a, b):

    es_divisible = False
    while not es_divisible:
        r = b % a
        if r ==0:
            es_divisible = True
        else:
            b = a
            a = r
    return a

def bezout(a, b):
    # this algorithm focus on the coefient of bezaut,
    # finally firts argument is the inverse, the second one is which muliply the module and the third one is the gcd
    if b == 0:
        return 1, 0, a
    else:
        q = a/b
        r = a % b
        x, y, g = bezout(b, r)
        # print q, r, "bezout", y, x - q * y, g
        return y, x - q * y, g



def teorema_chino_del_residuo(matriz):
    modulos = matriz['elemento_m']
    coefs = matriz['elemento_b']
    m = np.prod(modulos)
    M =[m/x for x in modulos]
    inversos = []
    for i in range(len(coefs)):
        inverso = bezout(M[i],modulos[i])[0]
        inversos.append(inverso)

    matrix_resultado = pd.DataFrame({"coefs" : matriz['elemento_b'],
                        'M': M,
                        'Y':inversos
                        })
    nro_filas = len(matrix_resultado)
    valor = sum(np.prod(matrix_resultado.iloc[i]) for i in range(nro_filas))
    return valor % m, m



# Euclides theorem and Bezout identities
a, m = 34017, 58029
print "Resultado usando gcd:", gcd(a,m)
inverso, k_multiplica_modulo, gcd = bezout(a,m)

print "\nResultado usando Bezout:"
print "inverso modular: %d,\nentero k que multiplica al modulo: %d \ngcd: %d" % (inverso, k_multiplica_modulo, gcd)

# Teorema chino del residuo
matrix_tcr = {'elemento_b' : [1,2,3,4],
         'elemento_m' : [2,3,5,11]}
valor, modulo = teorema_chino_del_residuo(matrix_tcr)
print "\nResultado usando Teorema chino del residuo:\n %d mod %d" % (valor, modulo)

# https://primes.utm.edu/lists/small/small3.html
longPrime = 203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123
print longPrime*2

p = 11
g = 8
s= 6
k = 8
K= g**k % p
delta = s+k*K % (p-1)
print K, delta

aa = -g**delta
bb = -K**k
inverso, k_multiplica_modulo, gcd = bezout(aa,p)
print "inverso modular: %d,\nentero k que multiplica al modulo: %d \ngcd: %d" % (inverso, k_multiplica_modulo, gcd)
v = inverso*bb % p
print "v: %d" % v

for i in range (10):
    print 2**i % 11