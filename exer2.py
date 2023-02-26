lista = [8,9,7];
lista2 = [4,5,6];

i = 0;
soma = 0;

for i in range(3):
   n = lista[i]; 
   soma = soma + n;
   i += 1;
   
media1 = soma/3;
print ('A média da primeira lista é: {}'.format(media1));

y = 0;
soma2 = 0;

for y in range(3):
   n1 = lista2[y]; 
   soma2 = soma2 + n1;
   y += 1;
   media2 = soma2/3;
print ('A média da segunda lista é: {}'.format(media2));

media = 0;
media = (media1 + media2)/2;
print ('A média das médias é: {}'.format (media));

  