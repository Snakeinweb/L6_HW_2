

x = int (input ())
k = 0
for y in range (1, x + 1):
    if x % y == 0:
        k += 1
print (k) 
