s = input()
r = 0
l = 0
for i in range(len(s)-1, -1, -1):
    if s[i] == "\\" and l == 0:
        l = i
    elif s[i] == "\\":
        r = i+1
        break
print(s[r:l])
