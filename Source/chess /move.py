def translate_movement(movements):
	move_list = list(map(str,movements.split(",")))
	move_current = move_list[0]
	move_next = move_list[1]

	# a5,a8 ----> (1,4),(1,1)
	# alpha to number 
	change_ATN = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
	move_current = repr(change_ATN[move_current[0]])+repr(9-int(move_current[1])
	move_next = repr(change_ATN[move_next[0]])+repr(9-int(move_next[1])

	return move_current+","+move_next


