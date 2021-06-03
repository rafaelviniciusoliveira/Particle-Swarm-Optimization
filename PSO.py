import random
import numpy as np
import math

# --------------------------------------------------------PSO-----------------------------------------------------------------

def gera_particula(tamanho):
  particulas = np.array([[0 ,0, 0]]*tamanho,dtype='float')
  velocidade = np.array([[0 ,0, 0]]*tamanho,dtype='float')
  for i in range(tamanho):
    particulas[i] = np.array([[round(random.uniform(-5.12,5.12),3) ,round(random.uniform(-5.12,5.12),3), round(random.uniform(-5.12,5.12),3)]],dtype='float')
    velocidade[i] = np.array([[random.uniform(0,10.24) ,random.uniform(0,10.24), random.uniform(0,10.24)]],dtype='float')
  return particulas,velocidade

def rastrigin(particulas,dimensao):
    fitness = np.array([0],dtype=float)
    fitness = 10*dimensao
    for i in range (dimensao):
          fitness += particulas[i]**2 - (10*math.cos(2*math.pi*particulas[i]))
    return fitness

def melhor_local(particulas,Gl_valor,Gl_posicao,dimensao):
  for i in range(len(particulas)):
    resultado = rastrigin(particulas[i],dimensao)
    if Gl_valor[i]>resultado:
      Gl_valor[i] = resultado
      Gl_posicao[i] = particulas[i]
  
  return Gl_valor, Gl_posicao  

def melhor_global(particulas,Gb_valor,Gb_posicao,Gl_posicao,dimensao):
  for i in range(len(particulas)):
    melhor_resultado = rastrigin(particulas[i],dimensao)
    if Gb_valor>melhor_resultado:
      Gb_valor = melhor_resultado
      Gb_posicao = Gl_posicao[i]
    
  return Gb_valor,Gb_posicao
  
def novas_particulas(particulas,velocidade,Gl_posicao,Gb_posicao,c1,c2): 
  for i in range(len(particulas)):  
    velocidade[i] = velocidade[i] + c1*(Gl_posicao[i]-particulas[i]) + c2*(Gb_posicao-particulas[i])
    particulas[i] = particulas[i] + velocidade[i]
  return particulas, velocidade

def PSO(tamanho, c1, c2,geracoes,target):
  dimensao = 3
  Gb_valor = 100000
  Gb_posicao = [0 ,0, 0]
  Gl_valor = np.array([1000]*tamanho,dtype=float)
  Gl_posicao = np.array([[0 ,0, 0]]*tamanho,dtype='float')

  particulas,velocidade = gera_particula(tamanho)
  cont_geracoes = 0
  while(Gb_valor>target and cont_geracoes < geracoes):
    Gl_valor,Gl_posicao = melhor_local(particulas, Gl_valor,Gl_posicao,dimensao)
    Gb_valor,Gb_posicao = melhor_global(particulas,Gb_valor,Gb_posicao,Gl_posicao,dimensao)
    particulas, velocidade = novas_particulas(particulas,velocidade,Gl_posicao,Gb_posicao,c1,c2)
    cont_geracoes = cont_geracoes + 1

  return Gb_valor, cont_geracoes

valor_minino, interacao = PSO(1000,1,0.5,1000,0.001)

print("-------PSO-------\n")
print("Valor minino:",valor_minino,"\n Iterações:",interacao)




