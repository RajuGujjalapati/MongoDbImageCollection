import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient)
mydb = myclient["mydatabase"]
print(mydb)

mycol = mydb['customers']
#print(mycol)
mydict = {'_id':{'name':'Raju', 'adress':'Bhavani nagar','loc':'banglore'}}
mylist = {
	'_id':1,
	Emp_ID: "10025AE336",
	Personal_details:{
		First_Name: "Radhika",
		Last_Name: "Sharma",
		Date_Of_Birth: "1995-09-26"
	},
	Contact: {
		e-mail: "radhika_sharma.123@gmail.com",
		phone: "9848022338"
	},
	Address: {
		city: "Hyderabad",
		Area: "Madapur",
		State: "Telangana"
	}
}
#print(mydb.list_collection_names())
x = mycol.insert_many(mylist)
######

#print(x.inserted_ids)
#for x in mycol.find({},{'address':1}):
# print(x)
dblist = myclient.list_database_names()


query={'address':'Valley 345'}

y=mycol.find(query)
for x in mycol.find(query):
    print(x)


#########sort#####
mydoc = mycol.find().sort('name',1)#for reverse -1
print(mydoc)

###
myquer = {'address':'Sky st 331'}
mydel = mycol.delete_many(myquer)
print(myquer)
print()
for y in mycol.find():
    print(y)




