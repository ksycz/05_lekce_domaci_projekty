jmeno = input('Zadej sve jmeno, nepouzivaj zdrobneliny ')
print(jmeno)
if (jmeno[-1] == 'a' or jmeno[-1] == 'e') and jmeno != 'Honza':
    print('Jsi zena')
else:
    print('Jsi muz')
