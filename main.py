import classes as c
from time import sleep as slp

a = 'Error: invalid cell'
board = c.Board()

def play(p, xy):
	played = []
	for coord in xy:
		try:
			played.append(int(coord))
		except:
			if coord == 'a':
				played.append(1)
			elif coord == 'b':
				played.append(2)
			elif coord == 'c':
				played.append(3)
			else:
				return 'Error: invalid coord'
	count = 0
	for cell in board.boardDict:
		count += 1
		if board.boardDict[cell] == played:
			break
	print(c.grob[f'c{count}'].state)
	slp(1)
	if c.grob[f'c{count}'].state == '-':
		c.grob[f'c{count}'] = c.Cell(played[0], played[1], p)
		return ''
	else:
		return a

while board.win == '':
	print(board.boardDict)
	print(board)
	pX = input("Player X's turn. Where do you want to play? (l#)\n")
	play('X', pX)
	while play('X', pX) != '':
		print(a)
		pX = input("Player X's turn. Where do you want to play? (l#)\n")
	print(board.boardDict)
	print(board)
	if board.checkWin() != '':
		print(board.checkWin())
		break
	pO = input("Player O's turn. Where do you want to play? (l#)\n")
	play('O', pO)
	while play('O', pO) != '':
		print(a)
		pO = input("Player O's turn. Where do you want to play? (l#)\n")
	print(board.boardDict)
	print(board)
	if board.checkWin() != '':
		print(board.checkWin())
		break