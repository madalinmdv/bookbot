import sys

if len (sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Function to read the file contents and use it as a string in the file_contents variable

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# Importing a function - which check the word count in a specifc file

from stats import count_words

# Importing a function - which counts characters and stores them in a dictionary

from stats import character_count

# Importing a function - which takes the aforementioned dictionary and provides a list of sorted dictionaries

from stats import sorted_dictionaries

def main():
    file_contents = get_book_text(sys.argv[1])

    num_words = count_words(file_contents)
    individual_word_count = character_count(file_contents)
    dictionary_list = sorted_dictionaries(individual_word_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in dictionary_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
