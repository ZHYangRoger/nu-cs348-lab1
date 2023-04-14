import common
def find_starting_position(map):
    for i in range(common.constants.MAP_HEIGHT-1):  #i is height
        for j in range(common.constants.MAP_WIDTH-1):  # j is width
            if map[i][j] == 2:
                #print(i, j)
                return i, j
            
def valid_move(nr, nc, map):
    return nc >= 0 and nr >= 0 and nc < common.constants.MAP_WIDTH and nr < common.constants.MAP_HEIGHT and not map[nr][nc] == 1 and not map[nr][nc] == 4
    
def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	start_x, start_y = find_starting_position(map)
	dfs_stack = [(start_x, start_y)]
	parent_dic = {}
	
	while dfs_stack:
		cur_row, cur_col = dfs_stack.pop()
		#print(cur_row, cur_col)
		if map[cur_row][cur_col] == 3:
			#print("Found")
			#print(parent_dic)
			found = True
			map[cur_row][cur_col] = 5
			while (cur_row, cur_col) != (start_x, start_y):
				cur_row, cur_col = parent_dic[(cur_row, cur_col)]
				#print(cur_row, cur_col)
				map[cur_row][cur_col] = 5
			map[start_x][start_y] = 5
			return found

		map[cur_row][cur_col] = 4
		#four_moves = [(cur_col, cur_row + 1), (cur_col + 1, cur_row), (cur_col, cur_row - 1), (cur_col - 1, cur_row)]
		four_moves = [(cur_row-1, cur_col), (cur_row, cur_col-1), (cur_row+1, cur_col), (cur_row, cur_col+1)]
		for move in four_moves:
			if valid_move(move[0], move[1], map):
				#print(move[0], move[1])
				dfs_stack.append((move[0], move[1]))
				parent_dic[(move[0], move[1])] = (cur_row, cur_col)
	#print("not found")
	return found

def bf_search(map):
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	start_x, start_y = find_starting_position(map)
	bfs_queue = [(start_x, start_y)]
	parent_dic = {}
	
	while bfs_queue:
		cur_row, cur_col = bfs_queue.pop(0)  #dequeue
		if map[cur_row][cur_col] == 3:
			found = True
			map[cur_row][cur_col] = 5
			while (cur_row, cur_col) != (start_x, start_y):
				cur_row, cur_col = parent_dic[(cur_row, cur_col)]
				map[cur_row][cur_col] = 5
			map[start_x][start_y] = 5
			return found

		map[cur_row][cur_col] = 4
		four_moves = [(cur_row, cur_col + 1), (cur_row + 1, cur_col), (cur_row, cur_col - 1), (cur_row - 1, cur_col)]
		for move in four_moves:
			if valid_move(move[0], move[1], map):
				bfs_queue.append((move[0], move[1]))
				parent_dic[(move[0], move[1])] = (cur_row, cur_col)
	return found
