num_test_case=int(raw_input())

test_list=[]

# xrange returns an iterator and only keeps one number in memory at a time. range keeps the entire list of numbers in memory.

# n= range(0,num_test_case)

for  n in range(0,num_test_case):
	test_list.append(int(raw_input()))


for test in test_list:
	if test==0:
		print "NULL"
	elif test%2==0:
		if test>0:
			print "EVEN POSITIVE"
		else:
			print "EVEN NEGATIVE"
	else:
		if test>0:
			print "ODD POSITIVE"
		else:
			print "ODD NEGATIVE"		
										


