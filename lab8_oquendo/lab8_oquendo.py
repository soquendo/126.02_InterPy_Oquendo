

#Sebastian Oquendo
#Lab4B
#SE126.02
#03-01-22

#==========================================================================================

# Write a program that can be used by a small theater to sell tickets for performances.  The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken.  Seats thar are available are represented by # and seats that are taken are represent by a *.

#	Row						Seats
#		   A  B  C  D  E  F  G  H  I  J  K  L  M  N O  P  Q  R S T U  V  W X Y Z 1 2 3 4
#	  1    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # # 
#	  2    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  3    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  4    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  5    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  6    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  7    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  8    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	  9    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	 10    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	 11    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	 12    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
# 	 13    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	 14    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #
#	 15    #  #  #  #  #  #  #  #  #  #  #  #  # #  #  #  #  # # # #  #  # # # # # # # #

#	The program should display the following seating map.  The user may enter the row and seat numbers for tickets being sold.  Every time a ticket or group of tickets is purchased, the program should display the total ticket prices and update the seating chart.
#	The program should keep a total of all ticket sales.  The user should be given option of viewing this amount.
#	The program should also give the user an option to see a list of how many seats have been sold, how many seats are available in each row, and how may seats are available in the entire theater.
#	The price for tickets are calculated using the following;
#	Row 1 – Row 5 are  $200.00
#	Row 6 – Row 10 are $175.00
#	Row 11 – Row 15 are $150.00

#==========================================================================================
import csv

rowCol = []
aCol = []
bCol = []
cCol = []
dCol = []
eCol = []
fCol = []
gCol = []
hCol = []
iCol = []
jCol = []
kCol = []
lCol = []
mCol = []
nCol = []
oCol = []
pCol = []
qCol = []
rCol = []
sCol = []
tCol = []
uCol = []
vCol = []
wCol = []
xCol = []
yCol = []
zCol = []
oneCol = []
twoCol = []
threeCol = []
fourCol = []

with open("D:\lab8.csv") as csvfile:
    fPlan = csv.reader(csvfile)

    for col in fPlan:
        rowCol.append(col[0])
        aCol.append(col[1])
        bCol.append(col[2])
        cCol.append(col[3])
        dCol.append(col[4])
        eCol.append(col[5])
        fCol.append(col[6])
        gCol.append(col[7])
        hCol.append(col[8])
        iCol.append(col[9])
        jCol.append(col[10])
        kCol.append(col[11])
        lCol.append(col[12])
        mCol.append(col[13])
        nCol.append(col[14])
        oCol.append(col[15])
        pCol.append(col[16])
        qCol.append(col[17])
        rCol.append(col[18])
        sCol.append(col[19])
        tCol.append(col[20])
        uCol.append(col[21])
        vCol.append(col[22])
        wCol.append(col[23])
        xCol.append(col[24])
        yCol.append(col[25])
        zCol.append(col[26])
        oneCol.append(col[27])
        twoCol.append(col[28])
        threeCol.append(col[29])
        fourCol.append(col[30])


def seatMap(a0, aA, aB, aC, aD, aE, aF, aG, aH, aI, aJ, aK, aL, aM, aN, aO, aP, aQ, aR, aS, aT, aU, aV, aW, aX, aY, aZ, a1, a2, a3, a4):
    for i in range (0, 16):
        print(" Row", i, " ", a0[i], aA[i], aB[i], aC[i], aD[i], aE[i], aF[i], aG[i], aH[i], aI[i], aJ[i], aK[i], aL[i], aM[i], aN[i], aO[i], aP[i], aQ[i], aR[i], aS[i], aT[i], aU[i], aV[i], aW[i], aX[i], aY[i], aZ[i], a1[i], a2[i], a3[i], a4[i])
   

answer = "Y"    
while answer == "Y":

    print("\n		 SEATING CHART\n\n")
    seatMap(rowCol, aCol, bCol, cCol, dCol, eCol, fCol, gCol, hCol, iCol, jCol, kCol, lCol, mCol, nCol, oCol, pCol, qCol, rCol, sCol, tCol, uCol, vCol, wCol, xCol, yCol, zCol, oneCol, twoCol, threeCol, fourCol)



    answer = input("\nWould you like to reserve a seat? [Y/N]: ").upper()
    while answer != "Y" and answer != "N":
		print("\n*ERROR* *INVALID ENTRY* Please enter Y or N: ")
		answer = input("\nWould you like to reserve a seat? [Y/N]: ").upper()

print("Thank you for using the program")