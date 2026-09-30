num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total_temp = 0.0

for i in range(num_days):
    temp = float(input())
    total_temp += temp

    if temp > danger_threshold:
        danger_days += 1

average_temp = total_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")
