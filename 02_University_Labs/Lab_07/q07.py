units=int(input("Enter theBll no. of electricity units consumed: "))


if units<=50:
    Bill=units*3.50
elif units>50 and units <=150:
    Bll = 50*3.50+(units-50)*4.00
elif units>=150 and units <=250:
    Bll = 50*3.50+100*4.00+(units-150)*5.20
elif units>250:
    Bill = 50*3.50+100*4.00+(units-250)*6.50

print("Total Bill: ",Bill)