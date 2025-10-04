def Flames():
	print("Are you intersted to play Flames, Then")
	my_name =  input("Enter your name :")
	other_name = input("Enter your crush name :")
	list_1= {}
	for character in my_name:
		if character in list_1:
			list_1[character] += 1
		else:
			list_1[character] = 1
	list_2= {}
	for character in other_name:
		if character in list_2:
			list_2[character] += 1
		else:
			list_2[character] = 1
	# print(list_1,list_2)		
	Total = 0
	for i in my_name:
		if i in list_2:
			if list_2[i] == 1:
				list_2.pop(i)
				list_1[i] -= 1
			else:
				list_2[i] -= 1
				list_1[i] -= 1	
		else:
			continue
	for i in list_1:
		Total += list_1[i]
	for i in list_2:
		Total += list_2[i] 		
	# print(list_1,list_2)
	# print(Total)	
	l = ["F","L","A","M","E","S"]
	if Total <= 0:
		print("Sorry, All the letters in your names is common, So can't make Flames")	
	else:
		while len(l) > 1:
			count = Total % len(l)
			if count != 0:
				l = l[count:] + l[:count - 1]
			else:
				l.pop()	
		
		if l[0]	== "F":
			print("Don’t waste money on roses… just buy a friendship band, because you two are officially “Friends”! 🌸🤝")
		elif l[0] == "L":
			print("Don’t be shy… guess what? Your crush also had feelings for you too! 💖")	
		elif l[0] == "A":
			print("You only have affection for your crush. Don’t worry—God has made another match for you. 😏")
		elif l[0] == "M":
			print("Congratulations! Now it’s time to think about family planning 💖, because you both are getting married soon...")			
		elif l[0] == "E":
			print("It’s better for you to stay alert… because your crush is your enemy.")
		else:
			print("Oh no... Make your heart strong, because you’ll be shocked to hear this: you two are Siblingsss.......💖 ")	

	# print(l)	
Flames()