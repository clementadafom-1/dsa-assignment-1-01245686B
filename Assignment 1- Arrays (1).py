"""Assignment 1: Arrays - University Course Registration Analytics."""


registrations = [
    1023, 1050, 1023, 1102,
    1050, 1023, 1201, 1102,
    1300, 1023,
]


def most_frequent_student(registration_list):
    """Return the student ID with the highest frequency, or None for an empty list."""
    if not registration_list:
        return None

    frequencies = {}
    most_frequent = registration_list[0]

    for student_id in registration_list:
        frequencies[student_id] = frequencies.get(student_id, 0) + 1

        if frequencies[student_id] > frequencies[most_frequent]:
            most_frequent = student_id

    return most_frequent


def ordered_deduplication(registration_list):
    """Remove duplicate student IDs while preserving first-appearance order."""
    seen = set()
    unique_registrations = []

    for student_id in registration_list:
        if student_id not in seen:
            seen.add(student_id)
            unique_registrations.append(student_id)

    return unique_registrations


def first_unique_student(registration_list):
    """Return the first student ID that occurs exactly once, or None if none exists."""
    frequencies = {}

    for student_id in registration_list:
        frequencies[student_id] = frequencies.get(student_id, 0) + 1

    for student_id in registration_list:
        if frequencies[student_id] == 1:
            return student_id

    return None


def subarray_sum_exists(registration_list, target):
    """Return True if any contiguous subarray has a sum equal to target."""
    prefix_sums = {0}
    running_sum = 0

    for student_id in registration_list:
        running_sum += student_id

        if running_sum - target in prefix_sums:
            return True

        prefix_sums.add(running_sum)

    return False


def run_tests():
    """Verify standard and edge cases for the array algorithms."""
    assert most_frequent_student(registrations) == 1023
    assert ordered_deduplication(registrations) == [1023, 1050, 1102, 1201, 1300]
    assert first_unique_student(registrations) == 1201
    assert subarray_sum_exists(registrations, 2224) is True

    assert most_frequent_student([]) is None
    assert ordered_deduplication([]) == []
    assert first_unique_student([]) is None
    assert subarray_sum_exists([], 0) is False

    assert most_frequent_student([7]) == 7
    assert ordered_deduplication([7]) == [7]
    assert first_unique_student([7]) == 7
    assert subarray_sum_exists([7], 7) is True

    assert first_unique_student([4, 4, 5, 5]) is None
    assert subarray_sum_exists([10, -3, 2, 1], 0) is True


def print_complexity_analysis():
    print("\nComplexity Analysis:")
    print("Most frequent student: O(n) time, O(n) space")
    print("Ordered deduplication: O(n) time, O(n) space")
    print("First non-repeated student: O(n) time, O(n) space")
    print("Subarray target sum check: O(n) time, O(n) space")


if __name__ == "__main__":
    run_tests()

    target = 2224

    print("Most frequent student:", most_frequent_student(registrations))
    print("Unique registrations:", ordered_deduplication(registrations))
    print("First non-repeated student:", first_unique_student(registrations))
    print("Subarray with target sum exists:", subarray_sum_exists(registrations, target))
    print_complexity_analysis()
