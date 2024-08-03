from src.controller.screen import TypingTest
from src.controller.path import get_available_languages


def set_languages(screen: TypingTest):
    languages = get_available_languages()
    screen.combo_language.clear()
    screen.combo_language.addItems(languages)
