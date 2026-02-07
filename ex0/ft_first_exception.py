def check_temperature(temp_str: str) -> int:
    """Tries to cast the temperature string to nd int
    and raises a different error for each condition"""
    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"{temp_str} is not an integer")

    if temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0° C)")
    if temp > 40:
        raise ValueError(f"{temp} is too  for plants (max 40° C)")
    return temp


def test_temperature_input():
    """Tests check_temperature()'s output in 4 different scenarios"""

    for temp in ("25", "abc", "100", "-50"):
        print(f"Testing temperature: {temp}")
        try:
            nbr = check_temperature(temp)
            print(f"Temperature {nbr}°C is perfect for plants!\n")
        except ValueError as error:
            print(f"Error: {error}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
