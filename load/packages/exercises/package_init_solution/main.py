from conversion import *


def main():
    print(f"3 km is {distance.km_to_miles(3):.2f} miles")
    print(f"3 kg is {weight.kg_to_lbs(3):.2f} lbs")
    print(f"100 deg C is {temperature.celsius_to_fahrenheit(100):.0f} deg F")


if __name__ == "__main__":
    main()
