def garden_operations():
    try:
        i: int = 3 / 0
        int("abc")
    except ValueError:
        raise ValueError("Caught ValueError: invalid literal for int()")
    except ZeroDivisionError:
        raise ValueError("Caught ZeroDivisionError: division by zero")


def test_error_types():
    try:
        garden_operations()
    except ValueError as error:
        print("Testing ValueError...")
        print(f"{error}")
    except ZeroDivisionError as error:
        print("Testing ZeroDivisionError...")
        print(f"{error}")
    except ZeroDivisionError:
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file ")
    except KeyError:
        print("Testing KeyError...")
        #print("Caught KeyError: 'missing\_plant' ")
    #except MultipleError:
    #    print("Testing multiple errors together...")
    #    print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()