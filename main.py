from stats import count_words, count_characters, sorted_list, print_book_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_chars = sorted_list(char_dict)
    print_book_report(num_words, sorted_chars)

main()