s = list(input())
f = ""
i = -1
while i < len(s):
    i += 1
    if i >= len(s):
        break
    if s[i] != " " and f == "":
        f = s[i]
        i += 1
        if i >= len(s):
            break
        while s[i] != " ":
            if s[i] == f:
                s[i] = "."
            i += 1
            if i >= len(s):
                break
        else:
            f = ""
print("".join(s))
