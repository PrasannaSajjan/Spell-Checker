import re, collections
def words(text): return re.findall('[a - z] + ', text.lower())
def train(features):
    model = collections.defaultdict(lambda: 1)
for f in features:
    model[f] += 1
return model
SOURCE = train(words(open('/home/psajjan/pyf/big.txt').read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def d1(word):
    splits = [(word[: i], word[i: ]) for i in range(len(word) + 1)]
deletes = [a + b[1: ]
    for a, b in splits
    if b
]
transposes = [a + b[1] + b[0] + b[2: ]
    for a, b in splits
    if len(b) > 1
]
replaces = [a + c + b[1: ]
    for a, b in splits
    for c in alphabet
    if b
]
inserts = [a + c + b
    for a, b in splits
    for c in alphabet
]
return set(deletes + transposes + replaces + inserts)
def d2(word):
    return set(e2
        for e1 in d1(word) for e2 in d1(e1) if e2 in SOURCE)
def known(words): return set(w
    for w in words
    if w in SOURCE)
def spellcheck(word):
    candidates = known([word]) or known(d2(word)) or d2(word) or[word]
return max(candidates, key = SOURCE.get)