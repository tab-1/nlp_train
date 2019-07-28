# -*- coding: utf-8 -*-
import sys
import os
import jieba

# 设置 UTF-8 输出环境
import importlib
importlib.reload(sys)

current_file_path = os.path.abspath(__file__)
ltp_train_path = os.path.dirname(current_file_path)
trains_path = os.path.dirname(ltp_train_path)
src_path = os.path.dirname(trains_path)
project_path = os.path.dirname(src_path)
user_dict = os.path.join(project_path, "models/jieba_userdict.txt")


sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树。"

jieba.load_userdict(user_dict) # 使用用户词典

wordlist = jieba.cut(sent, cut_all=True)  # 全模式
print("全模式:  {}".format(" | ".join(wordlist)))


wordlist = jieba.cut(sent)  # 精确模式
print("精确模式:  {}".format(" | ".join(wordlist)))


wordlist = jieba.cut_for_search(sent)  # 搜索引擎模式
print("搜索引擎模式:  {}".format(" | ".join(wordlist)))