#Sebastian Oquendo
#Lab4B
#SE126.02
#02-02-22




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
	
	answer = input("Would you like to make another reservation?: [Y/N]").upper()
	while answer == "Y":

		print("		 SEATING CHART\n\n")

		seatMap(aisleA, aisleB, aisleC, aisleD)
		print("\n")

		row = selectRow()
		seat = selectSeat()

		seatAssign(row, seat, aisleA, aisleB, aisleC, aisleD)
		print("\n")
	

def seatAssign(row, seat, aA, bB, cC, dD):

	if seat == "A" and aA[row] != "X":
		aA[row] = "X"
		print(" \nYour reservation has been placed.")
	if seat == "B" and bB[row] != "X":
		bB[row] = "X"
		print(" \nYour reservation has been placed.")
	if seat == "C" and cC[row] != "X":
		cC[row] = "X"
		print(" \nYour reservation has been placed.")
	if seat == "D" and dD[row] != "X":
		dD[row] = "X"
		print(" \nYour reservation has been placed.")
	if seat == "X":
		print(" \n *ERROR* This seat is already reserved, please select another: ")

	#else:
		#print(" \n *ERROR* This seat is already reserved, please select another: ")
		



#----------- MAIN -------------



aisleA = ["", "A", "A", "A", "A", "A", "A", "A"]
aisleB = ["", "B", "B", "B", "B", "B", "B", "B"]
aisleC = ["", "C", "C", "C", "C", "C", "C", "C"]
aisleD = ["", "D", "D", "D", "D", "D", "D", "D"]

answer = "y"
while answer == "y":

	print("		 SEATING CHART\n\n")

	seatMap(aisleA, aisleB, aisleC, aisleD)
	print("\n")

	row = selectRow()
	seat = selectSeat()

	seatAssign(row, seat, aisleA, aisleB, aisleC, aisleD)
	print("\n")

	#cont()
	

	