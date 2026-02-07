class CustomError(Exception):
    """Custom error class"""
    def __init__(self, message="An error occurred"):
        super().__init__(message)


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """Checks if all arguments are valid and raises the appropriate error"""
    if plant_name is None:
        raise CustomError("Error: Plant name cannot be empty!")
    elif water_level < 1:
        raise CustomError(
            f"Error: Water level {water_level} is too lowh (min 1)"
            )
    elif water_level > 10:
        raise CustomError(
            f"Error: Water level {water_level} is too high (max 10)"
            )
    elif sunlight_hours < 2:
        raise CustomError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
    elif sunlight_hours > 12:
        raise CustomError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """Tests check_plant_health()'s output
    for a regular call and each error case"""
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 2, 2)
    except CustomError as error:
        print(f"{error}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 2, 2)
    except CustomError as error:
        print(f"{error}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 2)
    except CustomError as error:
        print(f"{error}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 2, 0)
    except CustomError as error:
        print(f"{error}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
