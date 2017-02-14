class GenerateMoves(object):
	"""docstring for GenerateMoves"""
	
	def __init__(self, arg):
		super(GenerateMoves, self).__init__()
		self.arg = arg
		
		# Rook
	def Rook(self, matrix, color, i, j):
	    list_moves = []
	    atack_piceces = []
	    bound_for_moves = []

	    # Right moves check
	    for column in arnge(j, 9):
	        if (matrix[i][column] != "" and column != j):
	            if color == "w":
	                if (matrix[i][column][0] == "b"):
	                    atack_piceces.append([matrix[i][column], i, column])
	                    break
	                if (matrix[i][column][0] == "w"):
	                    bound_for_moves.append([i, column])
	                    break
	            else:
	                if (matrix[i][column][0] == "w"):
	                    atack_piceces.append([matrix[i][column], i, column])
	                    break
	                if (matrix[i][column][0] == "b"):
	                    bound_for_moves.append([i, column])
	                    break

	    # Left moves check
	    for column in arnge(j, 0, -1):
	        if (matrix[i][column] != "" and column != j):
	            if color == "w":
	                if (matrix[i][column][0] == "b"):
	                    atack_piceces.append([matrix[i][column], i, column])
	                    break
	                if (matrix[i][column][0] == "w"):
	                    bound_for_moves.append([i, column])
	                    break
	            else:
	                if (matrix[i][column][0] == "w"):
	                    atack_piceces.append([matrix[i][column], i, column])
	                    break
	                if (matrix[i][column][0] == "b"):
	                    bound_for_moves.append([i, column])
	                    break

	    # Down moves check
	    for row in arnge(i, 9):
	        if (matrix[row][j] != "" and row != i):
	            if color == "w":
	                if (matrix[row][j][0] == "b"):
	                    atack_piceces.append([matrix[row][j], i, row])
	                    break
	                if (matrix[row][j][0] == "w"):
	                    bound_for_moves.append([i, row])
	                    break
	            else:
	                if (matrix[row][j][0] == "w"):
	                    atack_piceces.append([matrix[row][j], i, row])
	                    break
	                if (matrix[row][j][0] == "b"):
	                    bound_for_moves.append([i, row])
	                    break

	    # Up moves check
	    for row in arnge(i, 0, -1):
	        if (matrix[row][j] != "" and row != i):
	            if color == "w":
	                if (matrix[row][j][0] == "b"):
	                    atack_piceces.append([matrix[row][j], i, row])
	                    break
	                if (matrix[row][j][0] == "w"):
	                    bound_for_moves.append([i, row])
	                    break
	            else:
	                if (matrix[row][j][0] == "w"):
	                    atack_piceces.append([matrix[row][j], i, row])
	                    break
	                if (matrix[row][j][0] == "b"):
	                    bound_for_moves.append([i, row])
	                    break



	# Bishop
	def Bishop(self, matrix, color, i, j):
	    list_moves = []
	    atack_piceces = []
	    bound_for_moves = []

	    # in y=x direction x positive
	    x = i
	    for column in range(j, 9):
	        if (matrix[x][column] != "" and column != j):
	            x -= 1
	            if x > 0:
	                if color == "w":
	                    if (matrix[x][column][0] == "b"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "w"):
	                        bound_for_moves.append([x, column])
	                        break
	                else:
	                    if (matrix[x][column][0] == "w"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "b"):
	                        bound_for_moves.append([x, column])
	                        break

	    # in y=x direction x negetive
	    x = i
	    for column in range(j, 0, -1):
	        if (matrix[x][column] != "" and column != j):
	            x += 1
	            if x <= 8:
	                if color == "w":
	                    if (matrix[x][column][0] == "b"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "w"):
	                        bound_for_moves.append([x, column])
	                        break
	                else:
	                    if (matrix[x][column][0] == "w"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "b"):
	                        bound_for_moves.append([x, column])
	                        break

	    # in y=-x direction x positive
	    x = i
	    for column in range(j, 9):
	        if (matrix[x][column] != "" and column != j):
	            x += 1
	            if x <= 8:
	                if color == "w":
	                    if (matrix[x][column][0] == "b"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "w"):
	                        bound_for_moves.append([x, column])
	                        break
	                else:
	                    if (matrix[x][column][0] == "w"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "b"):
	                        bound_for_moves.append([x, column])
	                        break

	    # in y=-x direction x negetive
	    x = i
	    for column in range(j, 0, -1):
	        if (matrix[x][column] != "" and column != j):
	            x -= 1
	            if x <= 8:
	                if color == "w":
	                    if (matrix[x][column][0] == "b"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "w"):
	                        bound_for_moves.append([x, column])
	                        break
	                else:
	                    if (matrix[x][column][0] == "w"):
	                        atack_piceces.append([matrix[x][column], x, column])
	                        break
	                    if (matrix[x][column][0] == "b"):
	                        bound_for_moves.append([x, column])
	                        break
		# Queen
	def Qeen(self, matrix, color, i, j):
	    Bishop(matrix, color, i, j)
	    Rook(matrix, color, i, j)


	def Knight(self, matrix, color, i, j):
	    list_moves = []
	    atack_piceces = []
	    bound_for_moves = []

	    list_moves = [(i + 1, j + 2), (i - 1, j + 2), (i + 2, j + 1), (i - 2, j + 1), (i + 1, j - 2), (i - 1, j - 2),
	                  (i - 2, j - 1), (i + 2, j - 1)]
	    for tuple in list_moves:
	        if (0 <= tuple[0] <= 8) and (0 <= tuple[1] <= 8):
	            if matrix[tuple[0]][tuple[1]] != "":
	                if color == "w":
	                    if matrix[tuple[0]][tuple[1]][0] == "b":
	                        atack_piceces.append([matrix[tuple[0]][tuple[1]], tuple[0], tuple[1]])
	                    elif matrix[tuple[0]][tuple[1]][0] == "w":
	                        bound_for_moves.append([tuple[0], tuple[1]])
	                else:
	                    if matrix[tuple[0]][tuple[1]][0] == "w":
	                        atack_piceces.append([matrix[tuple[0]][tuple[1]], tuple[0], tuple[1]])
	                    elif matrix[tuple[0]][tuple[1]][0] == "b":
	                        bound_for_moves.append([tuple[0], tuple[1]])
	            else:
	                list_moves.append([tuple[0], tuple[1]])


	# King
	def king(self, matrix, color, i, j):
	    list_moves = []
	    atack_piceces = []
	    bound_for_moves = []

	    list_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1),
	                  (i - 1, j - 1)]

	    for tuple in list_moves:
	        if (0 <= tuple[0] <= 8) and (0 <= tuple[1] <= 8):
	            if matrix[tuple[0]][tuple[1]] != "":
	                if color == "w":
	                    if matrix[tuple[0]][tuple[1]][0] == "b":
	                        atack_piceces.append([matrix[tuple[0]][tuple[1]], tuple[0], tuple[1]])
	                    elif matrix[tuple[0]][tuple[1]][0] == "w":
	                        bound_for_moves.append([tuple[0], tuple[1]])
	                else:
	                    if matrix[tuple[0]][tuple[1]][0] == "w":
	                        atack_piceces.append([matrix[tuple[0]][tuple[1]], tuple[0], tuple[1]])
	                    elif matrix[tuple[0]][tuple[1]][0] == "b":
	                        bound_for_moves.append([tuple[0], tuple[1]])
	            else:
	                list_moves.append([tuple[0], tuple[1]])


	# Pawn
	def Pawn(self, matrix, color, i, j):
	    list_moves = []
	    atack_piceces = []
	    bound_for_moves = []

	    # first_moves
	    if i == 2:
	        if matrix[i][j + 1] == "":
	            list_moves.append([i, j + 1])
	        if matrix[i][j + 2] == "":
	            list_moves.append([i, j + 2])

	    elif i == 7:
	        if matrix[i][j - 1] == "":
	            list_moves.append([i, j - 1])
	        if matrix[i][j - 2] == "":
	            list_moves.append([i, j - 2])

	    # moves
	    if matrix[i, j + 1] == "":
	        list_moves.append([i, j + 1])

	    if color == "w":
	        if matrix[i - 1][j + 1] == "":
	            list_moves.append([i + 1, j + 1])
	        elif matrix[i - 1][j + 1][0] == "b"
	            atack_piceces.append([matrix[i + 1][j + 1], i + 1, j + 1])
	        elif matrix[i - 1][j - 1] == "":
	            list_moves.append([i + 1, j + 1])
	        elif matrix[i - 1][j - 1][0] == "b"
	            atack_piceces.append([matrix[i + 1][j + 1], i + 1, j + 1])

	    else:
	        if matrix[i + 1][j + 1] == "":
	            list_moves.append([i + 1, j + 1])
	        elif matrix[i + 1][j + 1][0] == "w"
	            atack_piceces.append([matrix[i + 1][j + 1], i + 1, j + 1])
	        elif matrix[i + 1][j - 1] == "":
	            list_moves.append([i + 1, j + 1])
	        elif matrix[i + 1][j - 1][0] == "w"
	            atack_piceces.append([matrix[i + 1][j + 1], i + 1, j + 1])

