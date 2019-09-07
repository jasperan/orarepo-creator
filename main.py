from random_word import RandomWords
import os

"""
@developer jasperan
"""


def main():
    r = RandomWords()
    words = list()
    words = r.get_random_words(maxLength=15, limit=2)
    print('Random words: ', words)
    composed_repository_name = 'orarepo'
    for item in words:
        composed_repository_name = composed_repository_name + '-' + item
    print('Composed repository name: ' + composed_repository_name)
    # Convert to lowercasxe
    composed_repository_name = composed_repository_name.lower()
    # Now, we will initialize the repository in Github using os.system
    #location = input('Please introduce the pwd where you want to create the repositories:')
    #os.system('cd ' + location)
    os.system('mkdir /home/jasper/git/%s' % composed_repository_name)
    os.system('cd /home/jasper/git/%s' % composed_repository_name)
    os.system('git init /home/jasper/git/%s' % composed_repository_name)
    os.system('touch /home/jasper/git/%s/README.md' % composed_repository_name)
    os.system('echo %s >> /home/jasper/git/%s/README.md' % (composed_repository_name, composed_repository_name))
    os.system('git add -A')
    os.system('git commit')
    os.system('git push --set-upstream origin master')
    #os.system('git remote add origin git@github.com/jasperan/%s' % composed_repository_name)
    os.system('git push')

if __name__ == '__main__':
    main()