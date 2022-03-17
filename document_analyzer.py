given_File = open('document.txt')
words_in_file=given_File.read()
list_of_words=words_in_file.split()
word_counter={}
for i in list_of_words:
	if i not in word_counter:
		word_counter[i]=1
	else:
		word_counter[i]=1+word_counter[i]
last_dic = {}
l = len(word_counter)
new_dic = {}
a=0
sorted_word_counter = sorted(word_counter, key=word_counter.get)
for x in sorted_word_counter:
	a=a+1
	new_dic[x] = word_counter[x]
	if a == l-4:
		l=l+1
		last_dic[x] = new_dic[x]
lok=list(last_dic.keys())
lov=list(last_dic.values())
for i in range(0,5,1):
	for j in range(i+1, 5,1):
		if lov[j]==lov[i]:
			if lok[j]>lok[i]:
				temporary=lok[j]
				lok[j]=lok[i]
				lok[i]=temporary
print("\r")
for i in range(4,-1,-1):
	print(f"{lok[i]}: {lov[i]}")
