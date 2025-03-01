def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)

def get_character_count(book_contents):
    char_counts = {}
    book_contents = book_contents.lower()
    for char in book_contents:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def get_sorted_char_list(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    return sorted_list
