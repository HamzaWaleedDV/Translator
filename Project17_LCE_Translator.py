from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text(text, src_lang='auto', dest_lang='en'):
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

# Function to display available language codes
def display_languages():
    print("\nAvailable Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

print("Enhanced Translator CLI")
print("=======================")

while True:
    display_languages()
    src_lang = input("\nEnter the source language code (or 'auto' to detect automatically): ").strip()
    dest_lang = input("Enter the destination language code: ").strip()
    text = input("Enter the text to translate: ").strip()

    try:
        translated_text = translate_text(text, src_lang, dest_lang)
        print(f"\nTranslated Text: {translated_text}")
    except Exception as e:
        print(f"\nError: {e}")

    another = input("\nDo you want to translate another text? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print("\nThank you for using the translator CLI!")
