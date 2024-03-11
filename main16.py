# Dictionary for converting Roman numerals to decimal numbers
numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
           'IV': 4, 'I': 1}


# Recursive function for converting Roman numerals to decimal numbers
def roman_to_int(roman):
    # Base case: if the string is empty, return 0
    if len(roman) == 0:
        return 0
    # If there's only one character left in the string, return its value
    elif len(roman) == 1:
        return numbers.get(roman[0], 'Ошибка: неверная римская цифра')
    else:
        # If the current character is less than the next one, subtract the current from the next
        if numbers.get(roman[0], 0) < numbers.get(roman[1], 0):
            if roman[0] + roman[1] in numbers:
                return numbers[roman[0] + roman[1]] + roman_to_int(roman[2:])
            else:
                return 'Ошибка: недопустимая комбинация римских цифр'
        # Otherwise, simply add the value of the current character
        else:
            return numbers[roman[0]] + roman_to_int(roman[1:])


# Main program function
def main():
    roman_numeral = input('Введите число римскими цифрами: ')
    result = roman_to_int(roman_numeral.upper())
    print(f"Десятичное число: {result}")


# Running the main function
if __name__ == "__main__":
    main()
