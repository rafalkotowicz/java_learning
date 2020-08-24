def fahrenheit_to_celsius(temps_f):
    temps_c = (temps_f - 32) * 5 / 9
    return round(temps_c, 2)


def celsius_to_fahrenheit(temps_c):
    temps_f = temps_c * 9 / 5 + 32
    return round(temps_f, 2)


def main():
    temperature, unit = input().split()
    print(
        f'{fahrenheit_to_celsius(int(temperature))} C' if unit == "F" else f'{celsius_to_fahrenheit(int(temperature))} F')
