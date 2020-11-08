# Use a Sentinel Loop to calculate the return on a variable rate investment over user set years

# define variables for inputing the values and sentinel
# the number count is used to check for first value and count the n list
# use a sentinel value 0 to indicate when the list ends
# return the value at year n and average income per year

print ("Hello, we will now calculate the variable rate of return on your Investment")

#input
SENTINEL = 0
havealldata = False
numCount = 0

princVal = float (input ("First, enter the principle ammount: $"))
runVal = princVal

# check Principle Value
if princVal <= 0:
    print ("Principle Value must be >0")
    princVal = float(input ("Please re-enter the principle ammount: $"))

# Input Interest & Evaluation loop
print ("Please enter an interest rate for each year invested (as -.-%) - Note: zero ends the calculation")

while (not havealldata) :
    intRate = float (input("Please enter an interest rate for year " +str(numCount + 1)+ " (in percent): ")) 
    if intRate == SENTINEL :
        havealldata = True
    else  :
        numCount = numCount + 1
        runVal = runVal * ((1 + (intRate/100)))
        
# Check against 0 interest value in year 1 & output calc            
if numCount == 0 :
    print ("you entered no data")
else:
    print ("At the end of", numCount,"years, your investment is worth: ${:.2f}".format(runVal,2))
    print ("Your average earnings per year are: ${:.2f}".format((runVal-princVal)/numCount))
))
