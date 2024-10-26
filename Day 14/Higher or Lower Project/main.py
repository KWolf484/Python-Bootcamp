from game_data import data
import random
# 'name':
# 'follower_count':
# 'description':
# 'country':
#randomally chose two(2) entries from data list
#have player guess which has higher follow count (A) and (B)
#if player is correct, score one(1) point
#have entry (B) become entry (A)

A = random.randint(0,len(data))
B = random.randint(0,len(data))

print(A, B)
details = data[A]("name", "description", "country")
print(details)
#print(data[0]list([0,2,3]))
