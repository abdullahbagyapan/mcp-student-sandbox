def average_ratios(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty list")

    total = 0
    count = 0

    for n in numbers:
        if n == 0:
            continue  # skip zero safely
        total += 100 / n
        count += 1

    if count == 0:
        raise ValueError("No valid numbers (division by zero)")

    return total / count


if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))