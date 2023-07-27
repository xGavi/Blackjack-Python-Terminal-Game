import classes as c

board = c.Board()

def played(xy):
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
	#print(played)
	return played

def counter(pC):
    for index, value in enumerate(board.boardDict.values()):
        if all(x == y for x, y in zip(value, pC)):
        	print(index)
        	return index
    return 'Error: invalid cell'

def play(p, xy):
	if len(xy) != 2:
		return 'Error: invalid coord'
	pC = played(xy)
	count = counter(pC)
	if count == 'Error: invalid cell':
		return 'Error: invalid cell'

	board.boardDict.update({c.grob[f'c{count}']:p})
	c.grob[f'c{count}'] = c.Cell(pC[0], pC[1], p)
	c.cells[count] = c.Cell(pC[0], pC[1], p)
	return

def game():
	while True:
		print(board)
		pX = input("Player X's turn. Where do you want to play? (l#)\n")
		while play('X', pX) != None:
			print(play('X', pX))
			pX = input("Player X's turn. Where do you want to play? (l#)\n")
		print(board)
		if board.checkWin() != None:
			print(board.checkWin())
			break

		pO = input("Player O's turn. Where do you want to play? (l#)\n")
		while play('O', pO) != None:
			print(play('X', pX))
			pO = input("Player O's turn. Where do you want to play? (l#)\n")
		print(board)
		if board.checkWin() != None:
			print(board.checkWin())
			break