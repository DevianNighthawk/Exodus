import json


def recursive_items(dct):
	for key,value in dct.items():
		if type(value) is dict:
			yield (key,value)
			yield from recursive_items(value)
		else:
			yield (key,value)

def json_to_dict(annotation_file):
	with open(annotation_file) as f:
		data = json.load(f)
	return data

def recursive_key_value(dct):
	rec_keys=[]
	values=[]
	for k,v in recursive_items(dct):
		rec_keys.append(k)
		values.append(v)
	return (rec_keys,values)

def preproc_key_values(keys,values):
	new_keys=[]
	new_values=[]
	for i in range(len(values)):
		if i>0:
			new_keys.append(keys[i])
			new_values.append(values[i])
	
	return (new_keys,new_values)

def remap_nested_keys(keys, values):
	dct={}
	amount_keys=len(keys)
	for i in range(amount_keys):
		dct[keys[i]]=values[i]
	return dct


def region_key_values(regions_dct):
	pass

data2=json_to_dict("via_project_2Aug2020_13h29m_json.json")
print("another json dictionary: ",data2)
data=json_to_dict("via_project_29Jul2020_9h23m_json.json")

#with open('via_project_29Jul2020_9h23m_json.json') as f:
	#data = json.load(f)



#for k,v in rec


#print(type(data))
#print(data)
#print(json.dumps(data,indent=4,sort_keys=True))
#data_keys = data.keys()
#print(data_keys)
#rec_keys=[]
#values=[]
#for k,v in recursive_items(data):
	#print ("key:",k)
	#rec_keys.append(k)
	#values.append(v)
	#print("value:",v)
rec_keys,values=recursive_key_value(data)
rec_keys2,values2=recursive_key_value(data2)
print("----")
print(rec_keys2)
print("----")


#new_keys=[]
#new_values=[]
#for i in range(len(values)):
	#if i>0:
		#new_keys.append(rec_keys[i])
		#new_values.append(values[i])
	#print("i: ",i)
	#print("key: ",rec_keys[i])
	#print("value:",values[i])
new_keys,new_values=preproc_key_values(rec_keys,values)
nk,nv = preproc_key_values(rec_keys2,values2)

#nk=[]
#nv=[]
#for i in range(len(values2)):
	#if i>0:
		#nk.append(rec_keys2[i])
		#nv.append(values2[i])
	#print("i: ",i)
	#print("key: ",rec_keys2[i])
	#print("value :",values2[i])
#print("keys: ")
#print(nk)
#print("values: ")
#print(nv)
#print("*"*10)
#print(new_keys)
#print(new_values)
#print("*"*10)

dct=remap_nested_keys(new_keys,new_values)
#print(type(dct))
#for i in range(len(new_keys)):
	#dct[new_keys[i]]=new_values[i]

dct2=remap_nested_keys(nk,nv)
#for i in range(len(nk)):
	#dct2[nk[i]]=nv[i]

#print("dct2 keys: ",dct2.keys())
#print("dct2 values: ",dct2.values())
##print("dct2 regions: ",dct2["regions"])
#print("*"*10)
#print(len(dct["regions"]))
#print("*"*10)
#regions_dct_orig=dct["regions"]
#r_keys=[]
#r_values=[]
#for k,v in recursive_items(regions_dct_orig):
	#r_keys.append(k)
	#r_values.append(v)


#print("region keys: ",r_keys)
#print("region values: ",r_values)

r_k=[]
r_v=[]
r_k2=[]
r_v2=[]
iCard3=len(dct2["regions"])
#print("xxxx")
#print(dct2["regions"])
#print("xxxx")
print("iCard3: ",iCard3)
region_amount=len(dct["regions"])
print("region_amount: ",region_amount)
r_k_card=len(dct["regions"][0].keys())
regions_dct_lst=[{} for i in range(len(dct["regions"]))]
iCard1=len(dct["regions"])
#print("iCard1: ",iCard1)
#iCard2=dct["regions"][1].keys()
#print("iCard2")
#print(iCard2)
#regions_dct_lst_z=[{} for i in range(2*5)]
#print("regions_dct_lst_z: ",regions_dct_lst_z)
print("rk_card: ",r_k_card)
r_v_dictlst=[]
for k,v in recursive_items(dct["regions"][0]):
	r_k.append(k)
	r_v.append(v)
	#r_v_dictlst.append({0: v})

#for e in r_v:
	#r_v_dictlst.append({0: e})

#print(r_v_dictlst)

for k,v in recursive_items(dct["regions"][1]):
	#r_k.append(k)
	r_v.append(v)
	#r_v_dictlst.append({1:v})
#for e in r_v:
	#r_v_dictlst.append({1:e})

for k,v in recursive_items(dct2["regions"][0]):
	r_k2.append(k)
	r_v2.append(v)

for k,v in recursive_items(dct2["regions"][1]):
	r_v2.append(v)
for k,v in recursive_items(dct2["regions"][2]):
	r_v2.append(v)
for k,v in recursive_items(dct2["regions"][3]):
	r_v2.append(v)





print("r_k2: ",r_k2)
print("r_v2: ",r_v2)


#print("r_k")
#print(r_k)
#print("r_k length")
r_k_leng=len(r_k)
r_v_leng=len(r_v)
r_v_2_leng=len(r_v2)
#print("r_v_leng: ",r_v_leng)
print("r_v_2_leng: ",r_v_2_leng)
#print(len(r_k))
#print("r_v")
#print(r_v)


#print(regions_dct_lst)
#print("*"*10)
#print(dct["regions"])
#print("*"*10)

#lst_z=[{} for i in range(iCard1*r_k_leng)]
lst_z=[{} for i in range(r_v_leng)]
lst_zz=[{} for i in range(r_v_2_leng)]
#print("==============")
#print(iCard1*r_k_leng)
#print("==============")
#print("list z: ",lst_z)
#print(json.dumps(dct,indent=4,sort_keys=True))
#for i in range(len(dct["regions"])):
	#regions_dct[i]=dct["regions"][i]
dividends=[]
remainders=[]
for i in range(len(lst_z)):
	#print("%"*10)
	#print(i%iCard1)
	#print("%"*10)
	#print(i//iCard1)
	dividends.append(i//iCard1)
	remainders.append(i%iCard1)
	lst_z[i][i%iCard1]="--"


dd=[]
rr=[]
for i in range(len(lst_zz)):
	dd.append(i//iCard3)
	rr.append(i%iCard3)
	lst_zz[i][i%iCard3]="cc"
#print(lst_z)
#print(dividends)
#print(remainders)

print(lst_zz)
r_k_dict={}
#print("recap r_k")
#print(r_k)
for i in range(len(r_k)):
	r_k_dict[i]=r_k[i]

r_k_dict2={}
for i in range(len(r_k2)):
	r_k_dict2[i]=r_k2[i]

print("r_k_dict2: ",r_k_dict2)
#print(r_k_dict)
#print("r_v recap")
#print(len(r_v))
#print(len(dividends))

#for i in range(len(dividends)):
	#print(lst_z[i][remainders[i]])
	#lst_z[i][remainders[i]]=r_v[i]


#print(r_v_dictlst)

#print(r_v_dictlst)

#print(lst_z)
#print(r_k_leng)
#for i in range(len(lst_z)):
	#print(lst_z[i])

#print(r_v_dictlst)
#for j in range(len(r_v_dictlst)):
	#print(r_v_dictlst[i])
#print("----")
#print(len(r_v))
#print("----")

iCount=0
dctlst2=[]
print("r_v2 keys: ",r_v2[0].keys())
for i in range(len(r_v2)):
	print("i :",i)
	print(type(r_v2[i]))
	if ( type(r_v2[i]) == dict and ("name" in r_v2[i].keys() )):
		iCount+=1
	dctlst2.append({iCount: r_v2[i]})
print("iCount: ",iCount)


iRegion_cnt=0
dctlst=[]
print("r_v keys: ",r_v[0].keys())
for i in range(len(r_v)):
	#print(type(r_v[i]))
	#print(iRegion_cnt)
	#dctlst.append({iRegion_cnt: r_v[i]})
	if ( type(r_v[i]) == dict and ("name" in r_v[i].keys() )):
		#print(r_v[i].keys())
		iRegion_cnt+=1
		#dctlst.append({iRegion_cnt: r_v[i]})
	dctlst.append({iRegion_cnt: r_v[i]})
	#print(r_v[i])

#print(iRegion_cnt)
remainders.sort()
#print(remainders)
new_dct={}
new_dct_lst=[]
for i in range(len(dctlst)):
	k=list(dctlst[i].keys())[0]
	#print("-------")
	#print(dctlst[i])
	#print("-------")

	#print("*"*10)
	r={k-1:dctlst[i][k]}
	new_dct_lst.append(r)
	#print("*"*10)
	#print("x")
	#print("r: ",r)
	#print("x")
	#print(lst_z[i])
#print("r type: ")
#print(type(r))
rr.sort()
new_dct_lst2=[]
for i in range(len(dctlst2)):
	print("dctlst2 keys: ")
	print(dctlst2[i].keys())
	k=list(dctlst2[i].keys())[0]
	print("k: ",k)
	r={k-1:dctlst2[i][k]}
	new_dct_lst2.append(r)

#print("r_k recap")
print("%"*10)
print("amount of remainders: ")
print(len(remainders))
print(len(new_dct_lst))
for i in range(len(new_dct_lst)):
	print(new_dct_lst[i])
print("%"*10)

print("----------------------")

for i in range(len(new_dct_lst)):
	#print("*")
	#print(remainders[i])
	#print("*")
	print(new_dct_lst[i][remainders[i]])
print("------------------------")
print(rr)
print(new_dct_lst2)

print("*"*10)
for i in range(len(new_dct_lst2)):
	print(new_dct_lst2[i])
print("*"*10)

for i in range(len(new_dct_lst2)):
	print(rr[i])
	print(new_dct_lst2[i][rr[i]])
#for i in range(len(dctlst)):
	#print(dctlst[i])
#print(regions_dct)
#for i in range(len(regions_dct_lst)):
	#regions_dct_lst[i][i]=[r_v[1],r_v[2],r_v[3],r_v[4]]




#print(regions_dct_lst)


#print("*"*10)
#print(len(dct["regions"]))
#print("*"*10)

"""
print("===")
print(rec_keys)
print("===")
print("***")
print(values)
print("***")
"""
#rec_keys = rec_keys[1:]
#print(rec_keys)

#for k in rec_keys:
	#print("=====")
	#print(data[k])
	#print("=====")

#print(rec_keys)

#print(values)
#print("length of values: ")
#print(len(values))
