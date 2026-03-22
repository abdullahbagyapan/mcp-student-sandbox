from typing import List

def calculate_totals(data: List[float], multiplier: float = 1.15) -> List[float]:
    return [d * multiplier for d in data]

def format_totals(totals: List[float]) -> List[str]:
    return [f"Total: {val:.2f}" for val in totals]

def log_totals(totals: List[float], filename: str = "log.txt") -> None:
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def process_data(data: List[float]) -> List[float]:
    totals = calculate_totals(data)
    formatted = format_totals(totals)

    for line in formatted:
        print(line)

    log_totals(totals)
    return totals