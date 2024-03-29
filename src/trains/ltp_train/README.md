## 安装Ltp python组件
下载源代码
`wget  https://github.com/HIT-SCIR/ltp/archive/v3.4.0.tar.gz`

下载语言模型
```
wget http://ospm9rsnd.bkt.clouddn.com/model/ltp_data_v3.4.0.zip   
or
wget http://ospm9rsnd.bkt.clouddn.com/model/ltp_data_v3.3.0.zip
```
解压语言模型包
`unzip ltp_data_v3.4.0.zip`

安装pyltp
`pip3 install pyltp`

# 中文分词

## 使用Ltp进行中文分词
安装 [pyltp](https://github.com/HIT-SCIR/pyltp)后创建一个python文件chinese_segmentor.py
分别实例化分词模块、加载分词模型、调用segment方法得到原始分词结果、对分词结果做后处理、加载外部专有名词词典（下载的3.4版本模型压缩包解压后没有fulluserdict.txt词典，不知道我下载的全不全，如果有相应词典欢迎补充）

## 使用结巴分词模块
张华平的NShort的中文分词算法是目前大规模中文分词的主流算法。在商用领域，大多数搜索引擎公司都使用该算法作为主要的分词算法。具有算法原理简单、容易理解、便于训练、大规模分词的效率高、模型支持增量扩展、模型占用资源低等优势.

[结巴分词](https://github.com/fxsjy/jieba)模块可支持如下三种分词方式：

  *精确模式*，试图将句子最精确地切开，适合文本分析（类似Ltp的分词方式）
  
  *全模式*：把句子中所有可以成词的词语都扫描出来，速度非常块，但是不能解决歧义
  
  *搜索引擎模式*，在精确模式的基础上对长词再次切分，提高召回率，适合用于搜索引擎分词
  
  *支持繁体分词*
  
  *支持基于概率的用户词典*
  
# 词性标注
词性标注（Part of speech tagging 或者 POS Tagging），有称为词类标注，是指判断出在一个句子中每个词所扮演的语法角色。例如，表示人、事物、地点或抽象概念的名称就是名词；表示动作或状态变化的词为动词；用来描写或修饰名词性成分或表示概念的性质、状态、特征或属性的词称为形容词，等等。

中文词性标注中影响词性标注精度的因素主要是要正确判断文本中那些常用词的词性。

一般而言，中文的词性标注算法比较统一，大多数使用HMM或最大熵算法，如结巴的词性标注。为了获得更高的精度，也有使用CRF算法的，如Ltp中的词性标注。在一般的工程应用中，语料的中文分词和词性标注通常同时完成。目前流行的中文词性标签有两个类：北大词性标注集和宾州词性标注集，它们各有千秋

## 使用pyltp词性标注
词性标注模块的文件名为pos.model。pyltp 词性标注demo比较简单，实例化Postagger->加载模型->调用postag标注

# 命名体识别
命名实体识别不仅需要标注词的语法信息（名词），更重要的是要指示词的语义信息（人名还是组织机构名等）。这里所需要识别的命名实体一般不是指已知名词（词典中的登录词），而是指新词（或称未登录词）。更具体的命名实体识别任务还要识别出文本中三大类（实体类、时间类和数字类）、七小类（人名、机构名、地名、时间、日期、货币和百分比）命名实体。
## Ltp命名实体识别
命名实体识别模块的文件名为ner.model。pyltp 命名体识别demo比较简单，分词->词性标注->实例化NamedEntityRecognizer->加载模型->调用recognize标注(以分词结果、词性标注结果为入参)

# 句法解析
目前句法分析有两种不同的理论：一种是短语结构语法；另一种是依存语法。
## Ltp句法依存树
句法解析模块的文件名为parser.model。pyltp的依存句法分析demo比较简单，分词->词性标注->实例化句法分析模块->调用parse(入参是分词及词性标注的结果)->建Conll标准的数据结构->#转换为依存句法图(这里注意需要安装python3-tk，具体参考[这里](https://www.cnblogs.com/ilym/p/8387702.html))

# 语义角色标注
语义角色标注（SRL）来源于20世纪60年代美国语言学家菲尔墨提出的格语法理论。该理论是在句子语义理解上的一个重要突破。基于此理论，语义角色标注就发展起来了，并成为句子语义分析的一种重要方式。它采用”谓词-论元角色“的结构形式，标注句子成分相对于给定谓语动词的语义角色，每个语义角色被赋予一定的语义。 美国宾州大学已经开发出一个具有使用价值的表示语义命题库，称为PropBank。语义角色标注系统已经处于NLP系统的末端，其精度和效率都受到前面几个模块的影响。(ps:我在这里实现demo时报错入参不对，应该还是模型版本下载的问题，开发环境为Ubuntu16.04  python3.6.8，[官网](http://ltp.ai/download.html)的模型下载点了半天没反应，不知道怎么下载)