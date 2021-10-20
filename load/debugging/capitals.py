from enum import IntEnum
import json
import random
from typing import Dict, List


class YesNo(IntEnum):
    YES = 0
    NO = 1


CapitalsType = Dict[str, str]


def load_capitals(document_path: str) -> CapitalsType:
    with open(document_path) as f:
        return {capital["country"]: capital["capital"] for capital in json.load(f)}


def choose_random_country(countries: List[str]):
    return countries[random.randint(0, len(countries) - 1)]


def choose_candidate_capitals(capitals: CapitalsType, chosen_country: str) -> List[str]:
    other_capitals = [
        capital for country, capital in capitals.items() if country != chosen_country
    ]

    random.shuffle(other_capitals)
    other_capitals = other_capitals[:3]

    candidate_capitals = [capitals[chosen_country]] + other_capitals[:3]
    random.shuffle(candidate_capitals)

    return candidate_capitals


def play_once(countries: List[str], capitals: CapitalsType) -> bool:
    chosen_country = choose_random_country(countries)
    chosen_capital = capitals[chosen_country]
    candidate_capitals = choose_candidate_capitals(capitals, chosen_country)

    print(f"What is the capital of {chosen_country}?")

    for i, candidate_capital in enumerate(candidate_capitals):
        print(f"  {i + 1}. {candidate_capital}")

    selection = int(input("Enter you answer [1-4]: "))

    correct = candidate_capitals[selection - 1] == chosen_capital

    if correct:
        print("Well done!")
    else:
        print(f"Sorry. The capital of {chosen_country} is {chosen_capital}.")

    return correct


def check_continue() -> YesNo:
    yes = not input("Do you wish to play again? (Y/n) ").upper().startswith("N")

    return YesNo.YES if yes else YesNo.NO


def main() -> None:
    capitals = load_capitals("capitals.json")
    countries = list(capitals.keys())

    attempts = 0
    correct = 0

    playing = True

    while playing:
        if play_once(countries, capitals):
            correct += 1

        attempts += 1

        print(f"You have answered {correct} correctly out of {attempts}.")

        playing = check_continue() == YesNo.YES


if __name__ == "__main__":
    main()
