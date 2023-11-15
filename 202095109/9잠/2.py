'''
작성일:20203년 11월 15일
작성자:양사호 202095109
설명
'''

text = "There's a reason some people are working to make it harder to vote, especially for people of color. It’s because when we show up, things change."

textList=text.split()
print(len(textList))

text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

checklist=['kt','samsung','lg','skt']
textNList_re=''
textN=text.lower()
textNList=textN.split()
for i in textNList:
    for x in checklist:
        if(i==x):
            textNList_re+="* "
            break
    else:
        textNList_re+=i+" "

print(textNList_re)

'''for i in checklist:
    textN=textN.replace(i,'*')

print(textN)'''




'''text_low=text.lower()

textre_low=text_low.split()

for i in textre_low:
    for x in checklist:
        if(i==x):
            textre_low.remove(i)
        
print(textre_low)
text_low=' '.join(textre_low)

print(text_low)'''