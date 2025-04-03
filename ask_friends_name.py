friends = []

# This will be used in my loop to get the name of each friend that I want
# to put in the list. I can start it will any value, as long as that value
# is not "end", otherwise, it won't ever go into the loop I made to gather
# the names.
name = None

while name != "end":
    name = input("Type the name of a friend: ")

    # Without this if statement, I would put "end" into my list as well
    if name != "end":
        friends.append(name)

print()
print("Your friends are:")
# This will print out each name in the list of friends
for friend in friends:
    print(friend)