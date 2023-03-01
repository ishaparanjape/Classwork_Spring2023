import requests

server = "http://vcm-7631.vm.duke.edu:5002"

patient_data = requests.get(server + "/get_patients/ip68")
print(patient_data.text)

rec = requests.get(server + "/get_blood_type/M4")
donor = requests.get(server + "/get_blood_type/M5")
rec_bt = rec.text
donor_bt = donor.text
#print(rec.text)
#print(donor.text)

match = None
if rec == donor:
    match = "Yes"
else:
    match = "No"

#match_check = None
#if match == "Yes":
#    match_check = "Correct"
#else:
#    match_check = "Incorrect"

bt_match_data = {"Name": "ip68", "Match": match}
post_data = requests.post(server + "/match_check", json=bt_match_data)
print(post_data.text)