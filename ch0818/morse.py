# 모스부호 해독하기

mores_dict = {
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


def morse_to_english(mores_text):
    english_txt = ""
    morse_word = mores_text.strip().split(" ")
    for morse_word in morse_word:
        morse_chars = morse_word.split(" ")

        for morse_char in morse_chars:
            if morse_char in mores_dict:
                english_txt += mores_dict[morse_char]

            else:
                pass

        english_txt += " "
    return english_txt


english_txt = morse_to_english("-.-- --- ..-  .- .-. .  .-  --. . -. .. ..- ...")
print(english_txt)
