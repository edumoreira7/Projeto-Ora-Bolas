import math
import random

dados_bola = {}

roboXmax = int(2 * 100)
roboXmin = 0

roboYmax = int(1.5 * 100)
roboYmin = int(-0.5 * 100)

while(True):
  roboX = random.randint(roboXmin, roboXmax) / 100
  roboY = random.randint(roboYmin, roboYmax) / 100
  dist_i = math.sqrt((roboX - 1)**2 + (roboY - 0.5)**2)
  if dist_i <= 1:
    break
  else:
    continue
    
robo = {
  'raio_interceptacao': 0.10,
  'x':roboX,
  'y':roboY,
  'velocidade_max':2.8,
  'aceleracao_max':2.8,
}

def distancia(x1, y1, x2, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  
def leitura_dados():
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

leitura_dados()

def interceptar_bola(trajetoria, velocidade_maxima):
  # Posição inicial da pessoa (começa no ponto médio do plano)
  robo_x = robo['x']
  robo_y = robo['y']
  
  # Raio de interceptação (9 centímetros)
  raio_interceptacao = robo['raio_interceptacao']
  
  # Tempo atual
  tempo_atual = min(trajetoria.keys())
  
  # Loop para simular o movimento da bola
  for tempo, posicao_bola in trajetoria.items():
    posicao_x = posicao_bola['x']
    posicao_y = posicao_bola['y']

    # Calcula o vetor da posição da bola para a pessoa
    vec_x = robo_x - posicao_x
    vec_y = robo_y - posicao_y

    # Calcula o comprimento do vetor
    vec_comprimento = math.sqrt(vec_x ** 2 + vec_y ** 2)

    # Normaliza o vetor para ter comprimento 1 (para obter a direção)
    vec_x /= vec_comprimento
    vec_y /= vec_comprimento

    # Calcula a distância que a pessoa se move nesta iteração
    distancia_movimento = min(velocidade_maxima * (tempo - tempo_atual), distancia(robo_x, robo_y, posicao_x, posicao_y) - raio_interceptacao)

    # Calcula o número de intervalos de 20 milissegundos
    num_intervalos = int((tempo - tempo_atual) / 0.02)
    
    # Atualiza a posição do robô a cada intervalo de 20 milissegundos
    for _ in range(num_intervalos):
        # Calcula a nova posição da pessoa
        robo_x -= vec_x * (distancia_movimento / num_intervalos)
        robo_y -= vec_y * (distancia_movimento / num_intervalos)

    # Atualiza o tempo atual
    tempo_atual = tempo

    # Verifica se a pessoa interceptou a bola
    if distancia(robo_x, robo_y, posicao_x, posicao_y) <= raio_interceptacao:
        print(f"A pessoa intercepta a bola em ({posicao_x}, {posicao_y}) no tempo {tempo}.")
        return


interceptar_bola(dados_bola, robo['velocidade_max'])
