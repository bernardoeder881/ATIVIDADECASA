qtdestoque = float(input('Informe a quantidade do estoque: '))
qtdsolicitada = float(input('Informe a quantidade: '))
peso = float(input('Informe o peso: '))
if qtdestoque <= qtdsolicitada:
    if peso <= 50:
        print('Pedido liberado.')
else:
    print('O pedido não pode ser enviado.')
    