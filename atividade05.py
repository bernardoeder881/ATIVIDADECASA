nota1 = float(input('Insira a primeira nota.'))
nota2 = float(input('Insira a segunda nota.'))
notas = float(input(
    """Insira a nota substituitiva. 
Caso não tenha feito insira -1 """))

if nota1 < nota2 < notas or nota1 < notas < nota2:
    media = (nota2 + notas)/2
    print(f'A média é {media}')

if nota2 < nota1 < notas or nota2 < notas < nota1:
    media = (nota1 + notas)/2
    print(f'A média é {media}')

if notas < nota1 < nota2 or notas < nota2 < nota1:
    media = (nota2 + notas)/2
    print(f'A média é {media}')



