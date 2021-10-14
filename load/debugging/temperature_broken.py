def to_fahrenheit(deg_c: float) -> float:
    return deg_c * 9.0 / 5.0 + 32.0


deg_c = input("What temperature do you wish to convert? ")
deg_f = to_fahrenheit(deg_c)

print(f"{deg_c} degC is {deg_f} degF.")