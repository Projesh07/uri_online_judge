##1067

# num_test_case=int(raw_input())


# for  n in range(0,num_test_case+1):
# 	if n%2 !=0:
# 		print n



##1066
# list_test=[]

# odd=0;
# even=0;
# pos=0;
# neg=0;
# for  n in range(0,5):
# 	list_test.append(int(raw_input()))


# for test in list_test:
# 	if test%2==0:
# 		even=even+1
# 		if test !=0:
# 			if test>0:
# 				pos=pos+1
# 			else:
# 				neg=neg+1
				
# 	else:
# 		odd=odd+1
# 		if test !=0:
# 			if test>0:
# 				pos=pos+1
# 			else:
# 				neg=neg+1

# print "{} valor(es) par(es)".format(even)
# print "{} valor(es) impar(es)".format(odd)
# print "{} valor(es) positivo(s)".format(pos)
# print "{} valor(es) negativo(s)".format(neg)

##1065

# list_test=[]

# even=0;

# for  n in range(0,5):
# 	list_test.append(int(raw_input()))


# for test in list_test:
# 	if test%2==0:
# 		even=even+1

# print "{} valores pares".format(even)


##1070


num_test_case=int(raw_input())
odd=0


for  n in range(num_test_case,num_test_case+(2*6),2):
	if n%2 ==0:
		odd=n+1
		print odd
	else:
		odd=n
		print odd	




		

			

	

