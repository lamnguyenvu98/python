def to_roman(value):
    roman = [
                ( 1000, "M" ),( 900, "CM" ), ( 500, "D" ),( 400, "CD" ),
                ( 100, "C" ),( 90, "XC" ), ( 50, "L" ),( 40, "XL" ),
                ( 10, "X" ),( 9, "IX" ), ( 5, "V" ),( 4, "IV" ), ( 1, "I" )
            ]
    result = ""
    for val, char in roman:
        while(value >= val):
            result += char
            value -= val
    return result

print(to_roman(14))
