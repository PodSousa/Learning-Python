a = float(input(f'digite o primeiro número: '))
b = float(input(f'digite o segundo número: '))
c = float(input(f'digite o terceiro número: '))

if a < b and a < c:
    p = a
elif b < a and b < c:
    p = b
else:
    p = c

if b < a and a < c:
    s = a
elif c < a and a < b:
    s = a
elif a < b and b < c:
    s = b
elif c < b and b < a:
    s = b
elif a < c and c < b:
    s = c
else:
    s = c

if p < a and s < a:
    t = a
elif p < b and s < b:
    t = b
else:
    t = c
    
print(f'{p} < {s} < {t}')
