l= [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
n = len(l)
#print the sum of the left diagonal
diagonal = 0
for i in range(n):
    diagonal += l[i][i]
print(diagonal)
#print the sum of the right diagonal
diagonal = 0
for j in range(n):
    diagonal += l[n-j-1][j]
print(diagonal)
#sort a list
m = ['g','v','r','t','y','e']
m.sort()
print(m)
