n = {"Queen": "Bohemian Rhapsody",
     "Bee Gees": "Stayin' Alive",
     "U2": "One",
     "Michael Jackson": "Billie Jean",
     "The Beatles": "Hey Jude",
     "Bob Dylan": "Like A Rolling Stone"}

#3
print(len(n))

#4

print(n.keys())

for key in n.keys():
    print(key)

#5

print(n.values())

#6

for key, values in n.items():
    print(key,values)

#7

print(n.get("Promise of the Real","That is not a value in dictionary"))