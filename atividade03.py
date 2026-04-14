tempo = float(input('Informe o tempo de filiação em anos: '))
valor = float(input('Informe o valor movimentado: '))
if tempo > 3 or valor > 5000:
    print('Cooperado/a tem direito ao benefício especial.')
else:
    print('Cooperado/a não tem direito ao benefício especial.')
