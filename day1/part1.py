f = open('input_day1', 'r');

lastMeasure = 0
increases = 0

for line in f:
    currentMeasure = int(line)
    if lastMeasure == 0:
        lastMeasure = int(currentMeasure)
        continue
    if lastMeasure < currentMeasure:
        print("Increase: " + str(currentMeasure - lastMeasure))
        increases += 1
    else:
        print("Decrease: " + str(lastMeasure - currentMeasure))
    lastMeasure = int(currentMeasure)

print(increases)
