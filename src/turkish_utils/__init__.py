from typing import Literal
import typing


CONSONANTS = "BCÇDFGĞHJKLMNPRSŞTVYZ"
VOWELS = "AEIİOÖUÜ"

CONSONANTS_LOWER = "bcçdfgğhjklmnprsştvyz"
VOWELS_LOWER = "aeıioöuü"

CONSONANTS_FULL = CONSONANTS_LOWER + CONSONANTS
VOWELS_FULL = VOWELS_LOWER + VOWELS

LOWER_FULL = CONSONANTS_LOWER + VOWELS_LOWER
UPPER_FULL = CONSONANTS + VOWELS


def toUpper(input: str) -> str:
    return "".join(
        [
            LOWER_FULL.find(x) == -1 and x or UPPER_FULL[LOWER_FULL.find(x)]
            for x in input
        ]
    )


def toLower(input: str) -> str:
    return "".join(
        [
            UPPER_FULL.find(x) == -1 and x or LOWER_FULL[UPPER_FULL.find(x)]
            for x in input
        ]
    )


def classifyConsonantOrVowel(char: str) -> Literal["C", "V", None]:
    return char in CONSONANTS_FULL and "C" or char in VOWELS_FULL and "V" or None


def syllabilize(word: str) -> list[str]:
    """
    Raises:
        Exception: If a char cannot be found on the alphabet lists
    """

    cons_vowels = [classifyConsonantOrVowel(char) for char in word]
    error_chars = [word[idx] for (idx, val) in enumerate(cons_vowels) if val is None]

    if len(error_chars) > 0:
        raise Exception(
            f"Characters: [{error_chars}] cannot be found on the alphabet lists"
        )
    cons_vowels = typing.cast(list[str], cons_vowels)

    lst = []
    syllable = ""
    word_syllable = ""
    for idx, char in enumerate(cons_vowels):
        word_char = word[idx]
        # Start the syllable
        if syllable == "":
            syllable += char
            word_syllable += word_char
            continue

        # Last char
        # Match case below handles the edge cases with this
        if idx == len(word) - 1:
            lst.append(f"{word_syllable}{word_char}")
            break

        # We add to the syllable until there's at least one Vowel
        if "V" not in syllable:
            syllable += char
            word_syllable += word_char
            continue

        nextChar = cons_vowels[idx + 1]

        match char:
            case "V":
                lst.append(word_syllable)
                syllable = char
                word_syllable = word_char
            case "C":
                match nextChar:
                    case "V":
                        lst.append(word_syllable)
                        syllable = char
                        word_syllable = word_char
                    case "C":
                        syllable += char
                        word_syllable += word_char

    return lst
