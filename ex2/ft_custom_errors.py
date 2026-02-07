class GardenError(Exception):
    """Custom error class for generic garden errors"""
    def __init__(self, message="A garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    """Custom error class for plant-related errors"""
    def __init__(self, message="A plant-related error occurred"):
        super().__init__(message)


class WaterError(GardenError):
    """Custom error class for water-related errors"""
    def __init__(self, message="A wate-related error occurred"):
        super().__init__(message)


def trigger_plant_error():
    """Triggers the PlantError class at will"""
    raise PlantError("The tomato plant is wilting!")


def trigger_water_error():
    """Triggers the WaterError class at will"""
    raise WaterError("Not enough water in the tank!")


def test_errors():
    """Simulates custom errors"""
    print("=== Custom Garden Errors Demo ===")

    try:
        print("\nTesting PlantError...")
        trigger_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    try:
        print("\nTesting WaterError...")
        trigger_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for function in (trigger_plant_error, trigger_water_error):
        try:
            function()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
