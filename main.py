def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    count_result = each_character_count(file_contents)
    sorted_result = dict_to_sorted_list(count_result)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print("")
    for key in sorted_result:
        print(
            f"The '{key['char']}' character was found {key['count']} times")
    print("--- End report ---")

def count_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
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

def dict_to_sorted_list(count_dict):
    count_list = []
    for char in count_dict:
        keys_dict = {}
        count = count_dict[char]
        keys_dict['char'] = char
        keys_dict['count'] = count
        count_list.append(keys_dict)
    def sort_on(keys_dict):
        return keys_dict['count']
    count_list.sort(reverse=True, key=sort_on)
    return count_list
main()