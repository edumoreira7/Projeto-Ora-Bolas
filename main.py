dados_bola = {}

dados_a = []

trajetoria_bola = open("trajetoria_bola.txt", "r")

for linha in trajetoria_bola.readlines():
  dados_a.append(linha.strip().split('//'))

trajetoria_bola.close()
for i in range(len(dados_a)):
  dados_a[i][0] = float(dados_a[i][0])
  dados_a[i][1] = float(dados_a[i][1])
  dados_a[i][2] = float(dados_a[i][2])
  dados_bola[dados_a[i][0]] = {
    'x': dados_a[i][1],
    'y': dados_a[i][2],
  }

print(dados_bola)
