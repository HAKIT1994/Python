
match = ["{}","()","[]"]
s="{[]}"

s2 = s
while s:

    for i in match:

        if i in s2:
            s2=s2.replace(i,"")
            print("s2:",s2)
            print("s:",s)
    if s2 == s:
        print("s2:", s2)
        print("s:", s)
        break
    if not s2:
        print("none")
        break
    s = s2
if  not s2:
   print("none")

print("done")
