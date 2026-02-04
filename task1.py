def total_salary(path: str) -> tuple:
    """
    Calculates total and average salary from a file.

    :param path: Path to the salary file
    :return: Tuple (total_salary, average_salary)
    """
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                _, salary = line.split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total // count
        return total, average

    except (FileNotFoundError, ValueError, OSError):
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )
