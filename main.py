from stats import count_words, count_letters, create_list_of_counts

def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
        return file_contents
    
# def main():
#     print(get_book_text('books/frankenstein.txt'))

# main()

book_text = get_book_text('books/frankenstein.txt')
letters = count_letters(book_text)

# print(f'{count_words(book_text)} words found in the document')
# print(letters)

final_list = create_list_of_counts(letters)

print(f'{" BOOKBOT ":=^33}')
print('Analyzing book found at books/frankenstein.txt...')
print(f'{" Word Count ":=^33}')
print(f'Found {count_words(book_text)} total words')
print(f'{" Character Count ":=^33}')

final_list = create_list_of_counts(letters)

for i in range(len(final_list)):
    if final_list[i]['letter'].isalpha() == True:
        print(f"{final_list[i]['letter']}: {final_list[i]['count']}")

print(f'{" END ":=^33}')



