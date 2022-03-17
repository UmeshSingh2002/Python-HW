def sort_list(anylist):
	n=len(anylist)
	i=0
	while i<n:
		j=0
		while j<n-i-1:
			if anylist[j]>anylist[j+1]:
				a=anylist[j]
				anylist[j]=anylist[j+1]
				anylist[j+1]=a
			j=j+1
		i=i+1
	return anylist
