packages_delivered = int(input())
collisions = int(input())
total = packages_delivered * 50 - collisions * 10
if packages_delivered > collisions:
    total += 500
print(total)