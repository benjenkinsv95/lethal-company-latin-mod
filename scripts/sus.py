# Define Latin words for numbers
units = ["", "ūnus", "duo", "trēs", "quattuor", "quīnque", "sex", "septem", "octō", "novem"]
tens = ["", "decem", "vīgintī", "trīgintā", "quadrāgintā", "quīnquāgintā", "sexāgintā", "septuāgintā", "octōgintā", "nōnāgintā"]
hundreds = ["", "centum", "ducenti", "trecenti", "quadringenti", "quingenti", "sescenti", "septingenti", "octingenti", "nongenti"]
thousands = ["", "mille", "duo milia", "tria milia"]

def int_to_roman(num):
    """Convert an integer to a Roman numeral."""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def capitalize_first_word(s):
    """Capitalize the first word in a string."""
    if not s:
        return s
    words = s.split()
    words[0] = words[0].capitalize()
    return " ".join(words)

def special_case(num):
    """Handle special cases for Latin numbers."""
    if num == 0:
        return "Nihil"

    m, c, t, u = num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10

    # Handling numbers 11-19 and those ending in 8 and 9 (except 98 and 99)
    if t == 1 or (t > 1 and u in [8, 9] and not (c == 0 and t == 9)):
        prefix = "duodē" if u == 9 else "ūndē"
        next_tens = tens[t + 1] if t < 8 else "centum"
        return f"{thousands[m]} {hundreds[c]} {prefix}{next_tens} {units[u]}".strip()

    # For numbers like 101, 201, 301, etc.
    if c > 0 and t == 0 and u == 1:
        return f"{thousands[m]} {hundreds[c]} et ūnus".strip()

    return ""

def number_to_latin(num):
    """Convert a number into its Latin word equivalent."""
    special_num = special_case(num)
    if special_num:
        return capitalize_first_word(special_num)

    m, c, t, u = num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10
    latin_num = f"{thousands[m]} {hundreds[c]} {tens[t]} {units[u]}".strip()
    return capitalize_first_word(latin_num)

def aureus_or_aurei(num):
    """Determine if 'aureus' should be singular or plural."""
    return "aureī" if num > 1 else "aureus"

def generate_translation_patterns(max_num, filename):
    """Generate translation patterns for numbers up to max_num and write to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(max_num + 1):
            roman = int_to_roman(i)
            latin_word = number_to_latin(i)
            aureus_plural = aureus_or_aurei(i)
            pattern = f'r:"^\\${i}$"=<size\=10>{roman} AU</size>\\n<size\=8>({latin_word} {aureus_plural})</size>\n'
            file.write(pattern)

# Generate patterns up to 3,999 and write to money.txt
generate_translation_patterns(3999, "money.txt")