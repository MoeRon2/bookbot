from stats import get_word_count, get_book_text


def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    wordCount = get_word_count(book_text)
    print(f"{wordCount} words found in the document")

# call main
main()
