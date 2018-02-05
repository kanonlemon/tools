
test_patterns = [
    ('indic','operator','indic','fun1'),
    ('indic','operator','number','func1'),
    ('number','operator','indic','func1'),
    ('indic','operator','indic','adverb','operator','indic','func2'),
    ('class','indic','operator','number','adverb','operator','number','func2'),
    ('class','indic','operator','number','adverb','operator','indic','func2'),
    ('indic','operator','number','adverb','operator','indic','func2')
]
import json

class patterns_decision_tree(object):

    def __init__(self, patterns = [], **kw):
        self.patterns = patterns
        self.patterns_tree = {}
        if not self.patterns:
            print("patterns need to load, use function: load_patterns")
        else:
            self.patterns_tree = self.patterns_to_pt()
        
    def load_patterns(self, patterns=[]):
        self.patterns = patterns

    def patterns_to_pt(self):
        if not self.patterns :
            return {}
        pt = {}
        depth = 0
        max_depth = 0
        for pattern in self.patterns:
            max_depth = len(pattern) if len(pattern) > max_depth else max_depth 
        print("max depth : %d" % max_depth)
        for depth in range(max_depth):
            for pattern in self.patterns:
                if len(pattern) < depth:
                    #路径已经走完，不再处理
                    continue  
                else:
                    #路径还未走完，所以添加一个路径到原来的通路上
                    exec( "pt" + "['" + "']['".join(pattern[:depth + 1]) + "'] = {}")
        return pt

    def save_pt_to_file(self, file):
        with open(file, mode='w') as f:
            f.write(json.dumps(self.patterns_tree))
    
    def load_pt_from_file(self, file):
        with open(file) as f:
            self.patterns_tree = json.loads(f.readline())

    def isNode(self, tree, key):
        if key in tree and tree[key]:
            return True
        return False

    def isLeaf(self, tree, key):
        if key in tree and (not tree[key]):
            return True
        return False

    def find_patterns(self, types, params, pt):
        types_ = types
        types_.append('eod')
        patterns = []
        cur = pt
        st = 0
        for i in range(len(types_)):
            if self.isNode(cur, types_[i]) and i != len(types_):
                #如果包含子树并且没有到句尾，先进入子树，满足最大长度搜索
                cur = cur[types_[i]]
            else:
                #如果不包子树或者到句尾，则在当前树中找到执行方法
                for key in cur.keys():
                    if self.isLeaf(cur, key):
                        patterns.append((key, params[st:i] ))
                st = i + 1
                cur = pt        
        return patterns

