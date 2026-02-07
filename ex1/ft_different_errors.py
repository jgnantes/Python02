def garden_operations():
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
        d = {"plant" : "ok"}
        d["missing_plant"]

    def multiple_errors():
        int(test)
        test2 = '2' + 2

    return [
        ("ValueError", value_error),
        ("ZeroDivisionError", zero_division_error),
        ("FileNotFoundError", file_not_found_error),
        ("KeyError", key_error),
        ("Multiple", multiple_errors),
    ]


def test_error_types():
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
        except (NameError, TypeError):
            print("Caught an error, but program continues!\n")


    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()