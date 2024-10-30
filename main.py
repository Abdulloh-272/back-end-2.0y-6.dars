

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)  

set3 = {1, 2, 3}
set4 = {2, 3, 4}

intersection = set3.intersection(set4)
print(intersection)  

set_ = {1, 2, 3, 4}


number = int(input("Sonni kiriting: "))


set_.discard(number)
print(set_)  


set_ = {5, 1, 8, 7, 2}

min_value = min(set_)
max_value = max(set_)
print(min_value, max_value)  
