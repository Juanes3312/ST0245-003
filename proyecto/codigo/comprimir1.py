'''import zlib, sys, time, base64


text_string = open("./../enfermos/0397768d-9068-4b65-8e3a-945c69c75d9a_1140x641.csv", 'r').read()
text_bytes = text_string.encode("utf-8")
print("Raw size:", sys.getsizeof(text_string))

compress = zlib.compress(text_bytes,9)
print("9 compress sizs:", sys.getsizeof(compress))
'''

vacaEnfermoFinal = []
tam = len(listaEnfermos)
for i in range(tam):
    vacaEnfermoFinal.append("vacaEnfermo" + str(i))

b = 1
for archivo in listaEnfermos:
    nombre = vacaEnfermoFinal[b]
    nombre = []
    with open (archivo, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_file:
            vaca = [item.strip() for item in line.split(',')]
            nombre.append(vaca)
    if b == 2:
        break
    b = b + 1