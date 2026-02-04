def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"{temp_str} is not an integer")
    if temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0° C)")
    if temp > 40:
        raise ValueError(f"{temp} is too  for plants (max 40° C)")
    return temp


if __name__ == "__main__":
    i = check_temperature("a")
    print(f"{i}")