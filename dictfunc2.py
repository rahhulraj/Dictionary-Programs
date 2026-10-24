print("_________________________________________________________________")
print("")

Marks={
    "python":45,
    "c pro":49,
    "java":28
}
print(Marks)
sum=0
for submark in Marks.values():
    sum=sum+submark
print("SUM OF ALL SUBJECT :",sum)

print("_________________________________________________________________")
print("")

items={
    "book":50,
    "laptop":69000,
    "mobile":25000,
    "tv":25000,
    "watch":2500,
}
count=0
basevalue=0
basekey=0
print(items)

for itemname,itemprice in items.items():
        count=count+1
        if count==1:
                basevalue=itemprice
                basekey=itemname
        else:
               if basevalue<itemprice:
                      basevalue=itemprice
                      basekey=itemname
           
print("HIGHEST PRICE ITEM :",basekey)

print("_________________________________________________________________")
print("")


students={
    "Neymar":80,
    "Messi":45,
    "Ronaldo":65,
    "Maradona":35,
    "Pele":90
}

for name,mark in students.items():
    if mark>50:
        print(name,end="\t")

print("_________________________________________________________________")
print("")


student = {
    "name": "Neymar",
    "age": 36,
    "place": "Brazil"
}

if "age" in student:
    print("Age key exists")
else:
    print("Age key does not exist")

print("_________________________________________________________________")
print("")


products={
    "Pen":20,
    "Bag":800,
    "Book":150,
    "Pencil":10,
    "Watch":1200
}
count=0
for price in products.values():
    if price>100:
        count=count+1
print("Number of products:",count)
