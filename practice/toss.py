import random
head = 0
tail = 0
total = 9000
for i in range (total):
    toss = random.randint(1,2)
    if(toss == 1):
        head += 1
    else:
        tail += 1
print("head = ",head,"Tail = ",tail)
print("Head percent = ",round((head*100)/total,2),"tail percent = ",round((tail*100)/total,2))