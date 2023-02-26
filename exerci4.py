#Faça um programa para uma loja de tintas. O programa deverá pedir o
#tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
#vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#quantidades de latas de tinta a serem compradas e o preço total.


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

