try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program execution complete.")
#######################################

def safe_divide(x, y):
    if y == 0:
        # Manually raise an exception
        raise ZeroDivisionError("Division by zero is not allowed!")
    return x / y

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = safe_divide(a, b)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Program execution complete.")
