english_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " ",
}


def english_to_morse(english_text):
    morse_text = ""
    for char in english_text:
        if char.upper() in english_dict:
            morse_text += english_dict[char.upper()] + " "
        else:
            pass

    return morse_text


morseText = english_to_morse("coding time")
print(morseText)
