from stats import counterfunc, character_counter, final_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    # filepath = "books/frankenstein.txt"
    contents = get_book_text(sys.argv[1])
    # print(f"{counterfunc(contents)} words found in the document")
    # print(character_counter(contents))
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {counterfunc(contents)} total words\n--------- Character Count -------")
    for i in final_list(character_counter(contents)):
        for k, v in i.items():
            if k.isalpha():
                print(f"{k}: {v}")
    print("============= END ===============")

main()