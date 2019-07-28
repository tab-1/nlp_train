## 概述
该项目是学习《NLP汉语自然语言处理原理与实战》郑捷著，而自己总结的关于NLP基本任务及相关子摸快的demo实现

### 目录
```
    |-- README.md           整个项目的说明
    |-- requirements.txt    项目依赖描述文件
    |-- models              模型保存文件目录
    |   |-- jieba_userdict.txt
    |   |-- ltp_data_v3.4.0 Ltp模型文件夹
    |       |-- cws.model       ltp分词模型
    |       |-- md5.txt
    |       |-- ner.model       ltp命名体识别模型
    |       |-- parser.model    ltp句法解析模型
    |       |-- pisrl.model     ltp语义角色标注模型
    |       |-- pos.model       ltp词性标注模型
    |       |-- version
    |-- src
    |   |-- config  配置文件目录
    |   |   |-- __init__.py
    |   |   |-- config.ini      配置文件
    |   |   |-- read_config.py  读取配置文件的脚本
    |   |-- log 日志文件目录
    |   |   |-- __init__.py
    |   |   |-- logger.py       日志封装脚本
    |   |   |-- singleton.py    单例模式实现脚本
    |   |-- trains  demo练习目录
    |       |-- __init__.py
    |       |-- ltp_train       Ltp练习目录
    |           |-- README.md   Ltp练习概述
    |           |-- __init__.py
    |           |-- chinese_segmentor.py    pyltp中文分词demo
    |           |-- jieba_segmentor.py      jieba中文分词demo
    |           |-- labeller.py             pyltp语义角色标注demo
    |           |-- ner_train.py            pyltp命名体识别demo
    |           |-- parser_train.py         pyltp句法解析demo
    |           |-- pos_train.py            pyltp词性标注demo
```