from stats import count_words, count_characters, sorted_character_count
import sys

def get_book_report(path_to_file):
  with open(path_to_file) as f:
    book_text = f.read()
    chars = count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    x = sorted_character_count(chars)
    for i in x:
      if i["char"].isalpha():
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  get_book_report(sys.argv[1])

main()
