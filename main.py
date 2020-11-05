import os
import json
import argparse
from googletrans import Translator
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', default='en', choices=['mn', 'en'], help='source language')
parser.add_argument('-d', '--dst', default='mn', choices=['mn', 'en'], help='destination language')
args = parser.parse_args()
translator = Translator()
def main():
    while True:
        files = os.listdir('./')
        if 'data_%s-%s.json'%(args.src, args.dst) not in files:
            data = {}
            with open('data_%s-%s.json'%(args.src, args.dst), 'w') as fp:
                json.dump(data, fp)
        with open('data_%s-%s.json'%(args.src, args.dst), 'r') as fp:
            data = json.load(fp)
        word = input('What word do you to translate (write in roman):').lower()
        if word in data:
            print('Your word translation is: ', data[word])
        else:
            translations = translator.translate(word, dest=args.dst)
            if type(translations) == 'NoneType':
                print('Sorry, No result from Google')
            else:
                print('Google translate result is: ',translations.text)
            confirm = input('Do you want to add word in dictionary (y/n):')
            if confirm == 'y':
                data[word] = translations.text
                print(data)
                with open('data_%s-%s.json'%(args.src, args.dst), 'w') as fp:
                    json.dump(data, fp)
        ends = input('Do you want to continue (y/n): ')
        if ends == 'y' or ends == 'yes':
            continue
        else:
            break
if __name__ == "__main__":
    main()
