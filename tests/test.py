import sys
import os

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from solutions.solution import Solution, ListNode


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def run_test_case(input_list, val, expected_list, passed_count, total):
    total[0] += 1
    solution = Solution()

    # Build initial list
    head = None
    for item in reversed(input_list):  # to preserve original order
        head = solution.insertAtHead(head, item)

    # Insert at head
    head = solution.insertAtHead(head, val)
    actual = list_to_array(head)

    if actual == expected_list:
        passed_count[0] += 1
        print(f"\n✅ {passed_count[0]}")
    else:
        print("\n❌ Test failed for input:")
        print(f"Initial List: {input_list}, Insert Value: {val}")
        print(f"Actual: {actual}, Expected: {expected_list}")


# ✅ Main function to run all test cases
def main():
    passed_count = [0]
    total = [0]

    # ✅ Basic Cases
    run_test_case([], 1, [1], passed_count, total)
    run_test_case([1], 2, [2, 1], passed_count, total)
    run_test_case([1, 2, 3], 4, [4, 1, 2, 3], passed_count, total)
    run_test_case([10, 20], 30, [30, 10, 20], passed_count, total)

    # ✅ Edge Cases
    run_test_case([], -1, [-1], passed_count, total)
    run_test_case([0], 0, [0, 0], passed_count, total)
    run_test_case([5, 6, 7], 5, [5, 5, 6, 7], passed_count, total)
    run_test_case([-1, -2, -3], -4, [-4, -1, -2, -3], passed_count, total)
    run_test_case([999999], 888888, [888888, 999999], passed_count, total)
    run_test_case([1] * 5, 1, [1, 1, 1, 1, 1, 1], passed_count, total)

    # ✅ Summary
    print(f"\nPassed {passed_count[0]} / {total[0]} test cases!")

if __name__ == "__main__":
    main()
