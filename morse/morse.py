class MorseCodeTranslator:
    def __init__(self):
        self.morse_dict = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            " ": "",
        }
        self.eng_dict = {value: key for key, value in self.morse_dict.items()}

    def morse_to_eng(self, morse_text):
        eng_text = ""
        morse_words = morse_text.strip().split("  ")
        for morse_word in morse_words:
            morse_chars = morse_word.split(" ")

        for morse_char in morse_chars:
            if morse_char in self.morse_dict:
                eng_text += self.morse_dict[morse_char]
            else:
                pass
            eng_text += " "

        eng_text += " "
        return eng_text

    def eng_to_morse(self, eng_text):
        morse_text = ""
        for char in eng_text:
            if char.upper() in self.eng_dict:
                morse_text += self.eng_dict[char.upper()] + " "
            else:
                pass
        return morse_text


morse_translator = MorseCodeTranslator()
