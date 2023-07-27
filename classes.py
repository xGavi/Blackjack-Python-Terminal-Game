from logo import logo as l

class Cell:
	def __init__(self, x, y, state = '-'):
		self.x = x
		self.y = y
		self.state = state

	def __repr__(self):
		if self.state == '-':
			return ' '
		return self.state

xCount = 1
yCount = 1
cells = []
for i in range(9):
  globals()[f'c{i}'] = Cell(xCount, yCount)
  cells.append(globals()[f'c{i}'])
  xCount += 1
  if xCount == 4:
    xCount = 1
    yCount += 1

class Board:
	def __init__(self):
		self.boardDict = {cell:[cell.x, cell.y] for cell in cells}
		self.boardRows = [[], [], []]
		self.boardColumns = [[], [], []]
		self.boardDiagonals = [[], []]
		self.winC = []
		self.win = ''
			
	def __repr__(self):
		board = f'''
		{l}
		           a     b     c
		              |     |     
		        1  {c0}  |  {c1}  |  {c2}  
		         _____|_____|_____
		              |     |     
		        2  {c3}  |  {c4}  |  {c5}  
		         _____|_____|_____
		              |     |     
		        3  {c6}  |  {c7}  |  {c8}  
		              |     |     
		'''
		return board

	def genRows(self):
		count = 0
		for cell in cells:
			if count < 3:
				if len(self.boardRows[0]) >= 3:
					self.boardRows[0] = []
				(self.boardRows[0]).append(cell.state)
				count += 1
			elif count < 6:
				if len(self.boardRows[1]) >= 3:
					self.boardRows[1] = []
				(self.boardRows[1]).append(cell.state)
				count += 1
			elif count < 9:
				if len(self.boardRows[2]) >= 3:
					self.boardRows[2] = []
				(self.boardRows[2]).append(cell.state)
				count += 1
		return self.boardRows

	def genColumns(self):
		count = 1
		for cell in cells:
			if count % 3 == 1:
				if len(self.boardColumns[0]) >= 3:
					self.boardColumns[0] = []
				(self.boardColumns[0]).append(cell.state)
				count += 1
			elif count % 3 == 2:
				if len(self.boardColumns[1]) >= 3:
					self.boardColumns[1] = []
				(self.boardColumns[1]).append(cell.state)
				count += 1
			elif count % 3 == 0:
				if len(self.boardColumns[2]) >= 3:
					self.boardColumns[2] = []
				(self.boardColumns[2]).append(cell.state)
				count += 1
		return self.boardColumns

	def genDiagonals(self):
		count = 1
		for cell in cells:
			if count == 1 or count == 9:
				if len(self.boardDiagonals[0]) >= 3:
					self.boardDiagonals[0] = []
				(self.boardDiagonals[0]).append(cell.state)
				count += 1
			elif count == 3 or count == 7:
				if len(self.boardDiagonals[1]) >= 3:
					self.boardDiagonals[1] = []
				(self.boardDiagonals[1]).append(cell.state)
				count += 1
			elif count == 5:
				if len(self.boardDiagonals[0]) >= 3:
					self.boardDiagonals[0] = []
				if len(self.boardDiagonals[1]) >= 3:
					self.boardDiagonals[1] = []
				(self.boardDiagonals[0]).append(cell.state)
				(self.boardDiagonals[1]).append(cell.state)
				count += 1
			else:
				count += 1
		return self.boardDiagonals

	def winConditions(self):
		if self.winC != []:
			self.winC = []
		for triplet in self.genRows():
			self.winC.append(triplet)
		for triplet in self.genColumns():
			self.winC.append(triplet)
		for triplet in self.genDiagonals():
			self.winC.append(triplet)
		return self.winC

	def checkWin(self):
		winO = ['O', 'O', 'O']
		winX = ['X', 'X', 'X']
		for triplet in self.winConditions():
			if triplet == winO:
				self.win = 'Player O wins!'
				return self.win
			elif triplet == winX:
				self.win = 'Player X wins!'
				return self.win

grob = globals()