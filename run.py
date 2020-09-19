# def _(func, items):
# 	i=0
# 	for item in items:
# 		if func(item):
# 			items[i] = item
# 			i+=1

# 	del items[i:]

# x = ["1", "7", "2"]
# print(sorted(x))

# def find_max(nums):
# 	max_num = float("-inf")
# 	for num in nums:
# 		if num >max_num:
# 			max_num +=num

# 	return max_num


# def reverse_list(elems):
# 	new = []
# 	for i in rangge(len(elems)):
# 		new.append(elems[len(elems)-1])

# 	return new

def func(a,b):
	a+=1
	b.push(1)
	return a,b
# end
a,b = 0, []
func(a,b)
