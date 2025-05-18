def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def count_characters(book_text):
    character_dict = {}
    for char in book_text.lower():  # Convert once before the loop
        if char.isalpha():  # Only process alphabetic characters
            if char not in character_dict:
                character_dict[char] = 1
            else:
                character_dict[char] += 1
    return character_dict

def sorted_list(character_dict):
    mylist = []
    for char, count in character_dict.items():
        mylist.append({"char": char, "count": count})
    sorted_list = sorted(mylist, reverse=True, key=lambda x: x["count"])
    return sorted_list

def print_book_report(num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")









