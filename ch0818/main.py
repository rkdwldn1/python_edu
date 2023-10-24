# main

from morse_class import MoresCodeTranslator

morse_text = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
morse_translator = MoresCodeTranslator()
english_text = morse_translator.morse_to_english(morse_text)
print("english=", english_text)
