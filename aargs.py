import argparse


def parze():
    parser = argparse.ArgumentParser(description="Choose Yer Greeting")
    parser.add_argument("greeting", default="1", help="Pick 1 for 'hi', 2 for 'piratey hello'")
    parser.add_argument("-b", "--bye", default=False, action="store_true", help="Say Bye?")
    return parser.parse_args()


def say_hi():
    return "Hello there!"


def say_argh():
    return "Aarrgh! Ahoy ye mateys"


if __name__ == "__main__":
    args = parze()
    print(args)
    greeting = args.greeting
    # greeting = input("What greeting should we use?\n1: 'Hi'\n2: 'Piratey hello'\n")
    if greeting == '1':
        print(say_hi())
    elif greeting == '2':
        print(say_argh())
    if args.bye:
        print("See ya later alligator")
