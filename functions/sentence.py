
test_vocabulary = [
    ('indic','pe','pe|市盈率'),
    ('indic','pb','pb|市净率'),
    ('class','tech','科技|技术|tech'),
    ('class','bank','银行|bank'),
    ('class','agric','农业|农产品'),
    ('operator','gte','大于等于|>='),
    ('operator','gt','大于|>'),
    ('operator','lte','小于等于|<='),
    ('operator','lt','大于|<'),
    ('operator','eq','等于|='),
    ('adverb','and','且|并且'),
    ('adverb','or','或者|或')
]

class sentence_translator(object):

    def __init__(self,  vocabulary = [], **kw):
        self.vocabulary = vocabulary


    def type_and_param_for_word(self, word):
        for row in self.vocabulary:
            splited = row[2].split('|')
            for split in splited:
                if split and split in word:
                    return row[0], row[1]
        if word.isnumeric():
            return 'number', float(word) 
        return None, None

    def words_to_types_params(self, words):
        types = []
        params = []
        for word in words:
            type_, param_ = self.type_and_param_for_word(word)
            types.append(type_)
            params.append(param_)
        return types, params

