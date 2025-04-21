def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_letters(txt):
    dict = {}
    for l in txt:
        if l.lower() in dict:
            dict[l.lower()] += 1
        else:
            dict[l.lower()] = 1
    return dict