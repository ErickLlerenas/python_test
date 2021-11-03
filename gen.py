gen = (i +1 for i in range(100) if i%2!=0 )

for x in gen:
    print(x)


arreglo = [1,2,3]

arreglo.append(4)
print(arreglo)

tupla = (1,2,3,4)

comp = [i +1 for i in range(100) if i%2!=0 ]
comp.append(101)
print(comp)

dic = {'color': 'red','size': 100, 'width':200}

for key in dic:
    print(key + ': ' + str(dic[key]))
    if 'color' in dic:
        print(dic['color'])

def multiplicacion(a1,a2):
    return a1*a2


def mult(a1,a2,i=0,a=0):
    if i<a2:
        return mult(a1,a2,i+1,a1 + a)
    else:
        return a


def mult2(*args):
    res = 1
    for i in args:
        res*=1
    return res

def mult3(**kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res*=kwargs[key]

    return res

def mult4(*args, **kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res*=kwargs[key]

    for i in args:
        res*=i
        
    return res

#multiplicacion normal
print(multiplicacion(2,6))

#multiplicaciones recursivas
print(mult(2,6))
print(mult2(2,6))
print(mult3(num = 2,num2 = 6,num3 = 4))
print(mult3(num = 2,num2 = 6,num3 = 4,num4 = 3))




