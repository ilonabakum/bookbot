import sys
from stats import count_words, count_characters, sort_by_count

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_path = sys.argv[1]
        text = get_book_text(text_path)
        words_count = count_words(text)
        character_count = count_characters(text)
        sorted_characters = sort_by_count(character_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {text_path}...")
        print("----------- Word Count ----------")
        print(f"Found {words_count} total words")
        print("--------- Character Count -------")
        for dict in sorted_characters:
            print(f"{dict["char"]}: {dict["count"]}")
        print("============= END ===============")
    
main()