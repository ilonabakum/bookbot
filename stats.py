def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    dict = {}
    characters = "".join(set(book_text.lower()))
    book_text = book_text.lower()
    for character in characters:
        if character == " ":
            pass
        else:
            dict.update({character: book_text.count(character)})
    return dict

def sort_on(dict):
    return dict["count"]

def sort_by_count(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "count": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list