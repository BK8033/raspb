import requests
import time

def main():
	url = 'http://52.43.95.248:5365/pirequest'
	##############################
	#       RESPONSE CODE        #
	#                            #
	#    1: Predict Sick         #
	#    2: Predict Sleep        #
        #    3: Final Sick           #
        #    4: Final Sleep          #
	#                            #
	##############################
	while True:
		try:
			res = requests.get(url,timeout=3)
			time.sleep(1)
			res_code = res.json()['code']
			if res_code  == 1:
				predict_sick()
			elif res_code == 2:
				predict_sleep()
			elif res_code == 3:
				final_sick()
			else:
				final_sleep()
		except requests.exceptions.Timeout:
			print('TIME OUT')
		except Exception:
			time.sleep(1)




def predict_sick():
	########## AI predicts that occupant is sick ###########
	print('AI Prediction: sick')

def predict_sleep():
	########## AI predicts that occupant is sleep ##########
	print('AI Prediction: sleep')

def final_sick():
	########## Final Decision: Occupant is sick ##########
	return 0
def final_sleep():
	########## Final Decision: Occupant is sleep ##########
	return 0

















if __name__=='__main__':
	main()
