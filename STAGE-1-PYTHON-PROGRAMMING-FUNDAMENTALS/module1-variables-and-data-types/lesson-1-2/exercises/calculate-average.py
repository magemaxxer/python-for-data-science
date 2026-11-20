import statistics
import numpy

a = 4
b = 7
c = 6

print(statistics.mean([a,b,c]))

numbers = [11,3,6,7]
total = sum(numbers)
count= len(numbers)
average = total/count
print("The average of these numbers is:",average)

listofnum = [1,2,3,4]
avg = numpy.average(listofnum)
print('The average of this list is:',avg)