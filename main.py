'''Welcome to the final project of SE factory FCS course
We will be implementing a social media network using graphs
while also using everything we learned trough out this course'''

#IMPORTS
from collections import deque

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
        if user.ID in self.userIDs:
            print("User ID already exists, please choose another one!")
        else:
            self.userIDs[user.ID]=user
        #here we assigned a set to store friends of each user.
        #it will remove duplicates and is easy to add and delete into.
            self.friends[user.ID]=set()
            print("User added successfully!")

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
            print("User deleted successfully")
        else:
            print("User ID does not exist.")

    #Function to add relationship between users.
    def friendsRelation(self,userID,userID2):
        if userID not in self.userIDs or userID2 not in self.userIDs:
            print("One or both user IDs do not exist.")
        elif userID2 in self.friends[userID]:
            print("Users are already friends")
        elif (userID and userID2) in self.userIDs:
            #for each user we add the other as his friend
            self.friends[userID].add(userID2)
            self.friends[userID2].add(userID)
            print("Friend added successfully!")

    #Function to remove relationship between users.
    def delFriendsRelation(self,userID,userID2):
        if userID not in self.userIDs or userID2 not in self.userIDs:
            print("One or both user IDs do not exist.")
        elif (userID and userID2) in self.userIDs:
            #each user we delete the other from the set of friends
            self.friends[userID].discard(userID2)
            self.friends[userID2].discard(userID)
            print("Friend removed successfully.")
        else:
            print("Friendship does not exist.")

    #sorting+Binary searching algorithm by ID
    #We are Performing binary search to find a user by their ID.
    #if found we return name and bio
    #if not found return nothing
    def binary_search_user_by_id(self, searchID):
        sortedIDs = sorted(self.userIDs.keys())
        left, right = 0, len(sortedIDs) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_id = sortedIDs[mid]
            if mid_id == searchID:
                user = self.userIDs[mid_id]
                print("User found:",user.name,user.bio)
                return user
            elif mid_id < searchID:
                left = mid + 1
            else:
                right = mid - 1
        return "User not found"


    # Recommend top friend based on mutual friends
    def recommend_friends(self, userID):
        if userID not in self.userIDs:
            return "User not found"
        user_friends = self.friends.get(userID, set())
        recommendations = {}
        for friend in user_friends:
            for potential_friend in self.friends.get(friend, set()):
                if potential_friend != userID and potential_friend not in user_friends:
                    if potential_friend not in recommendations:
                        recommendations[potential_friend] = 0
                    recommendations[potential_friend] += 1
        # Sort recommendations by the number of mutual friends in descending order
        sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
        # Return the top recommendations
        return [self.userIDs[rec[0]].name for rec in sorted_recommendations]

   #This is the BFS breadth first search algorithm that will search inside the friends relations.
    def bfs(self, startID):
        if startID not in self.userIDs:
            print("Starting ID does not exist.")
        visited = []
        queue = []
        visited.append(startID)
        queue.append(startID)
        while queue:
            userID = queue.pop(0)
            print(self.userIDs[userID].name, " ")
            for neighbour in self.friends[userID]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    #This is the DFS deapth first search algorithm that will search inside the friends relations.
    def dfs(self,startID):
        if startID not in self.userIDs:
            print("Starting ID dos not exisrt.")
        visited=[]
        stack=deque()
        visited.append(startID)
        stack.append(startID)
        while stack:
            userID=stack.pop()
            print(self.userIDs[userID].name," ")
            for neighbour in self.friends[userID]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


    '''

    DIJKSTRA'S ALGORITHM to-do

    '''

    
    '''
    CONNECTED COMPONENTS ALGORITHM

    '''

#END OF CLASS GRAPH

#Creation of class user
class User:
    #initialize object
    def __init__(self,name,ID):
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
    if userID in social_network.userIDs and userID2 in social_network.userIDs:
        if userID2 not in social_network.friends[userID]:
            social_network.friendsRelation(userID, userID2)
            social_network.userIDs[userID].addFriends(userID2)
            social_network.userIDs[userID2].addFriends(userID)
        else:
            print("Friendship already exists.")
    else:
        print("One or both user IDs do not exist.")

#remove a friend
def remove_friend(social_network,userID,userID2):
    social_network.delFriendsRelation(userID,userID2)
    social_network.userIDs[userID].removeFriends(userID2)
    social_network.userIDs[userID2].removeFriends(userID)

#add/ change user bio
def bioUpdate(social_network,userID,details):
    user= social_network.userIDs.get(userID)
    if user:
        user.addBio(details)
        print("Bio updated successfully.")
    else:
        print("User ID doesnt exist.")

#delete a user
def delete_user(social_network,userID):
    if userID in social_network.userIDs:
        social_network.delUsers(userID)
        print("User deleted successfully.")
    else:
        print("User does not exist.")




#Function that calculates statistics of the network
#it will calculate: num of users,num of friendships and avg friends per user.
def network_stats(social_network):
    num_users = len(social_network.userIDs)
    num_friendships = sum(len(friends) for friends in social_network.friends.values())
    avg_friends = num_friendships / num_users
    return "num users:",num_users,"num friendships:",num_friendships,"avg friends",avg_friends




def menu(social_network):
    print("""Welcome to the newest social media platform FRIENDFUSION, 
    created by Joseph Nassif for the FCS final project.""")
    while True:
        print("""Please choose one of the numbered options you would like to do:
1. Add user
2. Add friend
3. Remove friend
4. Update your bio
5. Delete User
6. Calculate network statistics
7. Binary search a user
8. Recommend a friend
9. Use BFS algorithm
10. Use DFS algorithm
11. Dijkastras algorithm
12. Exit
""")
        choice = input("Enter your choice (1-16): ")
        
        if choice == '1':
            name = input("Enter the user's name: ")
            userID = int(input("Enter the user's ID: "))
            add_user(social_network, name, userID)
            
        elif choice == '2':
            userID1 = int(input("Enter the first user's ID: "))
            userID2 = int(input("Enter the second user's ID: "))
            add_friend(social_network, userID1, userID2)
            
        elif choice == '3':
            userID1 = int(input("Enter the first user's ID: "))
            userID2 = int(input("Enter the second user's ID: "))
            remove_friend(social_network, userID1, userID2)
            
        elif choice == '4':
            userID = int(input("Enter the user's ID: "))
            bio_details = input("Enter the bio details (format: key1=value1,key2=value2): ")
            bio_dict = dict(item.split("=") for item in bio_details.split(","))
            bioUpdate(social_network, userID, bio_dict)
           
            
        elif choice == '5':
            userID = int(input("Enter the user's ID to delete: "))
            delete_user(social_network, userID)
           
            
        elif choice == '6':
            stats = network_stats(social_network)
            print("Network Statistics:")
            print(stats)
            
        elif choice == '7':
            userID = int(input("Enter the user's ID to search: "))
            result = social_network.binary_search_user_by_id(userID)
            print(result)
            
        elif choice == '8':
            userID = int(input("Enter the user's ID to recommend friends for: "))
            recommendations = social_network.recommend_friends(userID)
            print("Recommended friends:", recommendations)
            
        elif choice == '9':
            startID = int(input("Enter the starting user's ID for BFS: "))
            print("BFS starting from user with ID", startID)
            social_network.bfs(startID)
            
        elif choice == '10':
            startID = int(input("Enter the starting user's ID for DFS: "))
            print("DFS starting from user with ID", startID)
            social_network.dfs(startID)
            
        elif choice == '12':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please enter a number between 1 and 12.")


'''RUN THE PROGRAM'''

social_network=Graph()
menu(social_network)





