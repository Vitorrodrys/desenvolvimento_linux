import numpy as np
from scipy.linalg import solve
from gauss_jordan import gauss_jordan

def run_test(coefficients, results):
    """
    Run a single test case, comparing the results of gauss_jordan with scipy.linalg.solve
    """
    expected = solve(coefficients, results)
    output = gauss_jordan(coefficients, results)
    is_correct = np.allclose(expected, output)

    print("Coefficients:")
    print(np.array(coefficients))
    print("Results:")
    print(results)
    print("Expected:", expected)
    print("Output:  ", output)
    print("Correct:", is_correct)
    print("-" * 40)

    return is_correct

def main():
    """
    Run multiple test cases
    """
    test_cases = [
        # Test Case 1: Simple 2x2 system
        ([[2, 1], [1, 3]], [5, 6]),

        # Test Case 2: Simple 3x3 system
        ([[2, 1, 1], [1, 3, 2], [1, 0, 0]], [4, 5, 6]),

        # Test Case 3: 3x3 system with negative coefficients
        ([[3, 2, -4], [2, 3, 3], [5, -3, 1]], [3, 15, 14]),

        # Test Case 4: 3x3 system with fractional coefficients
        ([[1.5, 2.5, -1.5], [3.5, -0.5, 4.5], [5.5, -1.5, 3.5]], [6.5, 7.5, -8.5]),

        # Test Case 5: Larger 4x4 system
        ([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], [10, 18, 26, 34]),

        # Test Case 6: Identity matrix
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [1, 2, 3]),

        # Test Case 7: 2x2 system with decimals
        ([[1.2, 3.4], [5.6, 7.8]], [9.1, 10.2]),

        # Test Case 8: Singular matrix (determinant = 0)
        ([[1, 2, 3], [2, 4, 6], [3, 6, 9]], [6, 12, 18]),

        # Test Case 9: 5x5 random matrix
        (np.random.rand(5, 5).tolist(), np.random.rand(5).tolist()),

        # Test Case 10: 6x6 random matrix
        (np.random.rand(6, 6).tolist(), np.random.rand(6).tolist())
    ]

    all_tests_passed = True
    for i, (coefficients, results) in enumerate(test_cases):
        print(f"Test Case {i + 1}")
        try:
            passed = run_test(coefficients, results)
        except Exception as e:
            print("Test failed with exception:", e)
            passed = False
        all_tests_passed &= passed

    if all_tests_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. Please check the output for details.")

if __name__ == "__main__":
    main()
