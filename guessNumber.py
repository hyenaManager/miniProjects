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

	def balanceEdit(self,modifier):
		if modifier == "+":
			self.user_balance +=5000
		else:
			self.user_balance -= 5000
class UserProfile:
	def __init__(self,user,plays,win,lost):
		self.user = user
		self.plays = plays
		self.win= win
		self.lost = lost

	def winrate(self):
		if self.plays == 0:
			return '0%'
		winratePer = (self.win*100)/self.plays
		return str(winratePer)+'%'
	def playE(self):
		self.plays +=1
	def winE(self):
		self.win +=1
	def lostE(self):
		self.lost+=1


def play(userS,user_profile):
	while True:
		user_input = input("enter 1 to play or enter 2 to look profile")
		if int(user_input)== 1:
			while True:
				guess=input(f"{userS.user_name} guess the number:")
				answer = random.randint(1,3)
				if int(guess)==answer:
					print("huray the answer is correct")
					userS.balanceEdit('+')
					user_profile.playE()
					user_profile.winE()
				else:
					print("wrong answer")
					print(f"answer is {answer}")
					userS.balanceEdit('-')
					user_profile.playE()
					user_profile.lostE()
				pOrExit = input("to play again enter>>1, to exit enter>>0:")
				if int(pOrExit) == 1:
					pass
				else:
					break
		elif int(user_input)==2:
			for user in gameData:
				users = gameData[str(user)]
				print(f'	__{users.user}__	')
				print(f'matches:	{users.plays}')
				print(f'win	   :	{users.win}')
				print(f'lost   :	{users.lost}')
				print(f'winrate:	{users.winrate()}')
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
			userData.update({username1:user})
			gameData.update({username1:user_profile})
			print("registeration success")
			print(userData)
			continue
		else:
			userName = input("please enter your userName:")
			if userName in userData:
				user1 = userData[str(userName)]
				print(user1.user_name)
				play(userData[str(userName)],gameData[str(userName)])
			else:
				print("incorrect user name please try again")

if __name__ == "__main__":
	main()