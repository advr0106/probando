def convert_to_roman(number):
    if not is_valid_input(number):
        return "You must introduce a positive number"
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    value = int(number)
    
    if value >= 5000:
        return "Number too large. Please enter a number equal to or less than 5000."
    else:
        for i in range(len(values)):
            while value >= values[i]:
                result += romans[i]
                value -= values[i]
    return result  
def is_valid_input(number):
    if number.isdecimal():
        return True
    else:
        return False
