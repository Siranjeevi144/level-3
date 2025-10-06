print("Ajith super market")
print("Nehru street,pudhuchery")
print("-----------")
print("Bill recipt")
print("-----------")
no=input("Enter the input no:")
name=input("Enter the particular:")
rate=int(input("Enter the rate:"))
qnty=int(input("Enter the quantity:"))
total=rate*qnty
print("Total amont in rupees:",total)
if(total>=100000):
    gst=total*10/100
elif(total>=50000):
    gst=total*5/100
elif(total>=20000):
    gst=total*3/100
elif(total>=10000):
    gst=total*2/100
else:
    gst=tatal*1/100
print("GST(goods and service tax):",gst)
amount=gst+total
print("Amount to be paid:",amount)
