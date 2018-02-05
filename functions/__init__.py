from patterns import patterns_decision_tree , test_patterns
from sentence import sentence_translator , test_vocabulary


def one_sentence(sentence, test_vocabulary, test_patterns):
    st = sentence_translator(test_vocabulary)
    types, pramas = st.words_to_types_params(['保险股','市盈率','大于','32','并且','等于','pb'])
    pm = patterns_decision_tree(test_patterns)
    pm.save_pt_to_file("d:/test.model")
    patterns = pm.find_patterns(types, pramas, pm.patterns_tree)
    return patterns

print(one_sentence("测试",test_vocabulary,test_patterns))
