allowed = set("ABCEHKMOPTXYP")
n = int(input())

for _ in range(n):
    s = input()
    ok = (
        len(s) == 6 and
        s[0] in allowed and
        s[1:4].isdigit() and
        s[4] in allowed and
        s[5] in allowed
    )
    print("Yes" if ok else "No")
