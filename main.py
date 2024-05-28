posArr = [(452, 852), (365,782 ), (328, 721), (492,799 )]
distArr = []
fMinDist = 0.0

def EuclideanDistance(posI,posII):
    xI, yI = posI
    xII, yII = posII
    distance = ((xII - xI) ** 2 + (yII - yI) ** 2) ** 0.5
    return distance

for i in range(len(posArr)):
    for j in range(i+1, len(posArr)):
        print(posArr[i], posArr[j])
        d = EuclideanDistance(posArr[i], posArr[j])
        distArr.append(d)

fMinDist = min(distArr)

print("Min Distance: ", fMinDist)
