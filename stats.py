
#  helps us get the book text by opening up the file and reading from it
#  will return there has been a problem if there was any issue
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    return "there has been a problem"



# gets the word count of TEXT
def get_word_count(TEXT):
    listOfWords = TEXT.split()
    wordCounts = len(listOfWords)
    return wordCounts



# counts each character with and stores it in a dictionary
def count_characters(TEXT):
    lowerCaseText = TEXT.lower()
    charactersCount = dict()
    # Counting loop
    
    # For each character
    for character in lowerCaseText:
        # If that character is already in charactersCount dictionary let's just increment its value
        if character in charactersCount:
            charactersCount[character] += 1 
        # Else if it is the first time this character came up and let's create a new key for it and initialize it with 1
        else:
            charactersCount[character] = 1
    
    # Return the dictionary
    return charactersCount


# print report just supply it with a filepath
def print_report(filepath):
    TEXT = get_book_text(filepath)
    wordCount = get_word_count(TEXT)
    charactersCount = count_characters(TEXT)



    reportTable = list()
    # Make the dictionary for every item we will make 2 key-value pairs
    for key in charactersCount:
        if key.isalpha():
            row = dict()
            row["char"] = key
            row["num"] = charactersCount[key]
            # add this to a dictionary that holds dictionary values
            reportTable.append(row)
    
    

    # printing
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    reportTable.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for row in reportTable:
        print(f"{row['char']}: {row['num']}")

# helper function for print report
def sort_on(items):
    return items["num"]