scroreArray = []
for i in range(10):
    userInput = int(input("Enter number : "))
    scroreArray.append(i)

max_in_range = None
for g in scroreArray:
    if 15 <= g <= 20:
        if max_in_range is None or g > max_in_range:
            max_in_range = g

min_div3 = None
for g in scroreArray:
    if g % 3 == 0:
        if min_div3 is None or g < min_div3:
            min_div3 = g

sum_mid = 0
count_mid = 0
for g in scroreArray:
    if 10 <= g <= 15:
        sum_mid += g
        count_mid += 1

if count_mid > 0:
    avg_mid = sum_mid / count_mid
else:
    avg_mid = None

even_count = 0
for g in scroreArray:
    if g % 2 == 0:
        even_count += 1


print("\n--- result ---")

if max_in_range is not None:
    print(max_in_range)
else:
    print("not found number")

if min_div3 is not None:
    print(min_div3)
else:
    print("not found number")

if avg_mid is not None:
    print(avg_mid)
else:
    print("not found number")

print(even_count)