def correct(x, y):
    if x == y:
        return True
    else:
        return False

inp = int(input())
sa = []
ca = []
correct = []
c = 0
i = 1
while i <= inp*2:
    if i<=inp:
        sa.append(input())
    elif i>=inp:
        ca.append(input())
    i+=1

i = 0
while i < len(sa):
    if sa[i] == ca[i]:
        correct.append(True)
    else:
        correct.append(False)
    i+=1
for k in correct:
    if k:
        c+=1
    
print(c)