# Course Registration Analytics

registrations = [
    1023, 1050, 1023, 1102,
    1050, 1023, 1201, 1102,
    1300, 1023
]

# 1. Most Frequent Registrant
def most_frequent_student(arr):
    freq = {}

    for student in arr:
        freq[student] = freq.get(student, 0) + 1

    return max(freq, key=freq.get)


# 2. Ordered Deduplication
def ordered_deduplication(arr):
    seen = set()
    result = []

    for student in arr:
        if student not in seen:
            seen.add(student)
            result.append(student)

    return result


# 3. First Unique Student
def first_unique_student(arr):
    freq = {}

    for student in arr:
        freq[student] = freq.get(student, 0) + 1

    for student in arr:
        if freq[student] == 1:
            return student

    return None


# 4. Contiguous Subarray Sum
def subarray_sum_exists(arr, target):
    prefix_sums = set()
    current_sum = 0

    for num in arr:
        current_sum += num

        if current_sum == target:
            return True

        if (current_sum - target) in prefix_sums:
            return True

        prefix_sums.add(current_sum)

    return False


# Example target
target = 2225

print("Most frequent student:", most_frequent_student(registrations))
print("Unique registrations:", ordered_deduplication(registrations))
print("First non-repeated student:", first_unique_student(registrations))
print("Subarray with target sum exists:",
      subarray_sum_exists(registrations, target))
