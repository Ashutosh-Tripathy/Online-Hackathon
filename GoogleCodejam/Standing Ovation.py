import collections

with open('A-large-practice (1).in') as f:
	content = f.readlines()


CurrentNumberOfPeopleStanding=0
numOfTestCase=int(content.pop(0))

def GetNumberOfPeopleRequireForShynesX(peopleAtCurrentLevel,numberOfPeopleRequredForStanding):
	global CurrentNumberOfPeopleStanding
	if(numberOfPeopleRequredForStanding==0):
		CurrentNumberOfPeopleStanding+=peopleAtCurrentLevel
		return 0
	if(peopleAtCurrentLevel==0):
		return 0
	# numberOfPeopleRequredForStanding=peopleAtCurrentLevel*x
	result=0
	if(numberOfPeopleRequredForStanding>CurrentNumberOfPeopleStanding):
		result=numberOfPeopleRequredForStanding - CurrentNumberOfPeopleStanding
	# CurrentNumberOfPeopleStanding+=numberOfPeopleRequredForStanding
	CurrentNumberOfPeopleStanding+=peopleAtCurrentLevel+result
	return result

for i in range(numOfTestCase):
	numerOfPeoplePerShynessLevel=content.pop(0).split(" ")[1].replace('\n','')
	numberOfFriendsRequired,CurrentNumberOfPeopleStanding=0,0
	for numberOfPeopleRequredForStanding in range(len(numerOfPeoplePerShynessLevel)):
		numberOfFriendsRequired+=GetNumberOfPeopleRequireForShynesX(int(numerOfPeoplePerShynessLevel[numberOfPeopleRequredForStanding]),numberOfPeopleRequredForStanding)
		# print("numberOfFriendsRequired  int(numerOfPeoplePerShynessLevel[numberOfPeopleRequredForStanding])  numberOfPeopleRequredForStanding   "+str(numberOfFriendsRequired)+"   " +str(int(numerOfPeoplePerShynessLevel[numberOfPeopleRequredForStanding]))+"   "  +str(numberOfPeopleRequredForStanding)+"   ")
		# print(CurrentNumberOfPeopleStanding)
		# print("________________________________________________________________________")
	
	print("Case #"+str(i+1)+": "+str(numberOfFriendsRequired))
	