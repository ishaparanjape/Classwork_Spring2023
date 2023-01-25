print("This is the blood_calculator.py file")
print("Python thinks this is called {}".format(__name__))

##variable and function names have to be different

##interface function
def interface():
	print("Blood calculator")
	keep_running = True
	while keep_running:
        #print("Options:")
        #print("1 - HDL")
        #print("2 - LDL")
        #print("3 - Total Cholesterol")
        #print("9 - End Program")
        
        choice = input("Select an option:")
	    if choice == "9":
			keep_running = False
		elif choice == "1":
            HDL_driver()
        elif choice == "2":
			LDL_driver()
		elif choice == "3":
			TotChol_driver()
	print("Program ending")

##HDL analysis
def HDL_driver():
    HDL_in = HDL_input()
	HDL_analy = HDL_analysis(HDL_in)
	HDL_output(HDL_in, HDL_analy)

def HDL_input():
	HDL_value = input("Enter the HDL result:")
	HDL_value = int(HDL_value)
	return HDL_value

def HDL_analysis(HDL_int):
	if HDL_int >= 60:
		answer = "Normal"
	elif 40 <= HDL_int < 60:
		answer = "Borderline Low"
	else:
		answer = "Low"
	return answer
	
#def generic_output(test_name, test_value, test_analy)
	#print("The {} result of {} is considered {}

def HDL_output(HDL_value, HDL_analy):
	print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
	return

##LDL analysis
def LDL_driver():
	LDL_in = LDL_input()
	LDL_analy = LDL_analysis(LDL_in)
	LDL_output(LDL_in, LDL_analy)

def LDL_input():
	LDL_value = input("Enter the LDL result:")
	LDL_value = int(LDL_value)
	return LDL_value

def LDL_analysis(LDL_int):
	if LDL_int < 130:
		answer = "Normal"
	elif 130 <= LDL_int <= 159:
		answer = "Borderline High"
	elif 160 <= LDL_int <= 189:
		answer = "High"
	else:
		answer = "Very High"
	return answer 

def LDL_output(LDL_value, LDL_analy):
	print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))
	return

##total cholesterol analysis
def TotChol_driver():
	HDL_in = HDL_input()
	LDL_in = LDL_input()

	totchol = HDL_in + LDL_in
	if totchol < 200:
		answer = "Normal"
	elif 200 <= totchol <= 239:
		answer = "Borderline High"
	else:
		answer = "High"
		
	print("The Total Cholesterol vlaue of {} is considered {}".format(totchol, answer))
	return

if __name__ == "__main__":
    interface()