f = open('input_day1', 'r');

def sumReadings(readings, index):
    return sum(readings[index:index+3]);

readings = [(int(l)) for l in f.readlines()];

"""
loop the readings and sum the next three numbers
"""
lastGroupSum = 0;
increases = 0
for i in range(len(readings)):
    currentGroupSum = sumReadings(readings, i)
    if currentGroupSum > lastGroupSum & lastGroupSum != 0:
        print("increase: " + str(currentGroupSum))
        increases += 1
    lastGroupSum = currentGroupSum

print(increases)


