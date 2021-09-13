#Student ID: 1201200678
#Student Name: Law Qian Er


LI=0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

litres=int(input("Enter amount of litres: "))
print("\nPrice per litres  = RM{:.2f}".format(LI))
print("Number of liters = ",litres)

total=litres*LI

print("Total: RM {:.2f}".format(total))