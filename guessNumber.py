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

	def register(self):
		userData.update()
		print("registeration success....")
def play(user_name):
	user_input = input("enter 1 to play")
	if int(user_input) == 1:
		while True:
			guess=input("guess the number:")
			answer = random.randint(1,7)
			if guess==answer:
				print("huray the answer is correct")
				gameData.update()
				print(gameData)
			else:
				print("wrong answer")
				gameData.update({user_name:{"player":'name',"guess":guess,"success":False,"answer":answer,"id":len(gameData)}})
				print(gameData)
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
			userage1 = input("user age:")
			userbalance1 = input("user balance:")
			userR = User(username1,userage1,userbalance1)
			userR.register()
			print("registeration success")
			print(userData)
			continue
		else :
			userName = input("please enter your userName:")
			if userName in userData:
				play(userName)
			else:
				print("incorrect user name please try again")

if __name__ == "__main__":
	main()