import random

from django.core.files.uploadedfile import InMemoryUploadedFile


def is_txt_file(file: InMemoryUploadedFile) -> bool:
    return file.content_type == "text/plain"


def mix_words_letters(words: list[str]) -> str:
    text = " ".join([shuffle_middle_letters_in_word(word) for word in words])
    return text


def shuffle_middle_letters_in_word(word: str) -> str:
    if len(word) <= 3:
        return word
    first_letter, last_letter = word[0], word[-1]
    rest_of_letters = word[1:-1]
    if len(rest_of_letters) == rest_of_letters.count(rest_of_letters[0]):
        return word
    mixed_letters = "".join(random.sample(rest_of_letters, k=len(rest_of_letters)))
    while mixed_letters == rest_of_letters:
        mixed_letters = "".join(random.sample(rest_of_letters, k=len(rest_of_letters)))
    return f"{first_letter}{mixed_letters}{last_letter}"
