# -*- coding: utf-8 -*-
import sys
import os
from pyltp import Segmentor

import importlib
importlib.reload(sys)

current_file_path = os.path.abspath(__file__)
ltp_train_path = os.path.dirname(current_file_path)
trains_path = os.path.dirname(ltp_train_path)
src_path = os.path.dirname(trains_path)
project_path = os.path.dirname(src_path)
model_path = os.path.join(project_path, "models/ltp_data_v3.4.0/cws.model")
user_dict = os.path.join(project_path, "models/ltp_data_v3.4.0/fulluserdict.txt")

# 实例化分词模块
segmentor = Segmentor()
# 加载分词模型
# segmentor.load(model_path)
segmentor.load_with_lexicon(model_path, user_dict) #加载专有名词词典

words = segmentor.segment("在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。")
print("原始分词结果：   {}".format(" | ".join(words)))

postdict = {"解 | 空间": "解空间", "深度 | 优先": "深度优先"} ## 分词后处理词典

seg_sent = " | ".join(words)
for key in postdict:
    seg_sent = seg_sent.replace(key, postdict[key])
print("分词结构后处理： {}".format(seg_sent))


