import random
import pyjokes

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    return reactions[random.randint(0, len(reactions) - 1)]


def print_random_joke_and_reaction():
    joke, reaction = pyjokes.get_joke(), get_random_reaction()
    print(joke, "\n", reaction)


if __name__ == "__main__":
    print_random_joke_and_reaction()
