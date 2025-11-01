Dollar = {
    "Country" : "USA",
    "Symbol" : "$",
    "Visual" : "💵"
}
Yen = {
    "Country" : "Japan",
    "Symbol" : "¥",
    "Visual" : "💴"
}
Euro = {
    "Country" : "France",
    "Symbol" : "€",
    "Visual" : "💶"
}
Pound = {
    "Country" : "UK",
    "Symbol" : "£",
    "Visual" : "💷"
}
Rupee = {
    "Symbol" : "₹"
}

money = [Dollar,Yen,Euro,Pound,Rupee]

print(money[0])
print(money[1])
print(money[2])
print(money[3])

Rupee["Country"] = "India"
print(money[4]["Country"])

del Rupee["Country"]
print(money[4])