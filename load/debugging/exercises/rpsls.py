from enum import IntEnum
import random


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


def parse_action(text):
    actions = {
        "R": Action.Rock,
        "P": Action.Paper,
        "S": Action.Scissors,
        "L": Action.Lizard,
        "K": Action.Spock,
    }

    return actions[text]


def get_user_action():
    action = None

    while action is None:
        input_text = (
            input("Enter a choice ([R]ock, [P]aper, [S]cissors, [L]izard or Spoc[K]): ")
            .strip()
            .upper()
        )

        if len(input_text) > 0 and input_text[0] in "RPSLK":
            action = parse_action(input_text[0])

    return action


def get_computer_action():
    return Action(random.randint(0, len(Action) - 1))


def determine_action_winner(action_1, action_2):
    print(action_1, action_2)

    if (action_1, action_2) == (Action.Rock, Action.Scissors):
        return "Rock blunts scissors!"
    elif (action_1, action_2) == (Action.Rock, Action.Lizard):
        return "Rock smashes lizard!"
    elif (action_1, action_2) == (Action.Paper, Action.Rock):
        return "Paper covers rock!"
    elif (action_1, action_2) == (Action.Paper, Action.Spock):
        return "Paper disproves Spock!"
    elif (action_1, action_2) == (Action.Scissors, Action.Paper):
        return "Scissors cut paper!"
    elif (action_1, action_2) == (Action.Scissors, Action.Lizard):
        return "Scissors decapitate lizard!"
    elif (action_1, action_2) == (Action.Lizard, Action.Paper):
        return "Lizard eats paper1"
    elif (action_1, action_2) == (Action.Lizard, Action.Spock):
        return "Lizard poisons Spock!"
    elif (action_1, action_2) == (Action.Spock, Action.Rock):
        return "Spock vapourises rock!"
    elif (action_1, action_2) == (Action.Spock, Action.Scissors):
        return "Spock smashes scissors!"
    else:
        return None


def determine_outcome(user_action, computer_action):
    if user_action == computer_action:
        return ("Tie!", False)

    user_won = determine_action_winner(user_action, computer_action)

    if user_won:
        return (f"{user_won} You win!", True)

    computer_won = determine_action_winner(computer_action, user_action)

    if computer_won:
        return (f"{computer_won} You lose. :(", False)

    assert False, "Indeterminent outcome"


def determine_whether_quit():
    return (
        input("Would you like to play another round? (Y/n): ")
        .strip()
        .upper()
        .startswith("N")
    )


def play_round():
    user_action = get_user_action()
    computer_action = get_computer_action()
    message, user_won = determine_outcome(user_action, computer_action)

    print(message)

    return user_won


def play():
    rounds_played = 0
    rounds_won = 0

    quit = False

    while not quit:
        user_won = play_round()

        rounds_played += 1

        if user_won:
            rounds_won += 1

        print(f"You have won {rounds_won} out of {rounds_played} round(s).")

        quit = determine_whether_quit()


def main():
    play()


if __name__ == "__main__":
    main()
