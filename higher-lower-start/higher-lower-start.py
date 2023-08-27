import art as art
from game_data import data
import random
import os

score=0
continuar = True

while(continuar):
  print(art.logo)
  
  # escolhendo os competidores
  escolhaA = random.choice(data)
  escolhaB = random.choice(data)
  
  # garantindo que sao diferentes
  while escolhaB == escolhaA:
    escolhaB = random.choice(data)
  # printando o score anterior
  if(score > 0):
    print(f"Acertou!! Seu score eh {score}.")
  # escolhendo o vencedor
  if(escolhaA['follower_count']>escolhaB['follower_count']):
    vencedor='A'
  else:
    vencedor='B'
  
  print(f"Compare A: {escolhaA['name']}, um(a) {escolhaA['description']} de {escolhaA['country']}")
  
  print(art.vs)
  
  print(f"Contra B: {escolhaB['name']}, um(a) {escolhaB['description']} de {escolhaB['country']}")
  # comparando o numero de seguidores
  escolha = input("Quem tem mais seguidores? Digite A ou B: ")
  
  if(escolha == vencedor):
    score+=1
    os.system('cls')
  else:
    os.system('cls')
    print(art.logo)
    print(f"Errou, seu score final eh {score}")
    continuar = False