class GardenError(Exception):
    """Custom error class for generic garden errors"""
    def __init__(self, message="A garden error occurred"):
        super().__init__(message)


class GardenManager():
    """ """
    class Plant():
        """"""
        def __init__(self, name: str, water_level: int, sunlight_hours: int):
            self.name = name
            self.water_level = water_level
            self.sunlight_hours = sunlight_hours


    def __init__(self):
        """ """
        self.plants: list = []


    def add_plant(self, plant: Plant):
        """ """
        if plant.name is None:
            raise GardenError("Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")


    def water_plants(self):
        """ """
        print("\nOpening watering system")
        try:
            for p in self.plants:
                print(f"Watering {p.name} - success")
        finally:
            print("Closing watering system (cleanup)")


    def check_plant_health(self, plant: Plant):
        """Checks if all arguments are valid
        and raises the appropriate error"""
        if plant.name is None:
            raise GardenError("Error: Plant name cannot be empty!")
        elif plant.water_level < 1:
            raise GardenError(
                f"Error: Water level {plant.water_level} is too low (min 1)"
                )
        elif plant.water_level > 10:
            raise GardenError(
                f"Error: Water level {plant.water_level} is too high (max 10)"
                )
        elif plant.sunlight_hours < 2:
            raise GardenError(
                f"Error: Sunlight hours {plant.sunlight_hours} is too low (min 2)"
                )
        elif plant.sunlight_hours > 12:
            raise GardenError(
                f"Error: Sunlight hours {plant.sunlight_hours} is too high (max 12)"
                )
        else:
            print(f"{plant.name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")


def test_garden_management():
    manager = GardenManager()
    tomato = manager.Plant("tomato", 5, 8)
    lettuce = manager.Plant("lettuce", 15, 8)
    null_plant = manager.Plant(None, 0, 0)

    print("Adding plants to the garden...")
    for p in (tomato, lettuce, null_plant):
        try:
            manager.add_plant(p)
        except GardenError as error:
            print(f"Error adding plant: {error}")

    print("Watering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    for p in (tomato, lettuce):
        try:
            manager.check_plant_health(p)
        except GardenError as error:
            print(f"Error checking {p.name}: {error}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")



if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
