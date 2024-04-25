from math import *
from random import *

def interceptar(robo, bola, tempo):

  mod_tan = sqrt(((bola['x'] - robo['x'])/(bola['y'] - robo['y']))**2)

  return mod_tan

robo_xi_max = int(2 * 100)
robo_xi_min = 0

robo_yi_max = int(1.5 * 100)
robo_yi_min = int(-0.5 * 100)

while(True):
  robo_xi = randint(robo_xi_min, robo_xi_max) / 100
  robo_yi = randint(robo_yi_min, robo_yi_max) / 100
  dist_i = sqrt((robo_xi - 1)**2 + (robo_yi - 0.5)**2)
  if dist_i <= 1:
    break
  else:
    continue



robo = {
  'x': robo_xi,
  'y': robo_yi,
  'raio': 0.09, #m
  'vel_max': 2.8,
  'vel': 0,
  'vel_x': 0,
  'vel_y': 0,
  'acc': 0,
  'acc_x': 0,
  'acc_y': 0,
  'interceptado': False
}

bola = {
  'x': 1,
  'y': 0.5,
  'distancia': dist_i
}



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
print(robo['x'], robo['y'])
print(interceptar(robo, bola, dados_bola))
