arr = [1,2,3,4,5,6]

##for loop
s1 = 0
for i in arr:
    s1 = s1 + i

##while loop
s2 = 0
i = 0
while i < len(arr):
    i += 1
    s2 = s2 + i
    
## recursion
l = len(arr) - 1
def s_(arr, l):
    if l == 0:
        return arr[l]
    else:
        return arr[l] + s_(arr, l - 1)

print(sum(arr))
print(s1)
print(s2)
print(s_(arr, l))
