from random import choice

from enums.elements import game_elements
from lexicon.lexicon_ru import LEXICON_RU


async def define_game_result(user_element: str) -> str:
    bot_element = choice(game_elements)
    result = bot_element + '\n\n'

    rock = LEXICON_RU['rock']
    paper = LEXICON_RU['paper']
    scissors = LEXICON_RU['scissors']

    beats_other = {
        rock: scissors,
        paper: rock,
        scissors: paper
    }

    if user_element == bot_element:
        result += LEXICON_RU['tie']
    elif beats_other[user_element] == bot_element:
        result += LEXICON_RU['user_wins']
    else: 
        result += LEXICON_RU['bot_wins']

    return result + f'\n\n{LEXICON_RU['suggest_to_play']}'

