#用于进行强制分词
import os
LTP_DATA_DIR = 'E:\work\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path,'userdict.txt')
words = segmentor.segment("黄渤毕业于新加坡国立大学")

from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path,'userdict.txt')  # 加载模型
postags = postagger.postag(words)  # 词性标注

print('\t'.join(words))
print('\t'.join(postags))

postagger.release()  # 释放模型
segmentor.release()