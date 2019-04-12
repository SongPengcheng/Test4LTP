import os
LTP_DATA_DIR = 'E:\work\ltp_data_v3.4.0'  # ltp模型目录的路径
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl_win.model')

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load_with_lexicon(cws_model_path,'userdict.txt')
words = segmentor.segment("中兴C580支持什么样的网络类型")

from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load_with_lexicon(pos_model_path,'userdict.txt')  # 加载模型
postags = postagger.postag(words)  # 词性标注

from pyltp import Parser
parser = Parser()
parser.load(par_model_path)
arcs = parser.parse(words,postags)

from pyltp import SementicRoleLabeller
labeller =  SementicRoleLabeller()
labeller.load(srl_model_path)  # 加载模型
roles = labeller.label(words, postags, arcs)  # 语义角色标注

print("\t".join(words))
#print("\t".join(postags))
print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
for role in roles:
    print(role.index, "".join(
        ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))

labeller.release()
parser.release()
postagger.release()
segmentor.release()

