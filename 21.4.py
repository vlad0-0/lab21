s = input()
c = 0
a = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
for i in range(len(s)):
    for j in a:
        if s[i] == j:
            c += 1
            break
print(c)
