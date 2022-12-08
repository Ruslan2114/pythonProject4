board = list(range(0,9))


is_win = False
counter = 0
while not is_win:
    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

        player_answers = input(f'Где поставим  {player_token}?:')
        player_answers = int(player_answers)

        if str(board[player_answers]) not in 'XO':
            board[player_answers] = player_token
            print('OK')
        else:
            print('Неправильный ввод. Нужно ввести число.')
            continue