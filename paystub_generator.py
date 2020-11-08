# Author: Colin MacDonald
# Objective: Create a paystub generator that:
    # takes input from the user for name, hours worked, hourly rate, deductions, deduction rate needed
    # calculates gross pay (OT incl), OT hours, deduction amount, net pay
    # outputs a formated name, total hours, OT hours, hourly rate, gross pay, deductions, net pay

print ("Paystub Generator, please enter the following: ")

# input 
nameF = input("Please enter your first name: ")       
nameL = input("Please enter your last name: ")
hourRate = float (input("Please enter your hourly rate: "))
hourWork = float (input("Please enter your hours worked this week: "))

# Base pay calculations
if hourWork <=40:
    grossPay = hourRate * hourWork
    overTm = 0
else:
    grossPay = (hourRate * 40) + ((hourWork - 40) * hourRate * 1.5)
    overTm = hourWork - 40

# Deduction calculations
deductFlag = input("Are there deductions to enter? (Y/N): ")
if (deductFlag == "Y"):
    deductRate = float (input("Enter the deduction rate (_%): "))
    deductTotal = grossPay * (deductRate/100)
else:      
    deductTotal = 0

netPay = grossPay - deductTotal
        
# Output
print ("----------------------------------------------")
print ("Employee: ", nameL,",",nameF)
print ("Hours this week: {:.1f}".format(hourWork))
print ("Overtime Hours this week: {:.1f}".format(overTm))
print ("Hourly rate: ${:0,.2f}".format(hourRate))
print ("Gross pay: ${:0,.2f}".format(grossPay))
print ("Deductions: ${:0,.2f}".format(deductTotal))
print ("Net Pay: ${:0,.2f}".format(netPay))
