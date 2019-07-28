# -*- coding: utf-8 -*-
import sys
import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

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

segmentor = Segmentor() # 实例化分词模块
segmentor.load_with_lexicon(cws_model_path, user_dict)
words = segmentor.segment("欧洲东部的罗马尼亚，首都是布加勒斯特，也是一座世界性的城市。")


postagger = Postagger()  #实例化词性标注类
postagger.load(pos_model_path)
postags = postagger.postag(words)

recognizer = NamedEntityRecognizer() # 实例化命名实体识别模块
recognizer.load(ner_model_path)
netags = recognizer.recognize(words, postags)

for word, postag, netag in zip(words, postags, netags):
    print(word+"/"+postag+"/"+netag)

