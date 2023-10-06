for n in range(1, 6):
    allat:str = input(f'kérem az {n}. állatfajtát: ')
    if allat == 'fotel': break
else: print('ügyi vagy, egyik állatod sem fotel!!!')
# ciklushoz tartozó 'else' akkor fut le, 
# ha a ciklus sosem futott 'break'-re