def length_conversion():
    print("\n=== Length Converter ===")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Meters")

    choice = input("Choose an option: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km = {km*1000} meters")
    elif choice == "2":
        m = float(input("Enter meters: "))
        print(f"{m} m = {m/1000} kilometers")
    elif choice == "3":
        m = float(input("Enter meters: "))
        print(f"{m} m = {m*100} centimeters")
    elif choice == "4":
        cm = float(input("Enter centimeters: "))
        print(f"{cm} cm = {cm/100} meters")
    else:
        print("Invalid option!")


def weight_conversion():
    print("\n=== Weight Converter ===")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")

    choice = input("Choose an option: ")

    if choice == "1":
        g = float(input("Enter grams: "))
        print(f"{g} g = {g/1000} kilograms")
    elif choice == "2":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {kg*1000} grams")
    elif choice == "3":
        lb = float(input("Enter pounds: "))
        print(f"{lb} lb = {lb*0.453592} kilograms")
    elif choice == "4":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {kg*2.20462} pounds")
    else:
        print("Invalid option!")


def temperature_conversion():
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose an option: ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {(c*9/5)+32}°F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F = {(f-32)*5/9}°C")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c}°C = {c + 273.15} K")
    elif choice == "4":
        k = float(input("Enter Kelvin: "))
        print(f"{k} K = {k - 273.15}°C")
    else:
        print("Invalid option!")


def main():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Choose the type of conversion: ")

        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            print("Exiting Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
