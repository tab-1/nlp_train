# -*- coding: utf-8 -*-
import sys
import os
# from nltk.tree import Tree    #导入nltk tree结构
# from nltk.grammar import DependencyGrammar  #导入依存句法包
from nltk.parse import *
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser
from pyltp import SementicRoleLabeller

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
ner_model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/ner.model")
parser_model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/parser.model")
labe_model_path = os.path.join(project_path, "models/ltp_data_v3.3.0/srl/")



sent = "欧洲东部的罗马尼亚，首都是布加勒斯特，也是一座世界性的城市。"

segmentor = Segmentor() # 实例化分词模块
segmentor.load_with_lexicon(cws_model_path, user_dict)
words = segmentor.segment(sent)
wordlist = list(words)  #从生成器变为列表元素

postagger = Postagger()  # 实例化词性标注类
postagger.load(pos_model_path)
postags = postagger.postag(words)

recognizer = NamedEntityRecognizer() # 实例化命名实体识别模块
recognizer.load(ner_model_path)
netags = recognizer.recognize(words, postags)

parser = Parser()  # 句法解析
parser.load(parser_model_path)
arcs = parser.parse(words, postags)

#语义角色标注
labeller = SementicRoleLabeller()
labeller.load(labe_model_path)
roles = labeller.label(words, postags, netags, arcs)

#输出标注结果
for role in roles:
	print('rel:', wordlist[role.index]) #谓词
	for arg in role.arguments:
		if arg.range.start != arg.range.end:
			print(arg.name, ' '.join(wordlist[arg.range.start:arg.range.end]))
		else:
			print(arg.name,wordlist[arg.range.start])


