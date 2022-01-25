
#Sebastian Oquendo
#Week 1 Review Demo

#variable dictionary
#begin_balance      beginning balance
#apy                Annual percentage
#month_deposit      amount of money being deposited at the end of each month
#years              amount of time the money will be invested
#month_interest     monthly interest
#total_months       number of months the money will be invested
#month_no           individual month that interest will be calculated
#end_balance        amount of money at the end of the month
#line_ct            line counter
#maxlines           number of lines to be printed
#
#===========================================

begin_balance = float(input("Enter the beginning balance $"))
apy = float(input("Enter the interest rate as a percent 5.2% = 5.2 "))
month_deposit = float(input("How much money do you want to invest each month $"))
years = int(input("How many years is this investment going to be? "))

rate = apy/100
total_months = years*12

month_no = 1
line_ct = 0
max_lines = 15


print("   beg           int         end")

while (month_no <= total_months):
    month_interest = begin_balance * rate/12
    end_balance = begin_balance + month_interest + month_deposit
    begin_balance = end_balance

    print("{0:8.2f}    {1:8.2f}    {2:8.2f}".format(begin_balance, month_interest, end_balance))
    line_ct = line_ct + 1
    if (line_ct >= max_lines):
        input("Press any key to continue..")
        line_ct = 0
        print("   beg           int         end")


    month_no = month_no + 1