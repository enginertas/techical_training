#!/usr/bin/python

def removeDuplicates(old_list):
    no_set = set()
    new_list = []

    for num in old_list:
    	if num not in no_set:
    		no_set.add(num)
    		new_list.append(num)
    		
    return new_list


if __name__ == "__main__":
	lists = []
	lists.append([])
	lists.append([1])
	lists.append([-4, -4])
	lists.append([-7, -2, -2])
	lists.append([8, 0, 8, 7])
	lists.append([1, 5, 7, -2, 5, 5])
	lists.append([1, 4, 7, -2, 'a', 20, 2, 'a', 4, -2])
	lists.append([-2, -2, -2, -2, 'a', 20, -2, 'a', -2, -2])
	lists.append([11, 11, 11, 11, 11, 11, 11, 11, 11])

	for l in lists:
		print "--------------------------"
		print "List:"
		print l
		print "After duplicate removal: "
		print removeDuplicates(l)