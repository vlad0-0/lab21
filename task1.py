a = input()
c = 2
if a == "":
    print(0)
else:
    for j in range(len(a)-1):
        if a[j] == " " and a[j+1] != " ":
            c += 1
    if a[0] == " ":
        c -= 1
    if a[-1] == " ":
        c -= 1
    if a[0] != " " and a[-1] != " ":
        c -= 1
    print(c)
