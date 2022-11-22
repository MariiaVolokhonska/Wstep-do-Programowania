sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for key,value in sample_dict.items():
 print(f'{key:<10},":",{value:>10}')
for key in sample_dict.keys():
 print(key,sample_dict[key])
newdict={}
l1=["age","salary","name"]
for key in l1:
 if key in sample_dict:
  newdict[key]=sample_dict[key]
  sample_dict.pop(key)

print(newdict)
print(sample_dict)
if "Jones" in sample_dict.values():
 print("yeeep")
else: print("nie(")


sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)


