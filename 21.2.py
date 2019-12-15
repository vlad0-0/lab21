s = input().split()
c = len(s[0])
for i in range(len(s)):
    if len(s[i]) < c:
        c = len(s[i])
print(c)
