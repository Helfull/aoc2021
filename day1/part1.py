f = open('./day1/input_day1', 'r');

readings = [(int(l)) for l in f.readlines()];
print(sum([(readings[index-1] < readings[index]) for index in range(len(readings))]));
