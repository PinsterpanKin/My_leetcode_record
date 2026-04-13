def romanToInt(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total =0
    for i in range(len(s)):
        if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i-1]]:
            total += roman_numerals[s[i]] - 2 * roman_numerals[s[i-1]]
        else:
            total += roman_numerals[s[i]]
    return total