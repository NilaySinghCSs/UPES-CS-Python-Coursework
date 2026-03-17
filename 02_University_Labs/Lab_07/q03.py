data={"a":1,"b":2,"c":3}
print(data)
for key in list(data.keys()):
    print(f"{key}")
    if data[key]%2==0:
     data[key]+=5
     print(f"{data[key]=}")
    else:
     data[key]=data[key]*2
     print(f"{data[key]=}")
print(data)