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

def run_tests(tests):
    sucess = True
    for i, (coefs, results) in enumerate(tests):
        print(f"Test Case {i + 1}")
        try:
            sucess &= run_test(coefs, results)
        except Exception as e:  # pylint: disable=broad-except
            print("Error:", e)
            sucess = False
    return sucess

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

        # Test Case 5: Identity matrix
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [1, 2, 3]),

        # Test Case 6: 2x2 system with decimals
        ([[1.2, 3.4], [5.6, 7.8]], [9.1, 10.2]),
    ]

    if run_tests(test_cases):
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed. Please check the output for details.")

if __name__ == "__main__":
    main()
