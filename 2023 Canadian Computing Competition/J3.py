num_people = int(input())
availability = [input() for _ in range(num_people)]
best_days = []
best_availability = 0

for i in range(5):
    people_available = 0
    for person in availability:
        if person[i] == 'Y':
            people_available += 1
    
    if people_available > best_availability:
        best_days = [str(i + 1)]
        best_availability = people_available
    elif people_available == best_availability:
        best_days.append(str(i + 1))

print(','.join(best_days))