a:int = int(input(' egyenlő oldalú 3szög oldalának hossza (cm): '))
print(f'kerület hetede: {round(a*3/7, 2)} cm')

print('------------------------------')

r:int = int(input('kör sugarának hossza (cm): '))
print(f'kerülete: {2*r*3.14:.2f} cm')

print('------------------------------')

n:int = int(input('hány csillag legyen?: '))
print(f'Béla jutalma: {n * "*"}')
print('Béla jutalma:', end=' ')
for _ in range(n):
    print('*', end='')
print('\n')