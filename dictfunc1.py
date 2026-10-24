print("")
fruits={
    "Apple":100,
    "Orange":60,
    "Mango":80
}
print("Apple Price is :",fruits["Apple"])

print("_________________________________________________________________")
print("")
nation={
    "India":"Delhi",
    "Japan":"Tokyo",
    "Russia":"Mosco",
    "America":"Washington DC",
    "Australia":"Sydney"
}
x=nation.keys()
print(x)
for i in nation:
    print(i,end="\t")

print("_________________________________________________________________")
print("")

Studentdetails={
    "Name":"Unknown",
    "Mark":50,
}
print("BEFORE UPDATION :",Studentdetails)
Studentdetails["Grade"]="A"
print("UPDATED :",Studentdetails)

print("_________________________________________________________________")
print("")

Employeedetails={
    "Name":"Person",
    "Salary":30000,
}
print("BEFORE UPDATION :",Employeedetails)
Employeedetails["Salary"]=25000
print("UPDATED :",Employeedetails)

print("_________________________________________________________________")
print("")