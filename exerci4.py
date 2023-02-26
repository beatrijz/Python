metroA = float (input ("Digite o valor em metros da área que será pintada: "));
LITROS_LATA = 18;
VALOR_LATA = 80.00;

quant_lata = (metroA // 54 )
if (quant_lata%54 == 0):
    
    print(f"Você irá precisar de {quant_lata} latas de tinta")
    
    valor_Compra = float (quant_lata * VALOR_LATA)
    
    print(f"O valor total da sua compra é de R$ {valor_Compra}")

elif (quant_lata%54 != 0):
    quant_lata = quant_lata + 1
    
    print("Você irá precisar de", quant_lata)
    
    valor_Compra = float (quant_lata * VALOR_LATA)
    print(f"O valor total da sua compra é de R$ {valor_Compra}")

