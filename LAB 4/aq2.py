import json

#Sample JSON DATA
data={
    "id":53,
    "name":"Ankit Mishra",
    "regno":200953214,
    "branch":"CCE"
}


#conversion of JSON to string
y=json.dumps(data)
print(y, type(y))



#now since variable y is holding String, we will convert that back to JSON
new_data=json.loads(y)
print(new_data, type(new_data))