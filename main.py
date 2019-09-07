from random_word import RandomWords
import os


def main():
    r = RandomWords()
    words = list()
    words = r.get_random_words(maxLength=15, limit=2)
    print('Random words: ', words)
    composed_repository_name = 'orarepo'
    for item in words:
        composed_repository_name = composed_repository_name + '-' + item
    print('Composed repository name: ' + composed_repository_name)
    # Now, we will initialize the repository in Github using os.system
    os.system('git init')
    os.system('')

if __name__ == '__main__':
    main()