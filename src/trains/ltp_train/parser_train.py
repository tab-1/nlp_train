# -*- coding: utf-8 -*-
import sys
import os
# from nltk.tree import Tree    #导入nltk tree结构
# from nltk.grammar import DependencyGrammar  #导入依存句法包
from nltk.parse import *
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser

import importlib
importlib.reload(sys)

current_file_path = os.path.abspath(__file__)
ltp_train_path = os.path.dirname(current_file_path)
trains_path = os.path.dirname(ltp_train_path)
src_path = os.path.dirname(trains_path)
project_path = os.path.dirname(src_path)
cws_model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/cws.model")
user_dict = os.path.join(project_path, "models/ltp_data_v3.4.0/fulluserdict.txt")
pos_model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/pos.model")
parser_model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/parser.model")

sent = "欧洲东部的罗马尼亚，首都是布加勒斯特，也是一座世界性的城市。"

segmentor = Segmentor() # 实例化分词模块
segmentor.load_with_lexicon(cws_model_path, user_dict)
words = segmentor.segment(sent)


postagger = Postagger()  # 实例化词性标注类
postagger.load(pos_model_path)
postags = postagger.postag(words)


parser = Parser()  # 句法解析
parser.load(parser_model_path)
arcs = parser.parse(words, postags)
arclen = len(arcs)
print("len(arcs): {}".format(arclen))

conll = ""
for i in range(arclen):  # 构建Conll标准的数据结构
    if arcs[i].head == 0:
        arcs[i].relation = "ROOT"
    conll += "\t" + words[i] + "(" + postags[i] + ")" + "\t" + postags[i] + "\t" + str(arcs[i].head) + "\t" + arcs[
        i].relation + "\n"

print(conll)

conlltree = DependencyGraph(conll)  #转换为依存句法图
tree = conlltree.tree() # 构建树结构
tree.draw()
