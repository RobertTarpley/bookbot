import sys
from stats import count_words, count_characters, sorted_list, print_book_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_chars = sorted_list(char_dict)
    print_book_report(book_path, num_words, sorted_chars)

main()