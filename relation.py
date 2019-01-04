A = set()

R = [(1, 1), (1, 2), (2, 2), (2, 3)]

for i in R:
    for j in i:
        A.add(j)

def reflexive():
    counter = 0
    for a in A:
        if (a, a) in R:
            counter += 1
    if counter == len(A):
        return True

def symmetric():
    counter = 0
    counter2 = 0

    for (a, b) in R:
        if (b, a) in R and (b != a):
            counter += 1

    for (a, b) in R:
        if a == b:
            counter2 += 1

    required = len(R) - counter2

    if counter == required:
        return True

def transitive():
    x = 1
    for (a, b) in R:

        for j in R[x::]:
            if b == j[0]:
                chk = (a, j[1])
                if chk in R:
                    continue
                if chk not in R:
                    return False
            
        x += 1

    return True

def equivalence():
    if transitive() and symmetric() and reflexive():
        return True

def antiSymmetric():
    for (a,b) in R:
        if (b, a) in R and (b == a):
            return True

def asymmetric():
    for (a, b) in R:
        if (b, a) not in R:
            return True

def irreflexive():
    counter = 0
    for a in A:
        if (a, a) not in R:
            continue
        if (a, a) in R:
            return False

    return True


print("Relation is Reflexsive? " + str(reflexive()))
print("Relation is Symmetric? " + str(symmetric()))
print("Relation is Transitive? " + str(transitive()))
print("Relation is Equivalance? " + str(equivalence()))
print("Relation is Anti Symmetric? " + str(antiSymmetric()))
print("Relation is Asymmetric? " + str(asymmetric()))
print("Relation is Irreflexive? " + str(irreflexive()))
