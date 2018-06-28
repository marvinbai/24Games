# This program calculates 24 for 4 input numbers.
import sys

def calc(num1, num2, op):
	if op == 0:
		return num1 + num2
	elif op == 1:
		return num1 - num2
	elif op == 2:
		return num1 * num2
	elif op == 3:
		if num2 == 0:
			error('Divided by zero')
		else:
			return num1 / num2
	else:
		error('Invalid operation number.')
		
def run4digit(candidates, dict):
	## ((0 1) 2) 3
	for a in range(4):
		if a == 3 and candidates[1] == 0:
			continue
		res1 = calc(candidates[0], candidates[1], a)
		for b in range(4):
			if b == 3 and candidates[2] == 0:
				continue
			res2 = calc(res1, candidates[2], b)
			for c in range(4):
				if c == 3 and candidates[3] == 0:
					continue
				res3 = calc(res2, candidates[3], c)
				if abs(res3 - 24) < 0.01:
					if (a == 0 or a == 1) and (b == 2 or b == 3):
						print('('+str(int(candidates[0]))+dict[a]+str(int(candidates[1]))+')' \
						+dict[b]+str(int(candidates[2]))+dict[c]+str(int(candidates[3])))
					elif (b == 0 or b == 1) and (c == 2 or c == 3):
						print('('+str(int(candidates[0]))+dict[a]+str(int(candidates[1])) \
						+dict[b]+str(int(candidates[2]))+')'+dict[c]+str(int(candidates[3])))
					else:
						print(str(int(candidates[0]))+dict[a]+str(int(candidates[1])) \
						+dict[b]+str(int(candidates[2]))+dict[c]+str(int(candidates[3])))
					return True
	## (0 (1 2)) 3
	for a in range(4):
		if a == 3 and candidates[2] == 0:
			continue
		res1 = calc(candidates[1], candidates[2], a)
		for b in range(4):
			if b == 3 and res1 == 0:
				continue
			res2 = calc(candidates[0], res1, b)
			for c in range(4):
				if c == 3 and candidates[3] == 0:
					continue
				res3 = calc(res2, candidates[3], c)
				if abs(res3 - 24) < 0.01:
					print('('+str(int(candidates[0]))+dict[b]+'('+str(int(candidates[1])) \
					+dict[a]+str(int(candidates[2]))+'))'+dict[c]+str(int(candidates[3])))
					return True
	## 0 ((1 2) 3)
	for a in range(4):
		if a == 3 and candidates[2] == 0:
			continue
		res1 = calc(candidates[1], candidates[2], a)
		for b in range(4):
			if b == 3 and candidates[3] == 0:
				continue
			res2 = calc(res1, candidates[3], b)
			for c in range(4):
				if c == 3 and res2 == 0:
					continue
				res3 = calc(candidates[0], res2, c)
				if abs(res3 - 24) < 0.01:
					print(str(int(candidates[0]))+dict[c]+'(('+str(int(candidates[1]))+dict[a] \
					+str(int(candidates[2]))+')'+dict[b]+str(int(candidates[3]))+')')
					return True
	## (0 1) (2 3)
	for a in range(4):
		if a == 3 and candidates[1] == 0:
			continue
		res1 = calc(candidates[0], candidates[1], a)
		for b in range(4):
			if b == 3 and candidates[3] == 0:
				continue
			res2 = calc(candidates[2], candidates[3], b)
			for c in range(4):
				if c == 3 and res2 == 0:
					continue
				res3 = calc(res1, res2, c)
				if abs(res3 - 24) < 0.01:
					print('('+str(int(candidates[0]))+dict[a]+str(int(candidates[1]))+')'+dict[c] \
					+'('+str(int(candidates[2]))+dict[b]+str(int(candidates[3]))+')')
					return True
	## (0 (1 (2 3)))
	for a in range(4):
		if a == 3 and candidates[3] == 0:
			continue
		res1 = calc(candidates[2], candidates[3], a)
		for b in range(4):
			if b == 3 and res1 == 0:
				continue
			res2 = calc(candidates[1], res1, b)
			for c in range(4):
				if c == 3 and res2 == 0:
					continue
				res3 = calc(candidates[0], res2, c)
				if abs(res3 - 24) < 0.01:
					print('('+str(int(candidates[0]))+dict[c]+'('+str(int(candidates[1]))+dict[b] \
					+'('+str(int(candidates[2]))+dict[a]+str(int(candidates[3]))+')))')
					return True
	return False

if __name__ == '__main__':
	print("Please input four numbers separated by space...")
	nums = input().split(" ")
	# THere must be exact four numbers from input.
	if len(nums) != 4:
		print("Input must be FOUR numbers.")
		sys.exit()
	# Convert from string to float.
	for i in range(len(nums)):
		nums[i] = float(nums[i])
	# Construct dictionary for operatorsself.
	dict = {0:'+', 1:'-', 2:'*', 3:'/'}
	# Brutal force.
	set = set()
	candidates = [None] * 4 # Four numbers of different combinations.
	for i in range(4):
		candidates[0] = nums[i]
		set.add(i)
		for j in range(4):
			if j in set:
				continue
			candidates[1] = nums[j]
			set.add(j)
			for k in range(4):
				if k in set:
					continue
				candidates[2] = nums[k]
				set.add(k)
				for l in range(4):
					if l in set:
						continue
					candidates[3] = nums[l]
					set.add(l)
					if run4digit(candidates, dict) == True:
						sys.exit()
					set.remove(l)
				set.remove(k)
			set.remove(j)
		set.remove(i)
	print("Solution not found...")

	
	
	
