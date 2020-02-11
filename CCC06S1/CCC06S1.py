def checkGene(gene1, gene2):
    possgene = []
    if gene1 == gene2:
        possgene.append(gene1[0])
        possgene.append(gene1[1])
        return list(dict.fromkeys(possgene))
    else:
        if gene1[0].islower() and gene2[0].isupper():
            possgene.append(gene2[0])
        if gene1[0].isupper() and gene2[0].islower():
            possgene.append(gene1[0])
        if gene1[1].islower() and gene2[1].isupper():
            possgene.append(gene2[1])
        if gene1[1].isupper() and gene2[1].islower():
            possgene.append(gene1[1])
        if gene1.isupper() and gene2.islower():
            possgene.append(gene1[0])
        else:
            possgene.append(gene2[0])
        
        return list(dict.fromkeys(possgene))

p1gene = input()
p2gene = input()
numbabies = int(input())
p1genes = [p1gene[i:i+2] for i in range(0, len(p1gene), 2)]
p2genes = [p2gene[i:i+2] for i in range(0, len(p2gene), 2)]
possgenes = ["a","b","c","d","e"]
possgenes[0] = checkGene(p1genes[0], p2genes[0])
possgenes[1] = checkGene(p1genes[1], p2genes[1])
possgenes[2] = checkGene(p1genes[2], p2genes[2])
possgenes[3] = checkGene(p1genes[3], p2genes[3])
possgenes[4] = checkGene(p1genes[4], p2genes[4])

within = False
k = 0
while k < numbabies:
    testgene = input()
    testgenes = [testgene[i:i+1] for i in range(0, len(testgene), 1)]

    n = 0
    while n < len(testgenes):
        if testgenes[n] in possgenes[n]:
            within = True
        else:
            within =  False
            break
        n+=1
    if within:
        print("Possible baby.")
    else:
        print("Not their baby!")
    k+=1