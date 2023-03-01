import requests

#out_data = {"name": "Isha Paranjape", "net_id": "ip68", "e-mail": "ip68@duke.edu"}
#r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)
#print(r.status_code)
#print(r.text)


out_data = {"user": "yc551", "message": "Hello"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json = out_data)
print(r.status_code)
print(r.text)
r2 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/yc551")
print(r2.text)