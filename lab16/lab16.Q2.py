#to find simple intrest and total amount
principle=int(input( "enter the principle amount"))
rate=int(input ("enter the rate in percentage"))
time=int(input ("enter the time in years"))
simple_intrest= (principle * rate * time/100)
print ("the simple intrest is   " , simple_intrest)
amount=simple_intrest + principle
print ("the total principle and intrest is", amount)