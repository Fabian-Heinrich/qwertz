def qwertz(felder):
    if len(felder) <= 1:
        print(felder[0])
        return felder[0]

    if (felder[0] < felder[1]):
        vergleichselement = felder[0]
    else:
        vergleichselement = felder[1]
    kleineElemente = []
    grosseElemente = []
    for i in range(0, len(felder), 1):
        if (felder[i] <= vergleichselement):
            kleineElemente.append(felder[i])
        else:
            grosseElemente.append(felder[i])
    return [qwertz(kleineElemente), qwertz(grosseElemente)]
     

test = [8,9,7,3,4,6,1,2,5]

a = qwertz(test)
