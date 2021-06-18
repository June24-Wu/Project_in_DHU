import jieba.analyse
import jieba

def  readfile(path):
    file = open(path,'r')
    datalist = file.readlines()
    data = str(datalist)
    return data

def cut(data):
    cut = jieba.cut(data.strip())
    # cutwords = ','.join(cut)
    return(cut)

def stopwordslist(path):
    stop_words = [line.strip() for line in open(path , 'r').readlines()]
    return stop_words

def keywordslist(path):
    keywords = [line.strip() for line in open(path , 'r').readlines()]
    return keywords

def moveStopWords(stop_words, words,key):
    # words = list(words)
    outstr = ''
    for word in words:
        if word not in stop_words:
            if word in key :
                if word != '\n':
                    outstr += word + '\n'
    return outstr

#基于TF-IDF 关键词抽取
def key_words(data):
    for x,w in jieba.analyse.extract_tags(data , withWeight =True,topK=30):
        print('%s %s' % (x,w))


stop_words = stopwordslist('C:\\Users\\HP\\Desktop\\biden词频\\stopwords2.txt')
key = keywordslist('C:\\Users\\HP\\Desktop\\数据\\keywords.txt')
path = 'C:\\Users\\HP\\Desktop\\biden词频\\biden.txt' 
words = cut(readfile(path))
without_stopwords = moveStopWords(stop_words , words ,key)
keywords = key_words(without_stopwords)
print(keywords)