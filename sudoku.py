correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

teste = [[0,1,2],
           [2,0,1],
           [1,2,0]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(grid):
	l, i = len(grid), 0

	new_grid = []
	for y in range(len(grid)):
		new_grid.append([])
		for x in range(len(grid)):
#			new_grid[y].append([])
			new_grid[y].append(grid[x][y])
	while i < l:
		#print i
		j = 0
		while j < l:
			#print "POS("+str(i)+";"+str(j)+")\tVALUE:" + str(grid[i][j]) + "\n"
			count = 0
			counter = 0
			#new_grid[j][i] = grid[i][j]

			for e in grid[i]:
				if not isinstance(e, int):
					#print "Incorrect type"
					return False
				else:
					if e<=0 or max(grid[i])+1-min(grid[i])>l:
						#print "MAX="+str(max(grid[i]))+" min="+str(min(grid[i]))+" Diff:"+str(max(grid[i])+1-min(grid[i]))
						return False

				if grid[i][j] == e:
					count = count + 1
				#print "Is "+str(grid[i][j])+" = "+str(e)+"? "+str(grid[i][j]==e)+"\n"
			#print "COUNTER: " + str(count)
			if count > 1:
				#print "Value is repeated (row)"
				return False
			for d in new_grid[i]:
				if new_grid[i][j] == d:
					counter = counter + 1
			if counter > 1:
				#print "Value is repeated (column)"
				return False
			j = j +1
		i = i + 1

	return True



print check_sudoku(teste)
print "------------------------------"
print check_sudoku(incorrect)
#>>> False
print check_sudoku(correct)
#>>> True
print check_sudoku(incorrect2)
#>>> False
print check_sudoku(incorrect3)
#>>> False
print check_sudoku(incorrect4)
#>>> False
print check_sudoku(incorrect5)
#>>> False


