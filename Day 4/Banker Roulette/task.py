import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friends_name = random.randint(1, 5)

if random_friends_name == 1:
    print(friends[0])
elif random_friends_name == 2:
    print(friends[1])
elif random_friends_name == 3:
    print(friends[2])
elif random_friends_name == 4:
    print(friends[3])
else:print(friends[4])


#simplified way to do it!
print(random.choice(friends))

#or this way
random_index = random.randint(1, 5)
print(friends[random_index])