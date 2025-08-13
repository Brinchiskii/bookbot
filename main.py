import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_content = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at book {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(file_content)} total words")
    print("--------- Character Count -------")
    sorted_char_list = get_sorted_dict(get_character_count(file_content))
    
    for item in sorted_char_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item["num"]}")
    print("============= END ===============")
    

main()
