count =0

def replaceval(n,v2i,table_1,table_2,whichtable,maxvalues,temp_arr):
	
	global count
	if(n==maxvalues): 
		print("KEY : ", v2i," is unpositioned \n"); 
		print("Cycle present. REHASH.\n"); 
		print(" ")
		count=count+1
		table_1.clear()
		table_2.clear()
		for i in range(11):
			table_1.append(-1)
			table_2.append(-1)
		for i in range(len(temp_arr)):
			varvalue=temp_arr[i]
			hashingcuko(maxvalues,varvalue,table_1,table_2,temp_arr)		
		return
	hashanswer1 = (v2i+count)%11
	hashanswer2 = int((v2i/(11+count)))%11
		
	if(table_1[hashanswer1]==v2i or table_2[hashanswer2]==v2i):
		return

	if(whichtable==0):
		if (table_1[hashanswer1]!=-1): 
			dis = table_1[hashanswer1] 
			table_1[hashanswer1] = v2i
			replaceval(n+1, dis, table_1, table_2,(whichtable+1)%2,maxvalues,temp_arr)
		else:
			table_1[hashanswer1] = v2i
			
	elif(whichtable==1):
		if (table_2[hashanswer2]!=-1): 
			dis = table_2[hashanswer2] 
			table_2[hashanswer2] = v2i
			
			replaceval(n+1, dis, table_1, table_2,(whichtable+1)%2,maxvalues,temp_arr)
		else:
			table_2[hashanswer2] = v2i
			 

def printtable(table_1,table_2):
	print("TABLE 1")	
	for i in range(len(table_1)):
		if(table_1[i]==-1):
			print("empty",end=" ")
		else:
			print(table_1[i],end=" ")
	
	print(" ")
	print("TABLE 2")
	
	for i in range(len(table_2)):
		if(table_2[i]==-1):
			print("empty",end=" ")
		else:
			print(table_2[i],end=" ")	

	print(" ")			



def insertatTable1(n,v2i,table_1):
	global count
	
	hashanswer1 = (v2i+count)%11
	#print("HASH 1 INDEX IS ", hashanswer1)
	hashanswer2 = int((v2i/(11+count)))%11
	

	if(table_1[hashanswer1]==-1):
		
		return True
	else:
		return False


def insertatTable2(n,v2i,table_2,):
	global count
	hashanswer1 = (v2i+count)%11
	hashanswer2 = int((v2i/(11+count)))%11
	
	if(table_2[hashanswer2]==-1):
		return True
	else:
		return False


def hashingcuko(n,v2i,table_1,table_2,temp_arr):
	global count
	hashanswer1 = (v2i+count)%11
	hashanswer2 = int((v2i/(11+count)))%11

	if(insertatTable1(n,v2i,table_1)==True):
		table_1[hashanswer1]=v2i
		
	elif(insertatTable2(n,v2i,table_2)==True):
		table_2[hashanswer2]=v2i
		
	elif(insertatTable1(n,v2i,table_1) == False and insertatTable2(n,v2i,table_2) == False):
		replaceval(0,v2i,table_1,table_2,0,n,temp_arr)


	


def searchval(table_1,table_2,val):
	for i in range(len(table_1)):
		if(table_1[i]==val):
			print("Value is located in table 1 at index : ",i)
			return

	for i in range(len(table_2)):
		if(table_2[i]==val):
			print("Value is located in table 2 at index : ",i)
			return

	print("Value is not present in both tables")
	return


def deleteval(table_1,table_2,val):
	for i in range(len(table_1)):
		if(table_1[i]==val):
			table_1[i]=-1
			print("VALUE DELETED")
			return

	for i in range(len(table_2)):
		if(table_2[i]==val):
			table_2[i]=-1
			print("VALUE DELETED")
			return

	print("Value is not present in both tables")
	return
	




def main():
	maxvalues=11

	table_1=[]
	table_2=[]
	temp_arr=[]
	for i in range(11):
		table_1.append(-1)
		table_2.append(-1)

	condition=True
	while(condition):
		print("")
		print("CHOOSE WHICH OPTION TO DO \n 1 to insert \n 2 to search \n 3 to print\n 4 to remove\n 5 to exit")
		choice=input("enter choice : \n")
		if(choice=="1"):
			val=input("enter key to insert\n")
			if(val.isdigit()==False):
				print("wrong input type")
				continue
			val=int(val)
			temp_arr.append(val)
			hashingcuko(maxvalues,val,table_1,table_2,temp_arr)		
		elif(choice=="3"):
			printtable(table_1,table_2)
		elif(choice=="2"):
			val=input("enter key to search\n")
			if(val.isdigit()==False):
				print("wrong input type")
				continue
			val=int(val)
			searchval(table_1,table_2,val)
		elif(choice=="4"):
			val=input("enter key to delete\n")
			if(val.isdigit()==False):
				print("wrong input type")
				continue
			val=int(val)
			deleteval(table_1,table_2,val)
		elif(choice=="5"):
			break
		else:
			print("wrong input enter again")
main()