#!/usr/bin/env python3
"""
Best Practice Example
"""


def main(dog_name):
    """
    This function takes in dog name and returns info about it.
    :param dog_name: string
    :return: string
    """
    print("This is the best!")
    print(dog_name)
    return "My dog is named" + dog_name


if __name__ == "__main__":
    main("Mudge")
