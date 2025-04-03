import sys
from stats import get_num_words, get_char_count, sort_char_count

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    book_content = get_book_text(book_path)
    
    num_words = get_num_words(book_content)
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    
    char_dict = get_char_count(book_content)
    #print(char_dict)

    sorted_char_dicts = sort_char_count(char_dict)
    print("--------- Character Count -------")
    for pair in sorted_char_dicts:
        if pair["char"].isalpha():
            print(f'{pair["char"]}: {pair["count"]}')
    
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

if __name__ == "__main__":
    main()