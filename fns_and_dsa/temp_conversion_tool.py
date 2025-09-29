# fns_and_dsa/temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main execution flow
def main():
    try:
        # Ask the user for a temperature
        temp_input = input("Enter the temperature to convert: ")
        
        # Validate numeric input
        if not temp_input.replace('.', '', 1).isdigit() and not (
            temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()
        ):
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)

        # Ask the user whether input is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

# Run the script
if __name__ == "__main__":
    main()
