import random
from django.core.files.uploadedfile import InMemoryUploadedFile


def is_txt_file(file: InMemoryUploadedFile) -> bool:
    if file.content_type == "text/plain":
        True


def mix_word_letters(splitted_words: list[str]) -> str:
    words = []
    for word in splitted_words:
        if len(word) > 3:
            first_letter, last_letter = word[0], word[-1]
            rest_of_letters = word[1:-1]
            mixed_letters = "".join(
                random.sample(rest_of_letters, k=len(rest_of_letters))
            )
            word = f"{first_letter}{mixed_letters}{last_letter}"
            words.append(word)
        else:
            words.append(word)
    text = " ".join(words)
    return text
