import argparse
import logging

from gauss_jordan import (
    gauss_jordan,
    GaussJordanInvalidMatrixError,
    GaussJordanSingularMatrixError,
)


def create_parser():
    parser = argparse.ArgumentParser(
        description="Run tests for the Gauss-Jordan method algorithm"
    )
    parser.add_argument(
        "--coefficients",
        type=lambda x: list(
            map(
                lambda xr: [float(xc) for xc in xr.split(",")],
                [xr for xr in x.split(";")],
            )
        ),
        required=True,
        help="Matrix of coefficients, given as a flat list of real numbers separated by commas. "
        "Example for 2x2: 1,2,3,4 (interpreted as [[1, 2], [3, 4]])",
    )
    parser.add_argument(
        "--results",
        type=lambda x: [float(xe) for xe in x.split(",")],
        required=True,
        help="Results vector, given as a list of real numbers separated by commas. Example: 1,2",
    )
    parser.add_argument(
        "--show-steps",
        action="store_true",
        required=False,
        default=False,
        help="Show intermediate steps of the algorithm",
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    coefficients = args.coefficients
    results = args.results

    if args.show_steps:
        logging.basicConfig(level=logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("\n%(message)s\n"))
        log_handler = logging.getLogger()
        log_handler.handlers.clear()
        log_handler.addHandler(handler)
    try:
        output = gauss_jordan(coefficients, results)
    except GaussJordanInvalidMatrixError:
        print(
            "The number of lines of the coefficients matrix must be the same of the results"
        )
        return
    except GaussJordanSingularMatrixError:
        print("The determinant of the matrix must be different from 0")
        return
    print("Output:", output)


if __name__ == "__main__":
    main()
