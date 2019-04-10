

numeros = [30, 33, 44, 10, -3, 2, 9, 6, 20, 31]
print (numeros)
i =0
for num in numeros:
    print ("sem enumerate.:  (%d)  ---> %d" % (i, num))
    i+=1


i=0
while i < len(numeros):
    print ("sem enumerate.: (%d)  ---> %d" % (i, numeros[i]))
    i+=1
