team_size = int(input("How many members? "))
for member in range(1, team_size + 1):
    name = input(f"Enter name for member {member}: ")
    print(f"Member {member}: {name}")