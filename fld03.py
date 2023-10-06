osszeg:int = 0
szam:int = 2345
while szam % 10 != 0:
    szam = int(input('írj be egy számot: '))
    osszeg += szam
print(f'számok összege: {osszeg}')