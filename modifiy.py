import random
# generates a list with 20 random integers from 0 until 100
a = []
i = 0
while (i <20):
    n = random.randint(1,100)
    a.append(n)
    i += 1
# sorts a list in ascending order
a.sort()

    # creates and populates new list with given condition using for loop
b = []
i = 0

while(i < len(a)):
    if 35 < a[i] < 65:
        b.append(a[i])
        a.remove(a[i])
        i-=1
    i+= 1
b.sort()
print("a = ", a)
print("b = ", b)
