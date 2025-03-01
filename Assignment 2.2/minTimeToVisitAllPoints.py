def minTimeToVisitAllPoints(points):
    steps=0
    x1,y1=points.pop()
    while points:
        x2,y2=points.pop()
        steps+=max(abs(x2-x1),abs(y2-y1))
        x1,y1= x2, y2

    return steps


#Alternate slution

def minTimeToVisitAllPoints(points):
    steps=0
    for i in range(len(points)-1):
        x1,y1= points[i]
        x2,y2 = points[i+1]
        steps+=max(abs(x2-x1),abs(y2-y1))

    return steps



            
