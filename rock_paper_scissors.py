from random import randint
counter_win = 0
counter_lose = 0
counter_draw = 0
while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    print("If you want the game to stop, enter: stop")
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == 'stop':
        break
    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid Input. Try again...')
        print()
        continue

    computer_random_number = randint(1, 3)
    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")

    if player_move == rock and computer_move == scissors \
            or player_move == scissors and computer_move == paper \
            or player_move == paper and computer_move == rock:
        counter_win += 1
        print('You win!')
    elif player_move == computer_move:
        counter_draw += 1
        print('Draw!')
    else:
        counter_lose += 1
        print('You lose!')
    print()

print(f'Win: {counter_win}')
print(f'Draw: {counter_draw}')
print(f'Lose: {counter_lose}')