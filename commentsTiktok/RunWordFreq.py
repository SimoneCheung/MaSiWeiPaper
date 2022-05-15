#Counting the word frequency and generate a wordcloud
import jieba
import wordcloud
import os

def takeSecond(elem):
    return elem[1]

def createWordCloud(text):
    #font_path is the font that you want to show in the wordcloud, we can change to another
    w=wordcloud.WordCloud(font_path="C:/Windows/Fonts/simhei.ttf",width=600,height=400,background_color="white")
    w.generate(text)  
    #this is the filename of the wordcloud picture
    w.to_file('wordcloud.jpg')

def main():
    path = os.getcwd() #to get the path where this python script is
    txtpath = os.path.join(path,"commentsTiktok.txt") #to include the txt filename into the text path
    file = open(txtpath,"r", encoding='utf-8') #open the text file
    text=file.read()
    file.close()

    words = jieba.lcut(text) # use jieba to cut the Chinese words
    counts = {} # set a dictionary to store the words and how many times they appear
    for word in words:
        if len(word) == 1:
            continue            
        else:
            rword = word
        counts[rword] = counts.get(rword,0) + 1

    file = open(path + "/excludes.txt","r", encoding='UTF-8') #excludes.txt is the words that won't be counted
    excludes =file.read().split(",")
    file.close

    for delWord in excludes:
        try:
            del counts[delWord]
        except:
            continue

    items = list(counts.items())
    items.sort(key = takeSecond,reverse=True)    

    for i in range(100): # find 50 words appear most times 
        item=items[i]
        keyWord =item[0]
        count=item[1]
        #print("{0:<10}{1:>5}".format(keyWord,count))
        print ("|",keyWord, "|",count,"|")

    createWordCloud(str(items[0:80]).replace("'", "")) #generate the picture of 80 words appear most times

main()
