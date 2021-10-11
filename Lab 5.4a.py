#Student ID:1201200678
#Student Name: Law Qian Er
#Q2a of lab5 exercise

def rectangle(width,length):
    area=width*length
    return area

def triangle(width,length):
    area=(width*length)/2
    return area

width=float(input("Enter width : "))
length=float(input("Enter length : "))
rarea=rectangle(width,length)
print("Rectangle area : {:.2f} ".format(rarea))
tarea=triangle(width,length)
print("Triangle area : {:.2f} ".format(tarea))