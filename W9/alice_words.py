import urllib.request
from collections import OrderedDict

book_url = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
data = urllib.request.urlopen(book_url)


def cal_word_occurrence():
    word_dict = OrderedDict()

    for line in data:
        for word in line.decode('utf-8').split():
            if not word.isalnum():
                continue

            clean_word = ''.join(filter(str.isalnum, word))

            if clean_word in word_dict:
                word_dict[clean_word] += 1

            else:
                word_dict[clean_word] = 1

    return OrderedDict(sorted(word_dict.items()))


def print2file(dictionary):
    file = open('alice_words.txt', 'w')

    for k, v in dictionary.items():
        file.write(str(k) + '\t' + str(v) + '\n')
        # file.write("Woops! I have deleted the content!")


if __name__ == "__main__":
    dict = cal_word_occurrence()
    print(dict)
    print2file(dict)
