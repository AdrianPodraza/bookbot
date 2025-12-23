from stats import count_words
from stats import unique_chars
from stats import final
import sys
def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def print_report():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    count=count_words(book_text)
    unique=unique_chars(book_text)
    final_unique=final(unique)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in final_unique:
        print(f"{char['char']}: {char['num']}")
  
    print("============= END ===============")

def main():
    print_report()
   
main()