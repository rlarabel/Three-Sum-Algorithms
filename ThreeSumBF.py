#####################################
# Title: Three Sum Algorithm (Brute Force)
# Author: Ramses Larabel
# Class: Design and Analysis of Algorithms
# Description: This algorithm finds three integers in a list that can add to a desired integer. 
#	This solution will check every distinct set of 3 integers by using a triple nested loop. Taking each set one 
#	at a time to compare its sum to W. If they are equal the set is included in the results
# Inputs: Let A be a list of distinct random integers, let W be the number 3 elements in the list must sum to, and
#	let n be the # of integers in the list.
# Outputs: Let results be a 2D list, containing each of the distinct results: a list of the three integers that add to W.
# Time Complexity: O(n^3)
#######################################

import random 
import time

def main(n):
	A = random.sample(range(-1999*5,1999*5), n)
	W = 1999
	start_time = time.time()
	bruteForce(A, W, n)
	stop_time = time.time() - start_time
	print(stop_time, " seconds")
	return stop_time

def bruteForce(A, W, n):
	results = []
	for i in range(n-2):
		for j in range(i+1,n-1):
			for z in range(j+1, n):
				if W == A[i] + A[j] + A[z]:
					results.append([A[i], A[j], A[z]])
	return results

if __name__ == "__main__":
	n = 8000
	trials = 1
	avg_time = 0
	for i in range(trials):
		avg_time += main(n)
	avg_time /= trials
	print("Brute force average run time, ", avg_time, " seconds for ", n, "input size")