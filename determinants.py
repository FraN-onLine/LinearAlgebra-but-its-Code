# determinant.py
# Simple Determinant Calculator (2x2 up to 5x5)
# Supports different methods:
# 0 - Diagonal Method (2x2 or 3x3 only)
# 1 - Determinant by Definition
# 2 - Using Determinant Rules (Row Operations)
# 3 - Cofactor Expansion

from fractions import Fraction
import copy


# -------------------------------------------------
# MATRIX INPUT
# -------------------------------------------------

def get_matrix():

    while True:
        size = int(input("Enter matrix size (2 to 5): "))
        if 2 <= size <= 5:
            break
        print("Size must be between 2 and 5.\n")

    Matrix = []

    print("\nEnter numbers row by row (separate with space):")

    for i in range(size):
        while True:
            row_input = input(f"Row {i+1}: ").split()

            if len(row_input) != size:
                print("Please enter exactly", size, "values.\n")
                continue

            # Convert everything to Fractions
            row = [Fraction(x) for x in row_input]
            Matrix.append(row)
            break

    return Matrix


# -------------------------------------------------
# PRINT MATRIX
# -------------------------------------------------

def print_matrix(Matrix):

    for row in Matrix:
        print("   ", [str(x) for x in row])
    print()


# -------------------------------------------------
# METHOD 0 — DIAGONALS (2x2 / 3x3)
# -------------------------------------------------

def det_diagonal(Matrix):

    n = len(Matrix)

    if n == 2:
        print("\nUsing 2x2 diagonal formula:")
        print("det = ad - bc\n")

        return Matrix[0][0]*Matrix[1][1] - Matrix[0][1]*Matrix[1][0]

    elif n == 3:
        print("\nUsing 3x3 Sarrus Rule (Diagonals Method)\n")

        a = Matrix

        positive = (
            a[0][0]*a[1][1]*a[2][2] +
            a[0][1]*a[1][2]*a[2][0] +
            a[0][2]*a[1][0]*a[2][1]
        )

        negative = (
            a[0][2]*a[1][1]*a[2][0] +
            a[0][0]*a[1][2]*a[2][1] +
            a[0][1]*a[1][0]*a[2][2]
        )

        print("Sum of downward diagonals =", positive)
        print("Sum of upward diagonals   =", negative)
        print()

        return positive - negative

    else:
        print("Diagonal method only works for 2x2 or 3x3.")
        return None


# -------------------------------------------------
# MINOR FUNCTION (for definition & cofactor)
# -------------------------------------------------

def get_minor(Matrix, row, col):

    return [
        r[:col] + r[col+1:]
        for i, r in enumerate(Matrix)
        if i != row
    ]


# -------------------------------------------------
# METHOD 1 — DETERMINANT BY DEFINITION
# (Recursive Expansion)
# -------------------------------------------------

def det_definition(Matrix):

    n = len(Matrix)

    if n == 1:
        return Matrix[0][0]

    if n == 2:
        return Matrix[0][0]*Matrix[1][1] - Matrix[0][1]*Matrix[1][0]

    total = Fraction(0)

    for col in range(n):

        sign = (-1) ** col
        minor = get_minor(Matrix, 0, col)

        total += sign * Matrix[0][col] * det_definition(minor)

    return total


# -------------------------------------------------
# METHOD 2 — USING DETERMINANT RULES
# (Row operations → Upper triangular)
# -------------------------------------------------

def det_rules(Matrix):

    A = copy.deepcopy(Matrix)
    n = len(A)
    determinant = Fraction(1)

    print("\nInitial Matrix:")
    print_matrix(A)

    for i in range(n):

        # If pivot is zero → swap rows (Property 3)
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    determinant *= -1
                    print(f"R{i+1} <-> R{k+1}    (Property 3: Row Swap)")
                    print_matrix(A)
                    break

        # If still zero → determinant is zero (Property 6)
        if A[i][i] == 0:
            print("Row of zeros detected. (Property 6)")
            return 0

        # Make zeros below pivot (Property 5)
        for j in range(i+1, n):

            factor = A[j][i] / A[i][i]

            if factor != 0:
                for k in range(n):
                    A[j][k] -= factor * A[i][k]

                print(f"{-factor}(R{i+1}) + R{j+1} -> R{j+1}    (Property 5)")
                print_matrix(A)

    print("Matrix is now upper triangular. (Property 7)\n")

    for i in range(n):
        determinant *= A[i][i]

    return determinant


# -------------------------------------------------
# METHOD 3 — COFACTOR EXPANSION
# -------------------------------------------------

def det_cofactor(Matrix):

    return det_definition(Matrix)


#strt rrprprpr

Matrix = get_matrix()

print("\nChoose Method:")
print("0 - Diagonal Method (2x2 or 3x3)")
print("1 - Determinant by Definition")
print("2 - Using Determinant Rules")
print("3 - Cofactor Expansion")

choice = int(input("\nChoice: "))

if choice == 0:
    result = det_diagonal(Matrix)

elif choice == 1:
    result = det_definition(Matrix)

elif choice == 2:
    result = det_rules(Matrix)

elif choice == 3:
    result = det_cofactor(Matrix)

else:
    print("Invalid choice.")
    result = None


if result is not None:
    print("\nDeterminant =", result)
