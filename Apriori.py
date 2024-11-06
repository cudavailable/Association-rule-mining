
def create_C1(dataset):
	""" create an initial candidate set """
	C1 = set()
	for t in dataset:
		for item in t:
			item_set = frozenset([item]) # convert array into set
			C1.add(item_set)
	return C1

def is_apriori(Ck_item, Lksub1):
	for item in Ck_item:
		sub = Ck_item - frozenset([item])
		if sub not in Lksub1:
			# sub is not a k-1 frequent item
			return False

	return True

def create_Ck(Lksub1, k):
	""" create k-candidate set by Lk-1 """
	Ck = set()
	len_Lksub1 = len(Lksub1)
	list_Lksub1 = list(Lksub1)

	for i in range(len_Lksub1):
		for j in range(1, len_Lksub1):
			l1 = list(list_Lksub1[i])
			l2 = list(list_Lksub1[j])

			l1.sort()
			l2.sort()

			if l1[:k-2] == l2[:k-2]:
				new_l = list_Lksub1[i] | list_Lksub1[j]
				if is_apriori(new_l, Lksub1):
					Ck.add(new_l)

	return Ck

def generate_Lk_by_Ck(dataset, Ck, min_support, support_data):
	""" generate frequent item sets by candidate sets """
	Lk = set()
	item_count = {}
	for t in dataset:
		for item in Ck:
			if item.issubset(t):
				# count when item appears in t
				if item in item_count:
					item_count[item] += 1
				else:
					item_count[item] = 1

	t_num = float(len(dataset))
	for item in item_count.keys():
		# add items whose support >= min_support
		if item_count[item] / t_num >= min_support:
			Lk.add(item)
			support_data[item] = item_count[item] / t_num

	return Lk

def generate_L(dataset, k, min_support):
	""" generate all of frequent item sets and corresponding support """
	support_data = {} # save the support of different frequent items
	C1 = create_C1(dataset)
	L1 = generate_Lk_by_Ck(dataset, C1, min_support, support_data) # generate L1 by C1
	Lksub1 = L1.copy()
	L = []
	L.append(L1)

	for i in range(2, k+1):
		Ci = create_Ck(Lksub1, i)
		Li = generate_Lk_by_Ck(dataset, Ci, min_support, support_data)
		Lksub1 = Li.copy()
		L.append(Li)

	return L, support_data

def generate_big_rules(L, support_data, min_conf):
	""" generate strong-association-rules by frequent item sets """
	big_rules = []
	sub_set_list = []
	for i in range(len(L)):
		for freq_set in L[i]:
			for sub_set in sub_set_list:
				if sub_set.issubset(freq_set):
					conf = support_data[freq_set] / support_data[freq_set-sub_set]
					big_rule = (freq_set-sub_set, sub_set, conf, support_data[freq_set])
					if conf >= min_conf and (big_rule not in big_rules):
						big_rules.append(big_rule)
			sub_set_list.append(freq_set)

	return big_rules


dataset = [[1, 2], [1, 3], [1, 2, 4], [4], [1, 4]]

L, support_data = generate_L(dataset, 2, min_support=0.4)
print(L)
print(support_data)
big_rules = generate_big_rules(L, support_data, min_conf=0.6)
print(big_rules)
exit(0)
C1 = create_C1(dataset)
# for item in C1:
# 	print(item)
# print(C1)
support_data = {}
L1 = generate_Lk_by_Ck(dataset, C1, min_support=0.6, support_data=support_data)
print(L1)
print(support_data)
print("-------------")
C2 = create_Ck(L1, 2)
print(C2)
print("-------------")
L2 = generate_Lk_by_Ck(dataset, C2, min_support=0.2, support_data=support_data)
print(L2)
print(support_data)