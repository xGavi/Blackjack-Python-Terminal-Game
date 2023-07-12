class Cell:
	def __init__(self, x, y, state = '-'):
		self.x = x
		self.y = y
		self.state = state

	def __repr__(self):
		if self.state == '-':
			return ' '
		return self.state


class Board:
	def __init__(self):
		boardDict = {1:[1, 2, 3], 2:[1, 2, 3], 3:[1, 2, 3]}

	def __repr__(self):
		board =f'''
       a     b     c
          |     |     
    1  {c1}  |  {c2}  |  {c3}  
     _____|_____|_____
          |     |     
    2  {c4}  |  {c5}  |  {c6}  
     _____|_____|_____
          |     |     
    3  {c7}  |  {c8}  |  {c9}  
          |     |     
          '''
		return board


xCount = 1
yCount = 1
for i in range(9):
	globals()[f'c{i+1}'] = Cell(xCount, yCount)
	xCount += 1
	if xCount == 3:
		xCount = 1
		yCount += 1


board = Board()
print(board) 