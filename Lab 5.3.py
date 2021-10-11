#Student ID:1201200678
#Student Name: Law Qian Er
#Q1 of lab5 exercise

def get_cm():
    cm=float(input("Enter centimeter : "))
    m=cm_to_m(cm)
    print("{:.2f} centimeters equals to {:.2f} meters".format(cm,m))

def cm_to_m(cm):
    meter=cm/100
    return meter

def get_m():
    m=float(input("Enter meter : "))
    cm=m_to_cm(m)
    print("{:.2f} meters equals to {:.2f} centimeters".format(m,cm))

def m_to_cm(m):
    cm=m*100
    return cm

print("======================================")
print("                MENU                  ")
print("======================================")
print("1.    Convert centimeter to meter")
print("2.    Convert meter to centimeter")
print("======================================")

choice=int(input("Enter your choice : "))

if(choice==1):
    get_cm();
elif(choice==2):
    get_m();
else:
    print("Invalid choice")




