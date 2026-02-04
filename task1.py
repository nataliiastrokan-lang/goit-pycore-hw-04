def total_salary(path: str) -> tuple:
    """
    Calculates total and average salary from a file.
    Returns integers.
    """
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                _, salary = line.split(",") # splitting data by comma in each line
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0)

        average = total // count   # ← to ensure average is an integer
        return (total, average)

    except FileNotFoundError:
        return (0, 0)
    except (ValueError, OSError):
        return (0, 0)
    

