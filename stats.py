def get_book_text(file):
  with open(file) as f:
    file_contents = f.read()

  return file_contents


def get_book_word_num(book):
  words_list = book.split()
  return (len(words_list))

def get_char_num(book):
  book_dictionary = {}
  book = book.lower()
 
  distinct_characters = set(book)
  for c in distinct_characters:
    book_dictionary[c] = book.count(c)
  return (book_dictionary)

def sort_on(items):
  return items["num"]

def sort_dictionary(book_dictionary):
  new_dictionary = {}
  dict_list = []
  for key in book_dictionary.keys():
    if (key.isalpha()):
      dict_list.append({"name" : key, "num" : book_dictionary[key]})

  dict_list.sort(reverse=True, key=sort_on)
  return dict_list