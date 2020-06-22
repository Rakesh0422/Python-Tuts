#Program having features like Excel

#Function to take multiple input
def read_input(prompt):
	print("Press Enter to give Input and when done just press enter")
	x = input(prompt)
	while x:
		yield x
		x = input(prompt)


#Function to calculate mean
def mean(lst):
	return sum(lst) / len(lst)

#Function to calculate mode
def mode(lst):
    most = max(list(map(lst.count, lst)))
    return list(set(filter(lambda x: lst.count(x) == most, lst)))


#Function to calculate median
def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


# Function to remove duplicate elements 
def remove(lst): 
    return [t for t in (set(tuple(i) for i in lst))]


#Function to add n numbers
def add(lst):
	return sum(lst) 


def mul(lst):
    prod = 1
    for num in lst:
        prod = prod * num
    print(prod)
    return prod


#Function to print tuple
def printList(lst):
	print("S_No"," Roll_No","   Name","   Marks")
	for i in range(0,len(lst)):
		print((i+1),'\t',lst[i][0],'\t',lst[i][1],'\t',lst[i][2])

def show_menu():
    '''
    Shows the list of available operations
    :return: None
    '''
    print('\n\n','*'*70)
    print("Choose from the following")
    print("1. Add")
    print("2. Multiply")
    print("3. Mean")
    print("4. Mode")
    print("5. Median")
    print("6. Remove Duplicate")
    print("7. Exit the program")
    option = input("Enter your choice of operation to be performed : ")
    print('\n')
    if option == str(7):
        print("Exiting the Program")
        exit(0)
    elif option ==str(6):
    	lst = []
    	print("Input Instruction: Roll_No Name Marks")
    	line = input("Enter the list of Students:\n")
    	while(line != ''):
    		lst.append(tuple(line.split()))
    		line = input()
    	printList(lst)
    	print("\n***Output***\n")
    	printList(remove(lst))
    elif option == str(5):
    	lst=list(map(float, read_input("-> ")))
    	print(lst)
    	print("\n","The Median of list is :", median(lst))
    elif option == str(4):
        lst=list(map(float, read_input("-> ")))
        print(lst)
        print("\n","Mode of list is :",mode(lst))
    elif option == str(3):
        lst = list(map(float, read_input("-> ")))
        print(lst)
        print("\n","Mean of list is :",mean(lst))
    elif option == str(2):
    	lst = list(map(float, read_input("-> ")))
    	print(lst)
    	print('\n',"The Product of list is :",mul(lst))
    elif option == str(1):
    	lst = list(map(float, read_input("-> ")))
    	print(lst)
    	print('\n',"The Sum of list is :",add(lst))

while True:
    show_menu()