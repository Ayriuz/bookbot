# File: main.py
# --- a/file:///home/nix/codespace/github.com/Ayriuz/bookbotimport sys
import sys
from stats import get_word_count,get_character_count, sort_character_count   

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)         
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sort_character_count(character_count)
    print(f'============ BOOKBOT ============ \n')
    print(f'Analyzing book found at {book_path}...\n')
    print(f'----------- Word Count ---------- \n')
    print(f'Found {word_count} total words \n')
    print(f'------Character Count------ \n')
    for char, count in sorted_character_count:
        print(f'{char}: {count}')
    print(f'============= END =============== \n')

if __name__ == "__main__":
    main()
