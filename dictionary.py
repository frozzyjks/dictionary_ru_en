from translate import Translator

# Указываем явно язык источника и целевой язык
translator = Translator(from_lang="ru", to_lang="en")

def translate_text(text: str) -> str:
    """
    Перевод текста с русского на английский.
    """
    try:
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print("Ошибка перевода:", e)
        return "Ошибка перевода"
