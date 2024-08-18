def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(f"Number of words: {count_words(file_contents)}")
    print(each_character_count(file_contents))

def count_words(file_contents):
    word_count = 0
    words = file_contents.split()
    for word in words:
        word_count +=1
    return word_count

def each_character_count(file_contents):
    count_dict = {}
    lowered_text = file_contents.lower()
    for character in lowered_text:
        if character.isalpha():
            if character in count_dict:
                count_dict[character] +=1
            else:
                count_dict[character] = 1
    return count_dict
main()