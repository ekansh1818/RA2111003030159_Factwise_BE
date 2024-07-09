def maxScore(cardPoints,k):
    n=len(cardPoints)
    total_points=sum(cardPoints[:k])
    max_points=total_points
    for i in range(1,k+1):
        total_points=total_points-cardPoints[k-i]+cardPoints[-i]
        max_points=max(max_points,total_points)
    return max_points
cardPoints1=[1,2,3,4,5,6,1]
k1=3
print(maxScore(cardPoints1,k1))

cardPoints=list(map(int,input("Enter card points by spacing: ").split()))
k=int(input("Enter value of k: "))

result=maxScore(cardPoints,k)
print(result)