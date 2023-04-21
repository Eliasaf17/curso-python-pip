import random


def choose_option():
  options = ('piedra', 'papel', 'tijera')
  user = input('piedra, papel o tijera --> ').lower()
  computer = random.choice(options)

  while not user in options:
    print('Escoja una de las tres opciones disponibles ')
    user = input('piedra, papel o tijera --> ').lower()
  
  print('User option --> ', user)
  print('Computer option --> ', computer)

  return user, computer
def check_rules(user, computer, user_w, com_w):
  if computer == user:
    print('Empate!')
  elif user == 'piedra':
    if computer == 'tijera':
      print('piedra gana a tijera')
      print('Usuario gana!')
      user_w += 1
    else:
      print('papel gana a piedra')
      print('Computadora gana!')
      com_w += 1
  elif user == "papel":
    if computer == 'piedra':
      print('papel gana a piedra')
      print('Usuario gana!')
      user_w += 1
  
    else:
      print('tijera gana a papel')
      print('Computadora gana!')
      com_w += 1
      
  elif user == 'tijera':
    if computer == 'papel':
      print('tijera gana a papel')
      print('Usuario gana!')
      user_w += 1
      
    else:
      print('piedra gana a tijera')
      print('Computadora gana!')
      com_w += 1

  return user_w, com_w
def run():
  user_w = 0
  com_w = 0
  round = 1
  while True:
    print('-' * 15)
    print('User wins --> ', user_w)
    print('COM wins --> ', com_w)
    if user_w <= 3 and com_w <= 3 : print('ROUND ', round, '¡FIGTH!')
    print('-' * 15)
    round += 1
      
    user, computer = choose_option()
    user_w, com_w = check_rules(user, computer, user_w, com_w)
    
    if user_w == 3 :
      print('El usuario ganó el juego ¡Felicitaciones!')
      break
    
    elif com_w == 3 :
      print('La computadora ganó el juego ¡mejor suerte la proxima!')
      break

run()