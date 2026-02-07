def garden_operations() -> list:
    """Defines a function for each error case and returns a list
    of tuples containing their respective labels and callables"""
    def value_error():
        int("abc")

    def zero_division_error():
        3 / 0

    def file_not_found_error():
        file = "missing.txt"
        try:
            open(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"No such file {file}")

    def key_error():
        d = {"plant": "ok"}
        d["missing_plant"]

    def multiple_errors():
        test = '2' + 2
        int(test)

    return [
        ("ValueError", value_error),
        ("ZeroDivisionError", zero_division_error),
        ("FileNotFoundError", file_not_found_error),
        ("KeyError", key_error),
        ("Multiple", multiple_errors),
    ]


def test_error_types():
    """Tests all errors in order"""
    print("=== Garden Error Types Demo ===\n")

    for label, op in garden_operations():
        try:
            if label != "Multiple":
                print(f"Testing {label}")
            else:
                print("Testing multiple errors together")
            op()
        except ValueError as error:
            print(f"Caught ValueError: {error}\n")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}\n")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}\n")
        except KeyError as error:
            print(f"Caught KeyError: {error}\n")
        except (ValueError, TypeError):
            print("Caught an error, but program continues!\n")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
