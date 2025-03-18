import string


def remove_punctuation(text: str = ""):
    return text.translate(str.maketrans("", "", string.punctuation))
