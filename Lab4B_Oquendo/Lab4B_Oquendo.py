#Sebastian Oquendo
#Lab4B
#SE126.02
#02-02-22




def seatMap(aA, bB, cC, dD):
	for r in range (1, 8):
		print("	Row", r, " | ", aA[r]," ", bB[r], "|   |", cC[r], " ", dD[r], "\n")

def selectRow():
	row = int(input("What row would you like to choose? [1-7]: "))

	return row

def selectSeat():
	seat = input("What seat would you like? [ex. A-D]: ").upper()

	return seat

def seatAssign(row, seat, aA, bB, cC, dD):

	if seat == "A" and aA[row] != "X":
		aA[row] = "X"
	if seat == "B" and bB[row] != "X":
		bB[row] = "X"

	else:
		print("This seat is already reserved, please select another: ")



#----------- MAIN -------------

print("	   Welcome to NEIT Airways\n")
print("		 SEATING CHART\n\n")

aisleA = ["", "A", "A", "A", "A", "A", "A", "A"]
aisleB = ["", "B", "B", "B", "B", "B", "B", "B"]
aisleC = ["", "C", "C", "C", "C", "C", "C", "C"]
aisleD = ["", "D", "D", "D", "D", "D", "D", "D"]

answer = "y"
while answer == "y":

	seatMap(aisleA, aisleB, aisleC, aisleD)

	row = selectRow()
	seat = selectSeat()

	seatAssign(row, seat, aisleA, aisleB, aisleC, aisleD)

	