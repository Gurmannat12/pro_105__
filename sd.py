import csv
import math
with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)
data = fileData[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)
    mean = total/n
    return mean

squarelist = []
for num in data:
    a = int(num)-mean(data)
    a = a**2
    squarelist.append(a)

sum = 0
for i in squarelist:
    sum = sum+i

result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)