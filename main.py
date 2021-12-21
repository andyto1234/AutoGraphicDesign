import re
from datetime import datetime
import nltk
from newspaper import Article
import argparse
import sys
from os import path
from pathlib import Path

# def drawing(titlestring):
#     db.newDrawing()
#     db.newPage(5000, 5000)
#     db.language('English')
#     db.fill(1)
#     db.rect(0, 0, 5000, 5000) # White canvas
#     db.fill(0)
#     db.rect(125, 125, 4750, 4750) # Black smaller canvas
#     db.font('Termina')
#     db.fontSize(270)
#     db.fill(1)
#     db.rect(330, 4550, 4340, 40) #top rectangle
#     db.rect(1000, 450, 3670, 40) #bottom rectangle
#     db.fill(0.12)
#     db.rect(330, 2750, 4340, 1700) #title background
#     db.fill(0.4)
#     db.rect(330, 2500, 3730, 140) # 1st context box
#     db.rect(330, 2300, 3030, 140) # 2nd context box
#     db.rect(330, 2100, 2330, 140) # 3rd context box
#     db.rect(330, 1900, 1630, 140) # 4th context box
#     db.fill(1)
#     titleBox = (450, 1200, 4100, 3130)
#     db.lineHeight(285)


#     def convert_to_uupercase(m):
#         """Convert the second group to uppercase and join both group 1 & group 2"""
#         return m.group(1) + m.group(2).upper()
#     titleText = titlestring
#     titleText = re.sub("(^|\s)(\S)", convert_to_uupercase, titleText)


#     db.textBox(titleText, titleBox, align='left')
#     im = db.ImageObject()
#     with db.savedState():
#         db.scale(0.45, 0.45)
#         db.image('Logo/logo.png', (550, 250))

#     db.fontSize(85)
#     dateBox = (1000,4510,3670,420)
#     db.textBox(datetime.today().strftime("%m/%d/%y"), dateBox, align='right')

#     hastagBox = (1000,150,3670,420)
#     db.textBox('@ukeconomiccircle    #StandWithHongKong', hastagBox, align='right')
#     Path(f'Designs/').mkdir(parents=True, exist_ok=True)
#     filename = f"Designs/{datetime.today().strftime('%Y%m%d')}.jpg"
#     if path.isfile(filename)==True:
#         now = datetime.now()
#         filename = f"Designs/{now.strftime('%Y%m%d_%H%M%S')}.jpg"
#     db.saveImage(filename)
#     db.endDrawing()
#     return filename

def summary(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    title = article.title
    news_summary = article.summary
    keywords = article.keywords
    return title, news_summary, keywords

def main(url):
    title, news_summary, keywords =summary(url)
    titlestring = '【'+title+'】'
    print(titlestring)
    print(news_summary)
    keywords = keywords+['FightForFreedom','StandWithHongKong','ukeconomiccircle','英國經濟圈']
    hashtags = []
    for keyword in keywords:
        hashtags.append('#'+keyword)
        print('#'+keyword)
    hashtags = ' '.join(hashtags)
    # filename = drawing(title)
    return titlestring, news_summary, hashtags

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description = 'Auto Graphic Design with Article Summary')
    # parser.add_argument('--folder', help = "Subfolder of C:\TEMP\ to manipulate")
    # args = parser.parse_args()
    url = str(sys.argv[1])
    main(url)


