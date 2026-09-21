n =13
m=4

def findcloset(n,m):
    closet = 0
    min_difference = float('int')

    for i in range(n-abs(m),n+abs(m)):
        if i% 3 ==0:
            difference = abs(n-i)