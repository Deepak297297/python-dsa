"""
	This simple code is to check if a given number is a poer of two or not.
		ex: 4 --> 2^2 --> 100 --> k = 2
			8 --> 2^3 --> 1000 --> k = 3
			16--> 2^4 --> 10000 --> k = 4
		
			n = 8 --> (1000)  , n-1 = 7 ---> (0111)
			n = 12 --> (1100)  , n-1 = 11 ---> (1011)
			performing bit (and) operation between both, then n&(n-1) = 1000
			
	Conclusion:

	NOTE:
		- Since Python considers 0 as "false", then we are gonna return the inversion of the result; i.e. return not(n&(n-1).
		- BUT If n = 0, the result will be zero indicating that 0 is a power of 2, wich is not true.
"""		
		

def pow_of_two(n):
  return(n and (not(n&(n-1))))

for i in range(20):
  if pow_of_two(i):
    print(f"{i} is a power of 2.")
  else:
    print(f"{i} is NOT a power of 2.")
