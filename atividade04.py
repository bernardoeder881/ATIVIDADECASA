valordacompra = float(input('Informe o valor da compra: '))
desconto = 0
acrecimo = 0
print("""

[1] À vista 

[2] Pix 

[3] Débito 

[4] Crédito 

[5] Cheque 
""")
formadepagamento = int(input ('Informe a forma de pagamento: '))
match formadepagamento:
    case 1:
        desconto = valordacompra * 0.1
        valorfinal = valordacompra - desconto
        formadepagamento = "À vista"           
        print (f'Forma de pagamento {formadepagamento}')
        print (f'Valordacompra {valordacompra}')
        print (f'Valor final {valorfinal}')
    case 2:
        valorfinal = valordacompra
        formadepagamento = "Pix"
        print (f'Forma de pagamento {formadepagamento}')
        print (f'Valordacompra {valordacompra}')
        print (f'Valor final {valorfinal}')
    case 3:
        acrecimo = valordacompra * 0.05
        valorfinal = valordacompra + acrecimo
        formadepagamento = "Débito"
        print (f'Forma de pagamento {formadepagamento}')
        print (f'Valordacompra {valordacompra}')
        print (f'Valor final {valorfinal}')
    case 4:
        acrecimo = valordacompra * 0.08
        valorfinal = valordacompra + acrecimo
        formadepagamento = "Crédito"
        print (f'Forma de pagamento {formadepagamento}')
        print (f'Valordacompra {valordacompra}')
        print (f'Valor final {valorfinal}')
    case 5:
        acrecimo = valordacompra * 0.12
        valorfinal = valordacompra + acrecimo
        formadepagamento = "Cheque"
        print (f'Forma de pagamento {formadepagamento}')
        print (f'Valordacompra {valordacompra}')
        print (f'Valor final {valorfinal}')
    case _:
        formadepagamento = "inválida"
        valorfinal = "Não calculado"
        valordacompra = "Não calculado"
        print (f'Forma de pagamento {formadepagamento}')





