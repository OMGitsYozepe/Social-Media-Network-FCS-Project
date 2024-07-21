'''Welcome to the final project of SE factory FCS course
We will be implementing a social media network using graphs
while also using everything we learned trough out this course'''

#Create a Class Graph that will contain functions regarding the relationships
#between users.

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

    #Function to add relationship between users.
    def friendsRelation(self,userID,userID2):
        if (userID and userID2) in self.userIDs:
            #for each user we add the other as his friend
            self.friends[userID].add(userID2)
            self.friends[userID2].add(userID)

    #Function to remove relationship between users.
    def delFriendsRelation(self,userID,userID2):
        if (userID and userID2) in self.userIDs:
            #each user we delete the other from the set of friends
            self.friends[userID].discard(userID2)
            self.friends[userID2].discard(userID)

#END OF CLASS GRAPH

#Creation of class user
class User:
    #initialize object
    def__init__(self,name,ID):
        self.name=name
        self.ID=ID
        self.friends=set()
        #dictionary, it could include interests,country,age...
        self.bio={}

    #function to add friends.
    def addFriends(self,friendID):
        self.friends.add(friendID)
    
    #function to remove friends.
    def removeFriends(self,friendID):
        self.friends.remove(friendID)
    
    #function to add/update a bio to your profile
    def addBio(self,details):
        self.bio.update(details)


#END OF CLASS USER



#Creation of basic operations functions


#add a new user
def add_user(social_network,name,userID):
    newUser= User(name,userID)
    social_network.addNewUser(newUser)

#add a new friend
def add_friend(social_network,userID,userID2):
    social_network.friendsRelation(userID,userID2)
    social_network.userIDs[userID].addFriends(userID2)
    social_network.userIDs[userID2].addFriends(userID)

#remove a friend
def remove_friend(social_network,userID,userID2):
    social_network.delFriendsRelation(userID,userID2)
    social_network.userIDs[userID].removeFriends(userID2)
    social_network.userIDs[userID2].removeFriends(userID)

#add/ change user bio
def bioUpdate(social_network,userID,details):
    user= social_network.userIDs.get(userID)
    if user is True:
        user.addBio(details)

#delete a user
def delete_user(social_network,userID):
    social_network.delUsers(userID)



'''GRAPH
ALGORYTHMS
TO - DO
LATER
'''


'''SORTING 
AND SEARCHING 
USERS'''


#Function that calculates statistics of the network
#it will calculate: num of users,num of friendships and avg friends per user.
def network_stats(social_network):
    num_users = len(social_network.userIDs)
    num_friendships = sum(len(friends) for friends in social_network.friends.values())
    avg_friends = num_friendships / num_users
    return "num users:",num_users,"num friendships:",num_friendships,"avg friends",avg_friends



'''
Reccomend friend
'''




