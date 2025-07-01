def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    return "there has been a problem"


def get_word_count(TEXT):
    listOfWords = TEXT.split()
    wordCounts = len(listOfWords)
    return wordCounts
