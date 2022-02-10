from functools import reduce
from curses.ascii import isalpha


def parse(source, dest):
    with open(source, 'rb') as f:
        res = bytes([c if isalpha(c) or c == 46 else 32 for c in f.read()]).decode('utf-8')
        word_list = [s.split(' ') for s in res.lower().split('.')]
        text = '\n'.join([' '.join(c for c in x if c != '') for x in word_list])

    with open(dest, 'w') as f:
        f.write(text)


def remove_stop_words(text):
    d = {'a', 'the', 'of', 'at', 'in', 'and', 'to'}
    return dict([(w.strip(), {text[:-1]}) for w in text.split(' ') if not w in d])


def merge_dict(x:dict, y:dict):
    for k in [*y]:
        x[k] = x.get(k, set([])).union(y[k])
    return x


def get_stats(source):
    with open(source, 'r') as f:
        list_d = [remove_stop_words(x) for x in f.readlines()]
        res = reduce(lambda x,y: merge_dict(x, y), list_d, {})
        stats = [(k, len(res[k]), sum(len(s) for s in res[k])/len(res[k])) for k in res]
        print('\n'.join([str(x) for x in stats]))


#parse('/Users/dstatz/Documents/temp/e1-data/sample.txt','/Users/dstatz/Documents/temp/e1-data/sample1.out')
get_stats('/Users/dstatz/Documents/temp/e1-data/sample1.out')
