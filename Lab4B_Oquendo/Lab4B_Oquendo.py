#Sebastian Oquendo
#Lab4B
#SE126.02
#02-14-22

# ------------------------------------

#	seatMap		=	function for display seating chart
#	selectRow	=	function for user to select desired row
#	selectSeat	=	function for user to select desired seat
#	seatAssign	=	function for selecting seats and marking them unavailable

#------------- FUNCTIONS ----------------

def seatMap(aA, bB, cC, dD):
	for r in range (1, 8):
		print("	Row", r, " | ", aA[r]," ", bB[r], "|   |", cC[r], " ", dD[r], "\n")

def selectRow():
	row = int(input(" What row would you like to choose? [1-7]: "))

	return row

def selectSeat():
	seat = input(" What seat would you like? [ex. A-D]: ").upper()

	return seat

def cont():
	
	answer = input("Would you like to make another reservation? [Y/N]: ").upper()
	while answer == "Y":

		print("		 SEATING CHART\n\n")

		seatMap(aisleA, aisleB, aisleC, aisleD)
		print("\n")

		row = selectRow()
		seat = selectSeat()

		seatAssign(row, seat, aisleA, aisleB, aisleC, aisleD)
		print("\n")
	
	if answer == "N":
		print("\nThank you for placing your reservations.")

	else:
		print("\nINVALID ENTRY, PLEASE ANSWER Y OR N")

def seatAssign(row, seat, aA, bB, cC, dD):

	if seat == "A" and aA[row] != "X":
		aA[row] = "X"
		print(" \nYour reservation has been placed.")
		
	elif seat == "B" and bB[row] != "X":
		bB[row] = "X"
		print(" \nYour reservation has been placed.")
		
	elif seat == "C" and cC[row] != "X":
		cC[row] = "X"
		print(" \nYour reservation has been placed.")
	
	elif seat == "D" and dD[row] != "X":
		dD[row] = "X"
		print(" \nYour reservation has been placed.")
		
	else:
		input(" \n *ERROR* INVALID ENTRY, PLEASE SELECT ANOTHER SEAT - PRESS ANY KEY TO CONTINUE")

#---------------- MAIN -----------------

aisleA = ["", "A", "A", "A", "A", "A", "A", "A"]
aisleB = ["", "B", "B", "B", "B", "B", "B", "B"]
aisleC = ["", "C", "C", "C", "C", "C", "C", "C"]
aisleD = ["", "D", "D", "D", "D", "D", "D", "D"]

answer = "Y"
while answer == "Y":

	print("		 SEATING CHART\n\n")

	seatMap(aisleA, aisleB, aisleC, aisleD)
	print("\n")

	row1 = selectRow()
	seat1 = selectSeat()

	seatAssign(row1, seat1, aisleA, aisleB, aisleC, aisleD)
	print("\n")
	seatMap(aisleA, aisleB, aisleC, aisleD)

	answer = input("\nWould you like the reserve another seat? [Y/N]: ").upper()
	while answer != "Y" and answer != "N":
		print("\n*ERROR: INVALID ENTRY!* Please enter Y or N: ")
		answer = input("\nWould you like the reserve a seat? [Y/N]: ").upper()

print("\nThank you for choosing to fly with us.")
