from stats import count_words, count_characters

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    book_text = f.read()
    print(f"{count_words(book_text)} words found in the document")
    print(f"{count_characters(book_text)}")

def main():
  get_book_text('./books/frankenstein.txt')

main()
