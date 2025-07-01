from stats import get_word_count, get_book_text, count_characters, print_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print_report(filepath)

# call main
main()
