def water_plants(plant_list: list):
    print("Opening watering system")

    try:
        for p in plant_list:
            if p is None:
                raise NameError
            print(f"Watering {p}")
    except NameError:
        print(f"Error: Cannot water {p} - invalid plant!")
        raise NameError
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===\n")

    p1: str = "tomato"
    p2: str = "lettuce"
    p3: str = "carrots"
    p4 = None

    print("Testing normal watering...")
    try:
        water_plants((p1, p2, p3))
    finally:
        print("Watering completed successfully!")

    print("\nTesting with error...")
    try:
        water_plants((p1, p4, p3))
    except NameError as error:
        print(f"{error}")
    finally:
        print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
