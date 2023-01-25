def removeCommonWords(sent1,sent2):
  com=[]
  sent1=list(sentence1.split())
  sent2=list(sentence2.split())
  for i in sent1:
    if i in sent2:
      sent1.remove(i)
      sent2.remove(i)
  print(*sent1)
  print(*sent2)
sentence1 =input("enter string")
sentence2 =input("enter string")
removeCommonWords(sentence1,sentence2)
