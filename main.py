import functions as f

while f.board.win == '':
	print(f.board.boardDict)
	print(f.board)
	pX = input("Player X's turn. Where do you want to play? (l#)\n")
	while f.play('X', pX) != None:
		print(f.play('X', pX))
		pX = input("Player X's turn. Where do you want to play? (l#)\n")
	print(f.board.boardDict)
	print(f.board)
	if f.board.checkWin() != '':
		print(f.board.checkWin())
		break

	pO = input("Player O's turn. Where do you want to play? (l#)\n")
	while f.play('O', pO) != None:
		print(f.play('X', pX))
		pO = input("Player O's turn. Where do you want to play? (l#)\n")
	print(f.board.boardDict)
	print(f.board)
	if f.board.checkWin() != '':
		print(f.board.checkWin())
		break