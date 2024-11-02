a = 5
s = a - 1
for k in range(0,a):
    for a in range(0,s):
        print(" ", end="")
    s -= 1
    for a in range(0, k + 1):
        print("* ", end="")
    print("")
