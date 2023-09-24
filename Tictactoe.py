import time
import random
def display(board):
	print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
	print('     |	     |')
	print('  '+board[0]+'  |  '+board[1]+'  |  '+board[2])
	print('-----|-----|-----')
	print('  '+board[3]+'  |  '+board[4]+'  |  '+board[5])
	print('-----|-----|-----')
	print('  '+board[6]+'  |  '+board[7]+'  |  '+board[8])
	print('     |     |')

def choose_players():
	while True:
		x=input('Will player 1 be "X" or "O":\n')
		player1_marker=''
		player2_marker=''
		if x.lower()=='x':
			player1_marker='x'
			player2_marker='o'
			break
		elif x.lower()=='o':
			player1_marker='o'
			player2_marker='x'
			break
		else:
			print('please enter either X or O:\n')
			continue
	return (player1_marker,player2_marker)

def choose_first(player1_marker,player2_marker):
	lis=[]
	lis.append(player1_marker)
	lis.append(player2_marker)
	random.shuffle(lis)
	if player1_marker==lis[0]:
		return 'player 1'
	else:
		return 'player 2'

def square_check(board,position):
	if board[position-1].lower()=='x' or board[position-1].lower()=='o':
		return False
	else:
		return True

def board_check(board):
	num_of_markers=0
	for marker in board:
		if marker!=' ':
			num_of_markers+=1
	if num_of_markers==9:
		return True
	else:
		return False


def win_check(board):
	if (board[6] == 'x' and board[7] == 'x' and board[8] == 'x') or (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') or (board[0] == 'x' and board[1] == 'x' and board[2] == 'x') or (board[6] == 'x' and board[3] == 'x' and board[0] == 'x') or (board[7] == 'x' and board[4] == 'x' and board[1] == 'x') or (board[8] == 'x' and board[5] == 'x' and board[2] == 'x') or (board[6] == 'x' and board[4] == 'x' and board[2] == 'x') or (board[8] == 'x' and board[4] == 'x' and board[0] == 'x'):
		return 'x'
	elif (board[6] == 'o' and board[7] == 'o' and board[8] == 'o') or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o') or (board[0] == 'o' and board[1] == 'o' and board[2] == 'o') or (board[6] == 'o' and board[3] == 'o' and board[0] == 'o') or (board[7] == 'o' and board[4] == 'o' and board[1] == 'o') or (board[8] == 'o' and board[5] == 'o' and board[2] == 'o') or (board[6] == 'o' and board[4] == 'o' and board[2] == 'o') or (board[8] == 'o' and board[4] == 'o' and board[0] == 'o'):
		return 'o'
	else:
		return False

'''
GAMEPLAY
'''

print('\nWelcome to tic tac toe!\n')
while True:
	board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	player1_marker,player2_marker=choose_players()
	first_player=choose_first(player1_marker,player2_marker)
	print(f'{first_player} will go first!\n')
	player=first_player
	time.sleep(3)
	playing=True
	while playing:
		if player=='player 1':
			while True:
				display(board)

				if win_check(board)==player2_marker:
					print('player 2 wins')
					playing=False

				elif board_check(board)==True and win_check(board)==False:
					print('its a tie')
					playing=False
				
				else:
					while True:
						try:
							position=int(input(f'where would you like to place your marker player 1? input a number between 1 and 9 according to where you want to place the marker:\n'))
							if not(position in [1,2,3,4,5,6,7,8,9]):
								print('inbetween 1 and 9 please!\n')
						except:
							print('sorry, that is not a number\n')
						else:
							break

					while True:
						if square_check(board,position)==True:
							board[position-1]=player1_marker
							break
						else:
							print('sorry, that square is already taken\n')
							continue
					player='player 2'
					break
				break
		elif player=='player 2':
			while True:
				display(board)

				if win_check(board)==player1_marker:
					print('player 1 wins')
					playing=False
				
				elif board_check(board)==True and win_check(board)==False:
					print('its a tie')
					playing=False
				
				else:
					while True:
						try:
							position=int(input(f'where would you like to place your marker player 2? input a number between 1 and 9 according to where you want to place the marker:\n'))
							if not(position in [1,2,3,4,5,6,7,8,9]):
								print('inbetween 1 and 9 please!\n')
								continue
						except:
							print('sorry, that is not a number\n')
						else:
							while True:
								if square_check(board,position)==True:
									board[position-1]=player2_marker
									break
								else:
									while True:
										print('sorry, that square is already taken\n')
										position=int(input(f'where would you like to place your marker player 2? input a number between 1 and 9 according to where you want to place the marker:\n'))
										if not(position in [1,2,3,4,5,6,7,8,9]):
											print('inbetween 1 and 9 please!\n')
											continue
										else:
											break
									break
							break
					player='player 1'
					break
				break


	replay=input('would you like to play again?\n')
	if replay[0].lower()=='y':
		continue
	else:
		print('\nthanks for playing!\n')
		break
	break






		

























