#!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frecuency of each character in the given file"""
    # Fist try to open the file
    try:
        f = open(filename)

    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()

    return characters


if __name__ == "__main__":

    print(character_frequency('test_file.txt'))
