'''Welcome to the final project of SE factory FCS course
We will be implementing a social media network using graphs
while also using everything we learned trough out this course'''

#Create a Class Graph that will contain functions regarding the object graph

class Graph:
    #We initialized the object graph that will have 2 dictionaries,
    #a userID (contain user IDs) and a 
    #friends(links user IDs to friends IDs).
    def __init__(self):
        self.userIDs={}
        self.friends={}
    
    #We need a function to add new users.
    def addNewUser(self,user):
        self.userIDs[userId]=user
        #here we assigned a set to store friends of each user.
        #it will remove duplicates and is easy to add and delete into.
        self.friends[userId]=set()

    #We need a function to delete users.
    def delUsers(self,userID):
        if userID in self.userIDs:
            del self.userIDs[userID]
            del self.friends[userID]
            #let i be the set in the dict friends.
            #we used the discard function because in case
            #there is no match in value, no error is raised. 
            for i in self.friends.values():
                i.discard(userID)

    
    
    

