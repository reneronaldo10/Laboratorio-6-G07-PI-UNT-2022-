
def T(n):
    if n == 0:
        return n
    
    elif n == 1:
        return 1
    
    elif n == 2:
        return 1
        
    else:
        return T(n-1)+T(n-2)+T(n-3)
    

print ('======TRIBONACCI======')
n = int(input("Ingrese el número de término que desea hallar: "))

print('El número de posición ', n, 'es: ', T(n))