#!/usr/bin/python 
import sys
import os	
import psycopg2

def phase1(cursor):

	print "    Phase 1: Select Views "
	print "-----------------------------------------------\n"
	print "1.What are the names of the employees that participated in the 'Let it be' campaign?\n"
	print "2.What are the names of the second tier volunteers?\n"
	print "3.What is the name of the second tier volunteer that helped organizing the campaign 'In My Life'? \n"
	print "4.Which supporter donated the most amount of money into GnG?\n"
	print "5.Which member is below the age of 25 that supported the campaign 'Let it be'?\n"
	print "6.Which position in the company has the least salary?\n"
	print "7.What amount of money did a supporter donated at most?\n"
	print "8.What are names of the male supporters that participated in the 'Let it be' campaign\n"
	print "9.What is the average age of the volunteers that organized the campaign 'Let it be'?\n"
	print "10.Which campaign cost the most? And what is the campaigns name and where was the campaign located?\n"
	print "11.What is the total cost of each event?\n"
	
	number = raw_input("Enter Query Number:")
	if(number == '1'):
		cursor.execute("""
		select * 
		from view1
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])
	
	elif(number == '2'):

		cursor.execute("""
		select * 
		from view2
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '3'):

		cursor.execute("""
		select * 
		from view3
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '4'):

		cursor.execute("""
		select * 
		from view4
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '5'):

		cursor.execute("""
		select * 
		from view5
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '6'):

		cursor.execute("""
		select * 
		from view6
		""",params)
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '7'):

		cursor.execute("""
		select * 
		from view7
		""",params)
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '8'):

		cursor.execute("""
		select * 
		from view8
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Name : %s" % (row[0])

	elif(number == '9'):

		cursor.execute("""
		select * 
		from view9
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Average : %s" % (row[0])

	elif(number == '10'):

		cursor.execute("""
		select * 
		from view10
		""")	 
		for row in cursor.fetchall():
		    print "Campaign : %s\nSum: %s\n location: %s\n" % (row[0],row[1],row[2])

	elif(number == '11'):

		cursor.execute("""
		select * 
		from view11
		""")
		print cursor.description[0].name	 
		for row in cursor.fetchall():
		    print "Campaign : %s\n Sum: %s\n" % (row[0],row[1])
	else:
		print("Invaild Input! Please Start Over Again!")
	return

def phase2(cursor,dbconn):
	print "\n\n"
	print "--------------------------------------"	
	print "Phase 2:Setting Up a Campaign"
	print "--------------------------------------\n"
	print "Please select one of following:\n"
	print "1.Create new Campaign"
	print "2.Adding (New/Existing) Volunteers to organize Campaign"
	print "3.Scheduling Events"
	print "4.View Campaign"
	print "5.Go back to Home Page"
	print "-------------------------------------\n"
	print "To Select, Please Enter Number:#"
	
	num = raw_input("Please Enter Number:")
	
	if num == '1':
		print "Create new Campaign"
		print "---------------------------------\n"
		name = raw_input("Please Enter Campaign Name:")
		startDate = raw_input("Please Enter start date:[yyyy/mm/dd]")
		endDate = raw_input("Please Enter end date:[yyyy/mm/dd]")
		params = {'name':name, 'sd':startDate, 'ed':endDate}
		cursor.execute("""
	    	insert into campaign(name,starttime,endtime) values(%(name)s,%(sd)s,%(ed)s)
			""",params)
		print "You Have Sucessfully Created A Campaign!"
		print "---------------------------------------------\n"
		print "To Save Changes, Enter 1"
		print "Start Again, Enter 0"
		i = raw_input("Please Enter Number:")
		if i == '1':
			dbconn.commit()
			print "You Have Saved Changes!"
			return
		elif i == "0":
			phase2(cursor,dbconn)
		else:
			print "Bad Input!"
			return
	if num == '2':
		print "Adding (New/Existing) Volunteers to organize Campaign"
		print "-----------------------------------------------------------\n"
		print "Would you like to Add a new Volunteer to our Organization?"
		i = raw_input("Please enter one of [y/n]:")
		if i == 'y':
			sin = raw_input("Please Enter Sin Number:");
			name = raw_input("Please Enter Volunteer Name:");
			gender = raw_input("Please Enter Gender:");
			age = raw_input("Please Enter Age:");
			numberOfParticipation = raw_input("Please Enter Number Of Participation:");
			tier = raw_input("Please Enter Tier Number:");
			params = {'sin':sin, 'name':name, 'gender':gender,'age':age, 'num':numberOfParticipation,'tier':tier}
			cursor.execute("""
			insert into volunteer(sin,name,gender,age,numberofparticipation,tier) values(%(sin)s,%(name)s,%(gender)s,%(age)s,%(num)s,%(tier)s)
			""",params)
			print "You Have Added Volunteer!"
			print "-------------------------------\n"		
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0"
			i = raw_input("Please Enter Number:")
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
			elif i == "0":
				phase2(cursor,dbconn)
			else:
				print "Bad Input!"
				return
		if i == 'n':
			print "The Current Campagins:"
			print "---------------------------\n"
			cursor.execute("""
			select name from campaign	
			""")
			for row in cursor.fetchall():
				print "%s\n" % (row[0])
			print
			print"Do you want to a make Volunteer organize campaign?"
			print "-------------------------------------------------------\n"
			val = raw_input("Please Enter [y/n]:")
			if val == 'y':
				print "You Have Choosen y!"
				print "------------------------\n"
				print "The Current Available Volunteers Are:\n"
				cursor.execute(""" select name ,sin from volunteer""")
				for row in cursor.fetchall():
					print "Name: %s"% row[0]
					print "Sin Number:%s" % str(row[1])
					print "\n"
				print
				sin = raw_input("Please Enter the sin number of the Volunteer:")
				campaign = raw_input("Please Enter the Campaign Name:")
				params = {'volunteer':sin,'campaign':campaign}
				cursor.execute("""
				insert into organize(volunteer,campaign) values(%(volunteer)s,%(campaign)s )		
				""",params)
				
				print "You Have Made the Volunteer organzie a Campaign!"
				print "-----------------------------------------------------\n"		
				print "To Save Changes, Enter 1"
				print "Start Again, Enter 0"
				i = raw_input("Please Enter Number:")
				if i == '1':
					dbconn.commit()
					print "You Have Saved Changes!\n\n\n"
					return
				elif i == "0":
					phase2(cursor,dbconn)
				else:
					print "Bad Input!\n\n"
					return
			if val =='n':
				print "You have selected n!"
				print "back to main page\n\n\n"
				return

		
	if num == '3':
		print "Scheduling Events"
		print "----------------------\n"
		campaign = raw_input("Please Enter Campaign Name:")
		name = raw_input("Please Enter Event Name:")
		note = raw_input("Please Enter Any Note For This Event:")
		params = {'campaign':campaign,'name':name,'note':note}
		cursor.execute("""
		insert into event(campaign,name,note) values(%(campaign)s,%(name)s,%(note)s)
		""",params)
	
		print "You Have Scheduled An Event!"
		print "-------------------------------\n"		
		print "To Save Changes, Enter 1"
		print "Start Again, Enter 0"
		i = raw_input("Please Enter Number:")
		if i == '1':
			dbconn.commit()
			print "You Have Saved Changes!"
			return
		elif i == "0":
			phase2(cursor,dbconn)
		else:
			print "Bad Input!"
			return
	if num == '4':
		print "View Campaigns"
		print "--------------------\n"
		print "The Current Campaigns "
		print "------             name             ------|--------  starttime --------|-----  endtime -----|"
		cursor.execute("""
		select * 
		from campaign
		""")
		
		for row in cursor.fetchall():
			print "------%s------|---------%s---------|-----%s-----|"% (row[0],row[1],row[2]) 
		
	if num == '5':
		print "Back to Home Page"
		print "----------------------\n"
		return
	else:
		print "\nWrong Entry!"
		print "Please Start Again!\n"
		phase2(cursor,dbconn)

def phase3(cursor):
	print "-------------------------------------"
	print "| Phase 3: Accounting Information   |"
	print "-------------------------------------\n"
	print "\n 1.To View Flow In\n"
	print " 2. To View Flow Out\n"
	print " 3. Current Balance\n\n\n"
	i = raw_input("Please Select A Number:")
	print
	donnation = 0
	f = 0.0
	cost = 0
	g = 0.0
	if i == '1':
		print" You have selected 1!"
		print" Here is the Flow In Information:"
		print "--------------------------------------\n\n"
		cursor.execute("""
		select name,donation from supporter
		""")
		info = cursor.fetchall()
		for row in info:
			donnation = donnation +row[1]
		print "Currently We Have Funding : $ "+ str(donnation) +"\n\n\n"
		print "Histogram:"
		print "----------------------\n" 
		for row in info:
			i = float(row[1])
			f = i/donnation 
			print ""+"#"*(int(f*20)+1 ) + "\n"+" \t\t\t\t      Donation:"+str(row[1])+"    name :"+ row[0]+"\n"

		print
	
	if i == '2':	
		print" You have selected 2!"
		print" Here is the Flow Out Information:"
		print "--------------------------------------\n\n"
		cursor.execute("""
		select * from cost
		""")
		info = cursor.fetchall()
		for row in info:
			cost = cost +row[1]
		print "Currently We Have Spend : $ "+ str(cost) +"\n\n\n"
		print "Histogram:"
		print "-----------------\n" 
		for row in info:
			i = float(row[1])
			g = i/cost
			print ""+"#"*(int(g*20)+1 ) + "\n"+" \t\t\t\t      Cost:"+str(row[1])+"    subject :"+ row[0]+"     Campaign:"+row[2]+"\n"
				
		print 	
	
	if i == '3':
		print "You have selected 3!"
		print "Here is your Balance:"
		print "--------------------------\n"
		
		cursor.execute("""
		select name,donation from supporter
		""")
		info = cursor.fetchall()
		for row in info:
			donnation = donnation +row[1]
		
		cursor.execute("""
		select * from cost
		""")
		info = cursor.fetchall()
		for row in info:
			cost = cost +row[1]
		print "Balance: "+str(donnation -cost)		
	else:
		print "Wrong Entry, Please Start Again!\n\n"
		phase3(cursor)

def phase4(cursor,dbconn):
	print "Phase 4:Membership History"
	print "-------------------------------\n"
	print "Please Select One Of Following:"
	print "1.View Membership History"
	print "2.Add Annotation to Members\n\n"
	num = raw_input("Please Enter A Number:")
	print
	if num == '1':
		print "You Have Selected 1"
		print "------------------------\n\n"
		print "Here is your Membership History"
		cursor.execute("""
		select * from member
		""")
		for row in cursor.fetchall():
			print "Name:"+row[1]
			print "--------------------\n"
			print "Memeber Sin :"+str(row[0]) 
			print "Gender: "+ row[2]
			print "Age: "+ str(row[3])
			print "Member ID:"+ str(row[4])
			print "Total Donaton:"+ str(row[5])
			print "Membership Duration:" + row[6]
			print "Annotation: "+ str(row[7])
			print "\n\n"
	if num == '2':
		print "You Have Selected 2"
		print "------------------------\n"
		print "Currently , We Have Memebers:\n\n"
		cursor.execute("""
		select sin,name from member
		""")
		for row in cursor.fetchall():
			print "Name : "+ row[1] +"Sin :" + str(row[0])
		print
		print"To add Annotation to member, please enter member sin number\n\n"
		sin = raw_input("Please Enter the Member Sin number:")
		print
		annotation = raw_input("Please add Annotation Here:")
		params = {'sin':sin,'anno':annotation}
		cursor.execute("""
		update member set annotation = %(anno)s where sin = %(sin)s	
		""",params)
		
		print "You Have Added An Annotation!"
		print "-----------------------------------------------------\n"		
		print "To Save Changes, Enter 1"
		print "Start Again, Enter 0"
		i = raw_input("Please Enter Number:")
		if i == '1':
			dbconn.commit()
			print "You Have Saved Changes!\n\n\n"
			return
		elif i == "0":
			phase4(cursor,dbconn)
		else:
			print "Bad Input!\n\n"
			return
		
def phase5(cursor,dbconn):
	print "------------------------------------"
	print "|  Phase 5: Extra Functionality!   |"
	print "------------------------------------ \n"
	print "Please Select One Of Following:\n"
	print "1.Delete "
	print "2.Modify\n"
	
	num = raw_input("Please Enter A Number:")
	print
	if num == '1':
		print "You Have Selected 1"
		print "------------------------\n"
		"Please Select One Of Following:\n"
		print"1.Delete Memeber"
		print"2.Delete Volunteer"
		print"3.Delete Campaign"
		print 
		i = raw_input("Please Enter A Number")
		if i == '1':
			print "You Have Selected 1!"	
			print "-------------------------\n"
			print "The Current Members Are:\n"
			cursor.execute(""" select name,sin from member""")
			for row in cursor.fetchall():
				print "Member Name:%s" % row[0]
				print "Member ID : %s" % str(row[1])
			print 
			sin = raw_input("To Delete, Please Enter Member ID:")
			params = {'sin':sin}
			cursor.execute("""
			delete from member where sin = %(sin)s
			""",params)
			
			print "You Have Removed A Member!"
			print "-------------------------------\n"		
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
		
		if i == '2':
			print "You Have Selected 2!"	
			print "-------------------------\n"
			print "The Current Volunteers Are:\n"
			cursor.execute(""" select name, sin from volunteer""")
			for row in cursor.fetchall():
				print "Volunteer Name:%s" % row[0]
				print "Volunteer Sin : %s" % str(row[1])
			print 
			sin = raw_input("To Delete, Please Enter SIN:")
			params = {'sin':sin}
			cursor.execute("""
			delete from volunteer where sin = %(sin)s
			""",params)
			
			print "You Have Removed A Volunteer!"
			print "-------------------------------\n"		
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
				
		if i == '3':
			print "You Have Selected 3!"	
			print "-------------------------\n"
			print "The Current Campaigns Are:\n"
			cursor.execute(""" select name from campaign""")
			for row in cursor.fetchall():
				print "Campaign Name:%s" % row[0]
			print
		 
			name = raw_input("To Delete, Please Enter Campaign Name:")
			params = {'name':name}
			cursor.execute("""
			delete from campaign where name = %(name)s
			""",params)
			
			print "You Have Removed A Campaign!"
			print "-------------------------------\n"		
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
		else: 
			print "Wrong Entry!, Please Start Again!"
			return	
	if num == '2':	
		print "---------------------------"
		print "|You| |Have| |Selected| |2|"
		print "---------------------------\n"
		print"Please Select One Of Following:"
		print"-------------------------------------\n"
		print"1.Change Campaign Name"
		print"2.Add Campaign Location"
		print"3.Change Memember Info "
		i = raw_input("Please Enter A Number")
		print
		if i == '1':
			print "You Have Selected 1 !"
			print "--------------------------\n"
			print "Currenty We Have Campaigns:"
			cursor.execute("""select name from campaign""")
			for row in cursor.fetchall():
				print "Campaign Name : %s" % row[0]
				print
			print "Please Select One Campaign And Enter The New Name!"
			name = raw_input("To Select A Campaign, Enter Campaign Name:")
			print
			new_name = raw_input("Please Enter The New Name:")
			params = {'name':name,'new_name':new_name}
			cursor.execute("""
			update campaign set name =%(new_name)s where name = %(name)s
			""",params)
			print "You Have Sucessfuly Changed the Name !! Congrats!!\n\n"	
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
		elif i == '2':
	
			print "You Have Selected 2 !"
			print "--------------------------\n"
			print "Currently We Have Campaigns with locaion:"
		
			cursor.execute("""select * from hostin""")
			for row in cursor.fetchall():
				print "Campaign Name : %s" % row[1]
				print "Location : %s\n" % row[0]
			
			print "Please Select One Campaign And Add New Location!"
			name = raw_input("To Select A Campaign, Enter Campaign Name:")
			print
			add = raw_input("Please Enter The New Location:")
			params = {'name':name,'add':add}
			cursor.execute("""
			insert into location(address) values( %(add)s) 
			""",params)
			cursor.execute("""
			insert into hostin(location, campaign) values(%(add)s,%(name)s)
			""",params)
			print "You Have Sucessfuly Added New Address For the Campaign!! Congrats!!\n\n"	
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
		elif i == '3':
		
			print "You Have Selected 3 !"
			print "--------------------------\n"
			print "Currently, We Have Members:\n" 
			cursor.execute("""select sin,name,donation,gender,age,duration from member""")
			for row in cursor.fetchall():
				print "Member Name : %s" % row[1]
				print "Memeber Sin Number : %s" % str(row[0])
				print "Donnated: $%s" %str(row[2])
				print "Gender: %s" %row[3]
				print "Age: %s"% str(row[4])
				print "Duration: %s"% row[5]
				print
			
			print "Please Select One Member And Add New Donnation Of Member!"
			sin = raw_input("To Select A Member, Enter Member Sin Number:")
			print
			total = raw_input("Please Enter The New Donnation Total:")
			duration = raw_input("Please Enter New Duration Of the Member:")
			age = raw_input("Please Enter Member New Age:")
			params = {'sin':sin,'total':total,'duration':duration,'age':str(age)}
			cursor.execute("""
			update member set donation = %(total)s , duration = %(duration)s, age = %(age)s  where sin = %(sin)s 
			""",params)	
			print "You Have Sucessfuly Updated The Info For the Member!! Congrats!!\n\n"	
			print "To Save Changes, Enter 1"
			print "Start Again, Enter 0\n\n"
			i = raw_input("Please Enter Number:")
			print
			if i == '1':
				dbconn.commit()
				print "You Have Saved Changes!\n\n\n"
				return
			elif i == "0":
				phase5(cursor,dbconn)
			else:
				print "Bad Input!\n\n"
				return
		else:
			print"Wrong Input ! Please Start Again!!\n\n"
			return

def transition(phase,cursor,dbconn):
	if phase == 1:
		sys.stdout.flush()
		phase1(cursor)
	elif phase == 2:
		sys.stdout.flush()
		phase2(cursor,dbconn)
	elif phase == 3:
		phase3(cursor)
	elif phase == 4:
		phase4(cursor,dbconn)
	elif phase == 5:
		phase5(cursor,dbconn)
	else:
		print("Invaild Input, Terminating Right Now!!")
		return
	
def main():
	print"\n\n"
	print("----------------------")
	print("|Welcome To Home Page|")
	print("----------------------\n")
	print("Please select a phase:\n")
	print("1.Select views")
	print("2.Setting up a Campaign")
	print("3.Accounting Info")
	print("4.Membership History")
	print("5.Extra Functions\n\n")
	print("To select a phase, please Enter Phase:#\n")
	print("To exit, please Enter Phase:q \n")
	

	flag = True
	while flag == True:
		dbconn = psycopg2.connect(host='studentdb.csc.uvic.ca', user='c370_s19',
	    password='8TmeVclb')
	
		cursor = dbconn.cursor()
		phase = raw_input("Enter Phase:")
		print
		if(phase == 'q'):
			print "You have Entered q, See You Next Time!!\n"
			dbconn.close()
			exit()
		transition(int(phase),cursor,dbconn)
		
		i = raw_input("Back to Home Page?[y/n]")
		print
		if(i =='y'):
			main() 
		if(i == 'n'):
			print "See you next time!\n"
			dbconn.close()
			exit()
		else:
			print "Wrong Input! System Terminating\n\n"
			exit()	



if __name__ == "__main__": main()
