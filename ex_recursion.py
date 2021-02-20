#for x in range(10):
#    for y in range(x):
#        print(y)
#print(y)



#for x in range(1, 10, 3):
#    print(x)



#def decade_counter():
#	while year < 50:
#		year += 10
#	return year

#print(decade_counter())




def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > 1:
				return_string += ","
			x = x - 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x + 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"





#def digits(n):
#	count = 0
#	if n == 0:
#	  count = 1
#	else:
#		count = len(str(n))
#	return count

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (int(n/10)>0):
		count += 1
		n = int(n/10)
	return count + 1


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1
