import random

computer_wins = 0
user_wins = 0

rounds = 1
options = ('piedra', 'papel', 'tijera')

user_name = input('Como te llamaremos? -> ')

message_win = f'{user_name} ganaste esta vez'
message_lose = "Te gano la computadora esta vez"
message_final_win = f'{user_name} eres el ganador absoluto'
message_final_lose = "Perdiste contra la computadora, mejor suerte para la proxima"

def set_choices(options):
  
  computer_option = random.choice(options)
  user_option = input('piedra, papel o tijera => ').lower()

  if not user_option in options:
    print('esa opcion no es valida')
    return False, False
  else:
    print('-' * 10)
    print(f'{user_name} option =>', user_option)
    print('Computer option =>', computer_option)
    print('-' * 10)
    return user_option,computer_option

def check_choices(user_option, computer_option,user_wins, computer_wins):
  ''' 
  usando una logica numerica, piedra papel y tijera son 1, 2 y 3
  restando la eleccion de la computadora a la eleccion del usuario, el usuario solo gana cuando el resultado es 1 o -2
  User    PC       resultado
  piedra  papel    pierde
  1       2        1 - 2 = -1
  tijera  papel    gana
  3       2        3 - 2 = 1
  papel   piedra   gana
  2       1        2 - 1 = 1
  piedra  tijera   gana
  1       3        1 - 3 = -2
  tijera  piedra   pierde
  3       1        3 - 1 = 2
  etc.
  el usuario solo gana cuando el resultado es 1 o -2
  '''
  
  user_option_index = options.index(user_option)
  computer_option_index = options.index(computer_option)
  compare_options_index = user_option_index - computer_option_index

  if user_option_index == computer_option_index:
      print('Empate!')
      return user_wins, computer_wins
  elif compare_options_index == 1 or compare_options_index == -2:
    print(f'{user_option} gana a {computer_option}')
    print(message_win)
    return user_wins+1, computer_wins
  else:
    print(f'{computer_option} gana a {user_option}')
    print(message_lose)
    return user_wins, computer_wins+1

def print_results(user_wins,computer_wins):
  print('-' * 10)
  print("Computer wins: ", computer_wins)
  print(f'{user_name} wins: ', user_wins)

  if computer_wins == 2:
    print('=*' * 10)
    print(message_final_lose)

  if user_wins == 2:
    print('==*' * 10)
    print(message_final_win)
    

while True:
    print("\n")
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print("\n")

    #inicia las opciones
    user_option,computer_option = set_choices(options)
    if not user_option:
      continue
      
    user_wins, computer_wins = check_choices(user_option, computer_option,user_wins, computer_wins)
    
    
    if user_wins == 2 or computer_wins == 2:
      print_results(user_wins, computer_wins)
      break
    else:
      rounds += 1
    

    

    