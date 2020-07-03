import numpy as np


def goedal_relation(u, v):
    p = []
    for x in u.T:
        for y in v:
            if x <= y:
                p.append(1)
            else:
                p.append(y)
    return np.array(p).reshape(u.shape[0], v.shape[0])


def system_relation(u, v):
    s = []
    for x, y in zip(u, v):
        p = goedal_relation(x, y)
        s.append(p)
    s = np.array(s)

    initial = True
    for i in s:
        if initial:
            inter = i
            initial = False
            continue
        sol = []
        if inter.any():
            for x, y in zip(inter, i):
                for a, b in zip(x, y):
                    temp = min(a, b)
                    sol.append(temp)
            inter = np.array(sol).reshape(inter.shape)
    solution = inter
    return solution


xval = input('Enter Number of Element for X:')
yval = input('Enter Number of Element for Y:')
#print(xval, yval)

ux = []
while True:
    x = list(map(str, input("Enter a value for X(Enter x to exit): ").split()))
    if x[0] == 'x':
        break
    ux.append([float(i) for i in x][:int(xval)])
ux = np.array(ux)
print('ux:\n', '\n'.join('{}'.format(i) for i in ux))

vy = []
while True:
    y = list(map(str, input("Enter values for Y(Enter x to exit): ").split()))
    if y[0] == 'x':
        break
    vy.append([float(i) for i in y][:int(yval)])
vy = np.array(vy)
print('vy:\n', '\n'.join('{}'.format(i) for i in vy))

p = system_relation(ux, vy)
print('Greatest Solution for the whole system:\n', '\n'.join('{}'.format(i) for i in p))