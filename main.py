from stats import get_book_text
from stats import get_book_word_num
from stats import get_char_num
from stats import sort_dictionary
import sys


def main():
  if (len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    file_path = sys.argv[1]
    content = get_book_text(file_path)
    num_words = get_book_word_num(content)
    book_dictionary = get_char_num(content)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    
    dict_list_sorted = sort_dictionary(book_dictionary)
    for dict in dict_list_sorted:
      print(f"{dict["name"]}: {dict["num"]}")

    print("============= END ===============")


main()