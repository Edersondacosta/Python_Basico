#Ordenação

temperatura = [30, 33, 20, 10, -3, 2, 9, 6, 20, 30]
maior = temperatura[0]
for listatemperaturas in temperatura:
    if listatemperaturas >maior:
        maior = listatemperaturas
print ("maior temperatura foi= ", maior)

menor = temperatura[0]
for listatemperaturas in temperatura:
    if listatemperaturas <menor:
        menor = listatemperaturas
print ("maior temperatura foi= ", menor)

