f = open('./day1/input_day1', 'r');

def sumReadings(readings, index):
    return sum(readings[index:index+3]);

readings = [(int(l)) for l in f.readlines()];
print(sum([(sumReadings(readings, i) < sumReadings(readings, i+1)) for i in range(len(readings)-2)]));

