data = [
    ('indic','pe','pe|市盈率'),
    ('indic','pb','pb|市净率'),
    ('class','tech','科技|技术|tech'),
    ('class','bank','银行|bank'),
    ('class','agric','农业|农产品'),
    ('operator','gte','大于等于|>='),
    ('operator','gt','大于|>'),
    ('operator','lte','小于等于|<='),
    ('operator','lt','大于|<'),
    ('adverb','and','且|并且'),
    ('adverb','or','或者|或')
]

patterns = [
    ('indic','operator','indic','fun1'),
    ('indic','operator','number','func1'),
    ('number','operator','indic','func1'),
    ('indic','operator','indic','adverb','operator','indic','func2'),
    ('indic','operator','number','adverb','operator','number','func2')
]


def patterns2dt(patterns):
    pass

def spilt_sentence(sentence):
    return None

def type_and_param_4word(word):
    for row in data:
        splited = row[2].split('|')
        for split in splited:
            if split and split in word:
                return row[0], row[1]
    if word.isnumeric():
        return 'number', float(word) 
    return None, None

def trans2types(words):
    types = []
    params = []
    for word in words:
        type_, param_ = type_and_param_4word(word)
        types.append(type_)
        params.append(param_)
    return tuple(types), tuple(params)

def find_sub_patterns(types):
    pass
