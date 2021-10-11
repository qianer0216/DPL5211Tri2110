#Student ID:1201200678
#Student Name: Law Qian Er
#Q3 of lab5 exercise
def get_bonus(unit,salary):
    
    if(unit>1000):
        bonusamt=salary*0.2
    elif(unit<1000 and unit>500):
        bonusamt=salary*0.1
    else:
        bonusamt=0
    
    return bonusamt

def get_nett_salary(bonusamt,salary):
    nettsalary=bonusamt+salary
    return nettsalary

def display(id,salary,unit,bonusamt,netsalary):
    print("\nStaff ID          : ",id)
    print("Staff salary      : RM {:.2f}".format(salary))
    print("Units sold        : ",unit)
    print("Bonus             : RM {:.2f}".format(bonusamt))
    print("Nett Salary       : RM {:.2f}".format(netsalary))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  DATA ENTRY                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
id=int(input("Enter staff id       : "))
salary=float(input("Enter staff salary  : RM "))
unit=int(input("Enter total units sold : "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                  SALARY SLIP               ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
bonusamt=get_bonus(unit,salary)
netsalary=get_nett_salary(salary,bonusamt)
display(id,salary,unit,bonusamt,netsalary)