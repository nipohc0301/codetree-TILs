Aage, Agen = input().split()
Bage, Bgen = input().split()
Aage, Bage = map(int, [Aage, Bage])

print(int((Aage >= 19 and Agen == "M") or (Bage >= 19 and Bgen == "M")))