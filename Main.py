import time


with open("Hotdogs.txt", "r") as file:
    data = file.readlines()

records = []

for line in data:
    fields = line.strip().split(",")

    if len(fields) != 7:
        print("Invalid record:", line)
        continue

    try:
        fields[2] = int(fields[2])
        fields[3] = int(fields[3])
        fields[4] = int(fields[4])
        fields[5] = float(fields[5])
        fields[6] = int(fields[6])

        records.append(fields)
    except ValueError:
        print("Invalid numeric data:", line)
        continue

    


def linear_search(records, vendor_id):
    for record in records:
        if record[0] == vendor_id:
            return record
    return None


def binary_search(records, vendor_id):
    low = 0
    high = len(records) - 1

    while low <= high:
        middle = (low + high) // 2

        if records[middle][0] == vendor_id:
            return records[middle]

        elif records[middle][0] < vendor_id:
            low = middle + 1

        else:
            high = middle - 1

    return None

def bubble_sort(records):
    sorted_records = records.copy()

    for i in range(len(sorted_records)):
        for j in range(0, len(sorted_records) - i - 1):

            if sorted_records[j][0] > sorted_records[j + 1][0]:
                sorted_records[j], sorted_records[j + 1] = sorted_records[j + 1], sorted_records[j]

    return sorted_records


def quick_sort(records):
    if len(records) <= 1:
        return records

    pivot = records[len(records) // 2][0]

    left = []
    middle = []
    right = []

    for record in records:
        if record[0] < pivot:
            left.append(record)
        elif record[0] == pivot:
            middle.append(record)
        else:
            right.append(record)

    return quick_sort(left) + middle + quick_sort(right)

# this is for displaying the records in a formatted table
def display_records(records):
    print("Vendor ID | Vendor Name  | Week   | Vegan | Meat | Onions | Ketchup")
    print("-" * 70)

    for record in records:
        print(
            f"{record[0]:9} | "
            f"{record[1]:12} | "
            f"{record[2]:6} | "
            f"{record[3]:5} | "
            f"{record[4]:4} | "
            f"{record[5]:6} | "
            f"{record[6]:7}"
        )

def total_hotdogs_by_vendor(records, vendor_id):
    total = 0

    for record in records:
        if record[0] == vendor_id:
            total += record[3] + record[4]

    return total

def total_by_type(records):
    total_vegan = 0
    total_meat = 0

    for record in records:
        total_vegan += record[3]
        total_meat += record[4]

    return total_vegan, total_meat

def total_ketchup_by_vendor(records, vendor_id):
    total = 0

    for record in records:
        if record[0] == vendor_id:
            total += record[6]

    return total

def total_onions_by_vendor(records, vendor_id):
    total = 0

    for record in records:
        if record[0] == vendor_id:
            total += record[5]

    return total


def save_analysis(records):
    vegan_total, meat_total = total_by_type(records)

    dolly_total = total_hotdogs_by_vendor(records, "DD_056")
    korner_total = total_hotdogs_by_vendor(records, "KK_745")

    dolly_ketchup = total_ketchup_by_vendor(records, "DD_056")
    korner_ketchup = total_ketchup_by_vendor(records, "KK_745")

    dolly_onions = total_onions_by_vendor(records, "DD_056")
    korner_onions = total_onions_by_vendor(records, "KK_745")

    with open("HotdogsAnalysis.txt", "w") as file:
        file.write("Hotdog Vendor Analysis\n")
        file.write("======================\n\n")

        file.write(f"Vegan hotdogs: {vegan_total}\n")
        file.write(f"Meat hotdogs: {meat_total}\n\n")

        file.write(f"Dolly Dogs total hotdogs: {dolly_total}\n")
        file.write(f"Korner Kart total hotdogs: {korner_total}\n\n")

        file.write(f"Dolly Dogs ketchup: {dolly_ketchup} litres\n")
        file.write(f"Korner Kart ketchup: {korner_ketchup} litres\n\n")

        file.write(f"Dolly Dogs onions: {dolly_onions} kg\n")
        file.write(f"Korner Kart onions: {korner_onions} kg\n")

# Linear search for vendor_id "DD_056" and "XX_999"
search_result = linear_search(records, "DD_056")
print(search_result)

search_result = linear_search(records, "XX_999")
print(search_result)


sorted_records = sorted(records, key=lambda record: record[0])

print("Sorted Records:")

search_result = linear_search(sorted_records, "KK_745")
print(search_result)

search_result = binary_search(sorted_records, "KK_745")
print("Binary Search:", search_result)

search_result = binary_search(sorted_records, "XX_999")
print("Binary Search:", search_result)


bubble_sorted_records = bubble_sort(records)

print("Bubble Sort:")
display_records(bubble_sorted_records)


quick_sorted_records = quick_sort(records)

print("Quick Sort:")
display_records(quick_sorted_records)

print("Search Times:")

repetitions = 100000

start_time = time.perf_counter()
for i in range(repetitions):
    linear_search(records, "KK_745")
end_time = time.perf_counter()
print("Linear Search Unsorted:", end_time - start_time)

start_time = time.perf_counter()
for i in range(repetitions):
    linear_search(sorted_records, "KK_745")
end_time = time.perf_counter()
print("Linear Search Sorted:", end_time - start_time)

start_time = time.perf_counter()
for i in range(repetitions):
    binary_search(sorted_records, "KK_745")
end_time = time.perf_counter()
print("Binary Search Sorted:", end_time - start_time)



print("Sort Times:")

repetitions = 10000

start_time = time.perf_counter()
for i in range(repetitions):
    bubble_sort(records)
end_time = time.perf_counter()
print("Bubble Sort:", end_time - start_time)

start_time = time.perf_counter()
for i in range(repetitions):
    quick_sort(records)
end_time = time.perf_counter()
print("Quick Sort:", end_time - start_time)


print("Vendor Analysis:")

vegan_total, meat_total = total_by_type(records)

print("Vegan hotdogs:", vegan_total)
print("Meat hotdogs:", meat_total)


dolly_total = total_hotdogs_by_vendor(records, "DD_056")
korner_total = total_hotdogs_by_vendor(records, "KK_745")

print("Dolly Dogs total:", dolly_total)
print("Korner Kart total:", korner_total)

dolly_ketchup = total_ketchup_by_vendor(records, "DD_056")
korner_ketchup = total_ketchup_by_vendor(records, "KK_745")

print("Dolly Dogs ketchup:", dolly_ketchup)
print("Korner Kart ketchup:", korner_ketchup)

dolly_onions = total_onions_by_vendor(records, "DD_056")
korner_onions = total_onions_by_vendor(records, "KK_745")

print("Dolly Dogs onions:", dolly_onions)
print("Korner Kart onions:", korner_onions)

save_analysis(records)

print("Analysis saved to HotdogsAnalysis.txt")