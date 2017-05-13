#Python3 Tic Tac Toe game (2 players)
#Created by George Moura, 2017, Federal University of Paraiba
#Good code for understanding and learning of python language, basics and syntax.

tie = 0

#AUXILIAR FUNCTIONS:

def create_matrix(): #initialize the matrix 3x3
	matrix = [[" " for i in range(3)] for j in range(3)]
	return matrix 

def verify_list(list): #returns true if all elements of a list are the same and different from whitespace, false otherwise
	return ((len(set(list)) <= 1) and (" " not in list))

def decorator(func): #this decorator will print the winner, the winner is returned by win() function

	def wrap(matrix, tie):
		result = func(matrix, tie)
		if result and result[1] != -1:
			print("\nThe winner is: \"", result[1], "\" !!")
			return True
		elif result and result[1] == -1:
			print("\nWe have a tie!")
			return True
		else:
			return False

	return wrap


#GAME FUNCTIONS:

def get_pos(): #read the player's next move
	valid = False
	while not valid:
		posx = int(input("Enter your position( x , y ):\nx:"))
		posy = int(input("y:"))
		if posx < 0 or posx > 2 or posy < 0 or posy > 2:
			print("\nSelect coordinates on range [0, 2] only!")
		else:
			valid = True
	return (posx, posy)


def print_matrix(matrix): #print the matrix state
	print("\n")
	print(matrix[0][0], " | ", matrix[0][1], " | ", matrix[0][2])
	print("--------------")
	print(matrix[1][0], " | ", matrix[1][1], " | ", matrix[1][2])
	print("--------------")
	print(matrix[2][0], " | ", matrix[2][1], " | ", matrix[2][2])

@decorator
def win(matrix, tie): #this function will return false if no one won the game yet, returns a tuple (True, player) when someone win

	for row in matrix:
		if verify_list(row):
			return (True, row[0])

	if verify_list([matrix[0][0], matrix[1][0], matrix[2][0]]) or verify_list([matrix[0][0], matrix[1][1], matrix[2][2]]):
		return (True, matrix[0][0])
	if verify_list([matrix[0][1], matrix[1][1], matrix[2][1]]):
		return (True, matrix[0][1])
	if verify_list([matrix[0][2], matrix[1][2], matrix[2][2]]) or verify_list([matrix[0][2], matrix[1][1], matrix[2][0]]):
		return (True, matrix[0][2])
	if tie == 9:
		return (True, -1)

	return False

def write(matrix, char, pos): #this function write a move on the matrix
	global tie
	if matrix[pos[0]][pos[1]] == " ":
		matrix[pos[0]][pos[1]] = char
		tie += 1
	else:
		print("\nYou can't write on that position.")

	return matrix


#MAIN FUNCTION

def main(): #where the game happens
	
	global tie
	play_again = True

	while play_again:
		playable = False 	#validation variable to see if user the choosed a valid character
		tie = 0
		matrix = create_matrix() #initialize the matrix, and refresh it when necessary
		while(not playable):
			first = input("Who plays first? (\"X\" or \"O\"): ").upper()

			if first == "X":
				second = "O" 
			elif(first == "O"):
				second = "X"
			else:
				print("Choose only valid players! (\"X\" or \"O\")")
				continue

			playable = True

		turn = False 	#status variable to define wich player should make a move
		while(not win(matrix, tie)): #while nobody wins or we didn't got a tie yet...
			turn = not turn

			if turn:
				play = first
			else:
				play = second

			print("\n\"",play, "\" turn:")
			aux = tie
			while aux == tie: #this loop makes sure the player isn't writing above another character
				pos = get_pos()
				matrix = write(matrix, play, pos)
				print_matrix(matrix)

		again = input("\n Do you wanna play again?( Y / N )").upper()
		while again != "Y" and again != "N":
			again = input("\n Choose only valid options. Do you wanna play again? ( Y / N )").upper()

		if again == "N":
			play_again = False


main()

		

	