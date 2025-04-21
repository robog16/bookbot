from stats import count_words, count_letters

def get_book_text(file_path):
    with open(file_path, encoding='utf-8') as f:
        file_contents = f.read()
        return file_contents
    
# def main():
#     print(get_book_text('books/frankenstein.txt'))

# main()

book_text = get_book_text('books/frankenstein.txt')
letters = count_letters(book_text)

print(f'{count_words(book_text)} words found in the document')
print(letters)
