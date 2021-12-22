import func

func.toArduino("U3 F1 U2 L1 D1 B1 U1 R3 D3 R1 U2 D2 B2 D1 B2 R2 F2 U3 F2 B2 (20f)")

string = "WYGWYWGGOGBYYRROOROOYWBGBYBYRYWWBWGWBRWGOBBORRORBGRGWO"
y = 0
b = 0
g = 0
r = 0
w = 0
o = 0

# for item in string:
#     if item == "U":
#         y +=1
#     if item == "F":
#         b +=1
#     if item == "R":
#         g +=1
#     if item == "L":
#         r +=1
#     if item == "D":
#         w +=1
#     if item == "B":
#         o +=1
# print(y,b,g,r,w,o)

for item in string:
    if item == "Y":
        y +=1
    if item == "B":
        b +=1
    if item == "G":
        g +=1
    if item == "R":
        r +=1
    if item == "W":
        w +=1
    if item == "O":
        o +=1
print(y,b,g,r,w,o)

    