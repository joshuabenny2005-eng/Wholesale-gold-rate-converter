print ("___Wholesale Rate converter___")
pureweight = []

while True :
	print ("1.Rate convert")
	print("2.show all weight")
	print("3.Total weight")
	print("4.Exit")
	option = input("Enter your option ")
	
	if option =="1":
		while True:
			try:
				weight=float (input("Enter your weight :"))
				break
			except ValueError:
				print("Invalid input! Please enter a valid i")
		
		while True :
			try:
				touch = float(input("Enter your touch "))
				break 
			except ValueError:
				print("invalid input")
			
		pure_weight = ( weight * touch )/99.9
		print(round(pure_weight,3))
		pureweight.append(round(pure_weight,3))	
	elif option == "2":
		print(pureweight)
	
	elif option =="3" :
		total_weight = round(sum (pureweight),3)
		print(total_weight)
	
	elif option =="4":
		break 
		
	else :
		print("invalid")
		
