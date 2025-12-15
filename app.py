def square_pyramidal(n):
    if n <= 0:
        raise ValueError

    result = (n * (n + 1) * (2 * n + 1)) // 6
    return result

if __name__ == "__main__":
    print("result: ", square_pyramidal(5))