#Student ID: 1201200678
#Student Name: Law Qian Er

BA=1.50
GR=5.60

print("Invoice for Fruits Purchase")
print("---------------------------------")
banana=int(input("Enter the quantity (comb) of bananas bought:"))
grape=int(input("Enter the amount (kg) of grapes bought:"))

total1=BA*banana
total2=GR*grape
total=total1+total2

print("Item\t\tQty\tPrice\t\tTotal ")
print("Banana (combs)\t{}\tRM{:.2f}\t\tRM{:.2f}".format(banana,BA,total1))
print("Grapes (kg)   \t{} \tRM{:.2f}\t\tRM{:.2f}".format(grape,GR,total2))
print("Total: RM{:.2f}".format(total))