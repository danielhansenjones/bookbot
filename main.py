import sys
from stats import *


def read_book(file_path):
    with open(file_path, encoding="utf-8") as f:
        book_contents = f.read()
    return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    book_contents = read_book(book_path)
    word_count = get_word_count(book_contents)
    print(f"Found {word_count} total words")
    print("--------- Character Count ------")

    character_count = get_character_count(book_contents)
    sorted_chars = get_sorted_char_list(character_count)

    print("\n--- Character Report ---")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")


if __name__ == "__main__":
    main()
