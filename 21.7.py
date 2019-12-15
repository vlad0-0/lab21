s = list(input())
a = []
b = []
for i in range(len(s)):
    if i%2 == 0:
        b.append(s[i])
    else:
        a.append(s[i])
a.extend(reversed(b))
a = "".join(a)
print(a)
    
