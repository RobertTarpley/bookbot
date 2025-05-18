from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    result = count_words(book_text)
    print(result)

main()