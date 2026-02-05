def get_cats_info(path: str) -> list:
    """
    Reads a file with cats data and returns a list of dictionaries.

    :param path: Path to the cats file
    :return: List of dictionaries with keys: id, name, age
    """
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                cat_id, name, age = line.split(",") #age remains string as in example

                cats.append(
                    {
                        "id": cat_id,
                        "name": name,
                        "age": age,
                    }
                )

    except (FileNotFoundError, ValueError, OSError):
        return []

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
