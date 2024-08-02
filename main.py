def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_count = get_list_of_char_counts(text)
  print(f"There are {word_count} words in this text")
  report(char_count)

def sort_on(dict):
  return dict["value"]

def get_list_of_char_counts(text):
  char_list = []
  char_dict = {}
  lower_text = text.lower()
  for char in lower_text:
    if char.isalpha():
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1
  for key in char_dict:
    char_list.append({"char":key, "value": char_dict[key]})
  char_list.sort(reverse=True, key=sort_on)
  return char_list

def report(list):
  for item in list:
    print(f"The '{item["char"]}' character was found {item["value"]} times")


def get_word_count(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()