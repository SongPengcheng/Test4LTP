#LTP自带的实体识别方法
import os
LTP_DATA_DIR = 'E:\work\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')
#file_name = "testfile.txt"
#content = open(file_name, "r").read()
content = "蝙蝠侠加入了哪些组织？？"

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path,'userdict.txt')
words = segmentor.segment(content)

from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path,'userdict.txt')  # 加载模型
postags = postagger.postag(words)  # 词性标注

from pyltp import  NamedEntityRecognizer
recognizer = NamedEntityRecognizer()
recognizer.load(ner_model_path)
netags = recognizer.recognize(words, postags)

print('\t'.join(words))
print('\t'.join(postags))
print('\t'.join(netags))

postagger.release()  # 释放模型
segmentor.release()
recognizer.release()

