# -*- coding: utf-8 -*-
import sys
import os
from pyltp import Segmentor
from pyltp import Postagger

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

segmentor = Segmentor() # 实例化分词模块
segmentor.load_with_lexicon(cws_model_path, user_dict)
words = segmentor.segment("在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。")


postagger = Postagger()  #实例化词性标注类
postagger.load(pos_model_path)

postags = postagger.postag(words)
for word, postag in zip(words,postags):
	print(word + "/" + postag)
