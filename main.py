import matplotlib.pyplot as plt

from map_reduce import map_reduce
from get_text import get_text
from utiles import remove_punctuation


TEXT_URL = "https://gutenberg.net.au/ebooks01/0100021.txt"


def visualize_top_words(word_counts, top_n=10):
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = sorted_word_counts[:top_n]

    words, counts = zip(*top_words)

    plt.figure(figsize=(10, 5))
    plt.barh(words[::-1], counts[::-1], color="skyblue")
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.show()


if __name__ == "__main__":
    text = get_text(TEXT_URL)

    if text:
        text = remove_punctuation(text)

        result = map_reduce(text)

        visualize_top_words(result)
    else:
        print("Помилка: Не вдалося отримати вхідний текст.")
