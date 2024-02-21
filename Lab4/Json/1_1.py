import json

with open("C:\\Users\\Cezar\\Desktop\\PY\\Lab4\\Json\\sample-data.json") as json_file:
    new_data = json.load(json_file)

print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
for item in new_data["imdata"]:
    print(item["l1PhysIf"]["attributes"]["dn"],"                            ",item["l1PhysIf"]["attributes"]["speed"]," ",item["l1PhysIf"]["attributes"]["mtu"])