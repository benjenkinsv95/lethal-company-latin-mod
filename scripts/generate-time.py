def number_to_ordinal_neuter(number):
    # Dictionary to convert numbers to Latin ordinal neuter forms (1-60)
    ordinal_neuter_dict = {
        # Add entries for 1 through 60
        0: "Nūllum", 1: "Prīmum", 2: "Secundum", 3: "Tertium", 4: "Quartum", 5: "Quīntum", 
        6: "Sextum", 7: "Septimum", 8: "Octāvum", 9: "Nōnum", 10: "Decimum", 
        11: "Undecimum", 12: "Duodecimum", 13: "Tertiodecimum", 14: "Quartodecimum", 
        15: "Quīntumdecimum", 16: "Sextumdecimum", 17: "Septimumdecimum", 18: "Duodēvīcēsimum", 
        19: "Undēvīcēsimum", 20: "Vīcēsimum", 21: "Vīcēsimum\\nprīmum", 22: "Vīcēsimum\\nsecundum", 
        23: "Vīcēsimum\\ntertium", 24: "Vīcēsimum\\nquartum", 25: "Vīcēsimum\\nquīntum", 
        26: "Vīcēsimum\\nsextum", 27: "Vīcēsimum\\nseptimum", 28: "Duodētrīcēsimum", 
        29: "Undētrīcēsimum", 30: "Trīcēsimum", 31: "Trīcēsimum\\nprīmum", 32: "Trīcēsimum\\nsecundum", 
        33: "Trīcēsimum\\ntertium", 34: "Trīcēsimum\\nquartum", 35: "Trīcēsimum\\nquīntum", 
        36: "Trīcēsimum\\nsextum", 37: "Trīcēsimum\\nseptimum", 38: "Duodēquadrāgēsimum", 
        39: "Undēquadrāgēsimum", 40: "Quadrāgēsimum", 41: "Quadrāgēsimum\\nprīmum", 
        42: "Quadrāgēsimum\\nsecundum", 43: "Quadrāgēsimum\\ntertium", 44: "Quadrāgēsimum\\nquartum", 
        45: "Quadrāgēsimum\\nquīntum", 46: "Quadrāgēsimum\\nsextum", 47: "Quadrāgēsimum\\nseptimum", 
        48: "Duodēquīnquāgēsimum", 49: "Undēquīnquāgēsimum", 50: "Quīnquāgēsimum", 
        51: "Quīnquāgēsimum\\nprīmum", 52: "Quīnquāgēsimum\\nsecundum", 53: "Quīnquāgēsimum\\ntertium", 
        54: "Quīnquāgēsimum\\nquartum", 55: "Quīnquāgēsimum\\nquīntum", 56: "Quīnquāgēsimum\\nsextum", 
        57: "Quīnquāgēsimum\\nseptimum", 58: "Duodēsēxāgēsimum", 59: "Undēsēxāgēsimum", 60: "Sēxāgēsimum"
    }
    return ordinal_neuter_dict.get(number, "Invalid Number")

def number_to_ordinal_masculine(number):
    # Dictionary to convert numbers to Latin ordinal masculine forms (1-12)
    ordinal_masculine_dict = {
        1: "Prīma", 2: "Secunda", 3: "Tertia", 4: "Quarta", 5: "Quīnta",
        6: "Sexta", 7: "Septima", 8: "Octāva", 9: "Nōna", 10: "Decima",
        11: "Undecima", 12: "Duodecima"
    }
    return ordinal_masculine_dict.get(number, "Invalid Number")

def convert_period(period):
    # Convert AM/PM to Latin equivalent
    # return "Ante Merīdiem" if period == "AM" else "Post Merīdiem"
    return period

def generate_times():
    with open('times_output.txt', 'w', encoding='utf-8') as file:
        for hour in range(1, 13):
            for period in ["AM", "PM"]:
                latin_hour = number_to_ordinal_masculine(hour)
                latin_period = convert_period(period)

                for minute in range(0, 60):
                    latin_minute = f"Momentum</size>\\n<size\=11>{number_to_ordinal_neuter(minute)}"
                    formatted_time = f'<size\=14>Hora {latin_hour}\\n{latin_minute}{latin_period}</size>'
                    file.write(f'r:"^{hour}:\s*{str(minute).zfill(2)}\s*{period}"={formatted_time}\n')

# Generate times for all hours AM and PM and save to a file
generate_times()