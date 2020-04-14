#Multiplication table from 1 to n
n = 12

print("       ",end="")

for i in range(1,n+1):
    print("%3d  " %i,end="")
print("\n  :-------",end="")
for i in range (1,n):
    print("-----",end="")
print("")

for i in range (1,n+1):
    print("%3d:   "%i,end="")
    for j in range(1,n+1):
        print("%3d  "%(i*j),end="")
    print("")