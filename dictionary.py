# A dictionary stores (key, value) pairs,
# similar to a Map in Java or an object in Javascript
nums = {'cat': 2, 'person': 2, 'pig': 4}
print(nums['pig'])
print('cat' in nums)
print('cat' not in nums)
nums['fish'] = 0
print(nums)
print(nums.get('pig'))
del nums['fish']
print(nums)
print(nums.get('fish', 'NA'))
for key, value in nums.items():
    print('%s:%d' % (key, value))
