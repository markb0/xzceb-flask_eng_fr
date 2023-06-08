
"""
Module for translating text between English and French using the deep_translator library.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.

    Args:
        english_text (str): Text to translate.

    Returns:
        str: Translated text.
    """
    return MyMemoryTranslator(source='english', target='french').translate(english_text)

def french_to_english(french_text):
    """
    Translate French text to English.

    Args:
        french_text (str): Text to translate.

    Returns:
        str: Translated text.
    """
    return MyMemoryTranslator(source='french', target='english').translate(french_text)
