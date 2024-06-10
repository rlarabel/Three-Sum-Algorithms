######################################
# Title: Three Sum Algorithm (Divide and Conquer)
# Author: Ramses Larabel
# Class: Design and Analysis of Algorithms
# Description: This algorithm finds three integers in a list that can add to a desired integer. 
#	This solution starts by merge-sorting a list. A double nested loop calls a binary search tree method to look for 
#	the last value. If the last value needed is in the list it is returned, if not, null is returned. 
#	If the last value is not null, then add the 3 integers to the results
# Inputs: Let A be a list of distinct random integers, let W be the number 3 elements in the list must sum to, and
#	let n be the # of integers in the list.
# Outputs: Let results be a 2D list, containing each of the distinct results: a list of the three integers that add to W.
# Time Complexity: O(n^2*log(n))
#######################################

import random
import time

def main(n):
	# Creates random list of size n
	A = random.sample(range(-1999*5,1999*5), n)
	# The desired number to reach 
	W = 1999
	start_time = time.time()
	divideConquer(A, W, n)
	stop_time = time.time() - start_time
	print(stop_time, " seconds")
	return stop_time
def divideConquer(A, W, n):
	results = []
	A = mergeSort(A, n)
	for i in range(n-2):
		for j in range(i+1, n-1):
			third_sum = BST(A, W - (A[i]+A[j]), j+1, n-1)
			if third_sum != None:
				results.append([A[i], A[j], third_sum])
	return results

def mergeSort(A, n):
	if (n <= 0):
		return None
	elif (n == 1):
		return [A[0]]
	else:
		mid = int(n / 2)
		L = A[:mid]
		R = A[mid:]
		return merge(mergeSort(L, len(L)), mergeSort(R, len(R)))

def merge(L, R):
	A = [0 for _ in range(len(R) + len(L))]
	i = 0
	j = 0
	z = 0
	while i < len(L) and j < len(R):
		if L[i] <= R[j]:
			A[z] = L[i]
			i += 1
		else:
			A[z] = R[j]
			j += 1
		z += 1

	while i < len(L):
		A[z] = L[i]
		i += 1
		z += 1
	while j < len(R):
		A[z] = R[j]
		j += 1
		z += 1
	return A

def BST(A, k, low , high):
	if low > high:
		return None
	else:
		mid = int((low + high) / 2)
		if k == A[mid]:
			return A[mid]
		elif k < A[mid]:
			return BST(A, k, low, mid - 1)
		else:
			return BST(A, k, mid + 1, high) 

if __name__ == "__main__":
	n = 100
	trials = 5
	avg_time = 0
	for i in range(trials):
		avg_time += main(n)
	avg_time /= trials
	print("Divide and Conquer average run time, ", avg_time, " seconds for ", n, "input size")