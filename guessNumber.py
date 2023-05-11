import time
import random
gameData = {}
userData = {}

class User:
	def __init__(self,user_name,user_age,user_balance,user_id):
		self.user_name = user_name
		self.user_age = user_age
		self.user_balance = user_balance
		self.user_id = user_id

	def __str__(self) -> str:
		return self.user_name

	def balanceEdit(self,value,modifier):
		if modifier == "+":
			self.user_balance +=value
		else:
			self.user_balance -= value
class UserProfile:
	def __init__(self,user,plays,win,lost):
		self.user = user
		self.plays = plays
		self.win= win
		self.lost = lost

	def winrate(self):
		winratePer = (self.win*100)/self.plays
		return winratePer
	def plays(self):
		self.plays +=1
	def win(self):
		self.win +=1
	def lost(self):
		self.lost+=1
def play(user,user_profile):
	user_input = input("enter 1 to play")
	if int(user_input) == 1:
		while True:
			guess=input(f"{user.user_name} guess the number:")
			answer = random.randint(1,7)
			if int(guess)==answer:
				print("huray the answer is correct")
				user_profile.plays()
				user_profile.win()
				print(gameData)
			else:
				print("wrong answer")
				user_profile.plays()
				user_profile.lost()
			pOrExit = input("to play again enter>>1, to exit enter>>0:")
			if pOrExit == 1:
				continue
			else:
				break
def main():
	while True:
		loginOregister = input("login for 1 and register for 2: ")
		if int(loginOregister) == 2:
			username1 = input("user name:")
			if username1 in userData:
				print("user name already exist try another name")
				continue
			userage1 = input("user age:")
			userbalance1 = input("user balance:")
			user = User(username1,userage1,userbalance1,len(userData))
			user_profile = UserProfile(user,0,0,0)
			userData.update({username1:{user}})
			gameData.update({username1:{user_profile}})
			print("registeration success")
			print(userData)
			continue
		else:
			userName = input("please enter your userName:")
			if userName in userData:
				play(userData[str(userName)],gameData[str(userName)])
			else:
				print("incorrect user name please try again")

if __name__ == "__main__":
	main()