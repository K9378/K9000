import random

x_name = ""
o_name = ""
board_mode = 1
def hello():
  print(f'------------------------------------------------------------------------\n'
        f'---===+++===--- Добро пожаловать в игру крестики нолики! ---===+++===--- \n'
        f'------------------------------------------------------------------------\n')


def player_input():
  hello()
  player1 = input(f'Введите имя первого игрока : \n')
  player2 = input(f'Введите имя второго игрока : \n')
  global x_name
  global o_name
  player_random = random.randint(1, 10)
  if player_random > 6:
      x_name = player1
      o_name = player2
  else:
      x_name = player2
      o_name = player1
  board_select()

def board_select():
  global board_mode
  board_mode_check = input(f'Отображать поле с координатами? (y/n):')
  if board_mode_check == "y" or "n":
    if board_mode_check == "y":
      board_mode = 0
      tic_tac_toe()
    elif board_mode_check == "n":
      board_mode = 1
      tic_tac_toe()
    else:
      print("\nМожно вводить только y или n!")
      board_select()

def tic_tac_toe():
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  board_2 = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
  end = False
  win_board = [4, 9, 2, 3, 5, 7, 8, 1, 6]
  hello()
  board_cord = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

  def show_board():
    if board_mode == 1:
      print(f'{x_name} VS {o_name}\n')
      print('', board[0], ":", board[1], ":", board[2])
      print("---:---:---")
      print('', board[3], ":", board[4], ":", board[5])
      print("---:---:---")
      print('', board[6], ":", board[7], ":", board[8])
      print()
    else:
      print(f'{x_name} VS {o_name}\n')
      print("  0 1 2 ")
      print('0', board_2[0], board_2[1], board_2[2])
      print('1', board_2[3], board_2[4], board_2[5])
      print('2', board_2[6], board_2[7], board_2[8])
      print()

  def get_number():
    if board_mode:
      while True:
        number = input()
        try:
          number = int(number)
          if number in range(1, 10):
            return number
          else:
            print("\nНет такого поля!")
        except ValueError:
          print("\nМожно вводить только цифры!")
          continue
    else:
      while True:
        cords = input(f'Введите координаты: ').split()
        if len(cords) != 2:
          print(" Введите 2 координаты! ")
          continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
          print(" Введите числа! ")
          continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
          print(" Координаты вне диапазона! ")
          continue
        number = board_cord[x][y]
        print(number)
        return number

  def turn(player):
    index = get_number() - 1
    if board[index] == "X" or board[index] == "O":
      print("\nПоле уже занято!")
      turn(player)
    else:
      board[index] = player
      board_2[index] = player

  def win_check(player):
    count = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if board[x] == player and board[y] == player and board[z] == player:
              if win_board[x] + win_board[y] + win_board[z] == 15:
                print(f'Игра оконченна! \n')
                if player == "X":
                    print(f'Победил {x_name}!\n')
                    game_repeat()
                else:
                    print(f'Победил {o_name}!\n')
                    game_repeat()
                return True

    for a in range(9):
      if board[a] == "X" or board[a] == "O":
        count += 1
      if count == 9:
        print(f'Ни кто не победил! \n')
        game_repeat()
        return True

  while not end:
    show_board()
    end = win_check("O")
    if end == True:
      break
    print(f'Ходит {x_name} "X"')
    turn("X")

    show_board()
    end = win_check("X")
    if end == True:
      break
    print(f'Ходит {o_name} "O"')
    turn("O")


def game_repeat():
  end_game = input(f'Желаете сыграть еще раз? (y/n) :')
  if end_game == "y" or "n":
    if end_game == "y":
      player_change = input(f'Хотите сменить игроков?? (y/n) :')
      if player_change == "y" or "n":
        if player_change == "y":
          player_input()
        elif player_change == "n":
          board_select()
        else:
          print("\nМожно вводить только y или n!")
          game_repeat()
    elif end_game == "n":
      print("\nСпасибо за игру.")
    else:
      print("\nМожно вводить только y или n!")
      game_repeat()


player_input()
