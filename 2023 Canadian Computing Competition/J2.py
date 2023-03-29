spiciness_dict = {
    'Poblano': 1500,
    'Mirasol': 6000,
    'Serrano': 15500,
    'Cayenne': 40000,
    'Thai': 75000,
    'Habanero': 125000,
}
num_peppers = int(input())
total_spiciness = 0
for _ in range(num_peppers):
    pepper = input()
    total_spiciness += spiciness_dict[pepper]

print(total_spiciness)