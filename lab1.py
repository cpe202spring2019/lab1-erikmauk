
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   if int_list == None:
   	raise ValueError
   elif len(int_list) == 0:
   	return None
   else:
   	maxNum = int_list[0]
   	for i in range(len(int_list)):
   		if int_list[i] > maxNum:
   			maxNum = int_list[i]

   return maxNum

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
   	raise ValueError
   if len(int_list) == 0:
   	return int_list
   else:
   	return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
   	raise ValueError

   if low > high:
   	return None

   midpoint = (low + high) // 2

   if int_list[midpoint] == target:
   	return midpoint

   if int_list[midpoint] < target:
   	return bin_search(target, midpoint+1, high, int_list)
   	
  	if int_list[midpoint] > target:
   	return bin_search(target, low, midpoint-1, int_list)

