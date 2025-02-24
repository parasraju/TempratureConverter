def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def main():
    print("Temperature Converter")
    print("1. Kelvin to Celsius")
    print("2. Kelvin to Fahrenheit")
    print("3. Celsius to Kelvin")
    print("4. Celsius to Fahrenheit")
    print("5. Fahrenheit to Celsius")
    print("6. Fahrenheit to Kelvin")
    
    choice = int(input("Choose an option (1-6): "))
    temp = float(input("Enter the temperature: "))
    
    if choice == 1:
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
    elif choice == 2:
        print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
    elif choice == 3:
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == 4:
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    elif choice == 5:
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
    elif choice == 6:
        print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
    else:
        print("Invalid choice! Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
