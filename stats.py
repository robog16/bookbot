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

def create_list_of_counts(dict):
    list_of_count = []
    for key, value in dict.items():
        letter_dict = {}
        letter_dict['letter'] = key
        letter_dict['count'] = value
        list_of_count.append(letter_dict)

    sorted_list_of_count = sorted(list_of_count, key=lambda item: item['count'], reverse=True)
    
    return sorted_list_of_count


