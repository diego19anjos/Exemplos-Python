num = [2,5,9,1]
print(num)
num[2] = 3
print(num)
num.append(7) 
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

num.insert(2,0) 
print(num)
num.pop(2) 
print(num)
num.remove(2) 
print(num)
print(f'esta lista tem {len(num)} elementos')