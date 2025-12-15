def square_pyramidal(n):
    if n <= 0:
        return "Число n має бути натуральним (більше 0)."

    result = (n * (n + 1) * (2 * n + 1)) // 6
    return result

if __name__ == "__main__":
    print(square_pyramidal(5))