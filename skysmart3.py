board = list(range(0,9))

cells = 3

dashes = 13

spaces = 14
counter = 0

is_win = False

win_coords = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (8, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
)

player_token = ''



print('The game is over!\nUse your brain :)')




while not is_win:
    for i in range(cells):
        print(' ' * spaces, end='')
        print('-' * dashes)
        print(' ' * spaces, end='')
        print(f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print(' ' * spaces, end='')
        print('-' * dashes)


    if counter % 2 == 0:
        player_token = 'X'
    else:
        player_token = 'O'

    player_answers = input(f'Where we put a {player_token}?:')
    player_answers = int(player_answers)


    if str(board[player_answers]) not in'XO':
        board[player_answers] = player_token
    else:
        print('This cell is already taken!')
        continue

    counter += 1

    if counter > 4:
        for each in win_coords:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                is_win = True
                break
        if is_win:
            print(f'{player_token} is win!')
            break

    if counter == 9:
        print("Draw! You're amazing!")
        break


input( "Нажми Enter для выхода")
