def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"

def count_characters(book_text):
    character_dict = {}
    for char in book_text.lower():  # Convert once before the loop
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict






