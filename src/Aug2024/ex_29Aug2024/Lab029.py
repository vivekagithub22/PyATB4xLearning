""" Dictionary """
# 1. Dictionary contains Key and value
# 2. name -> "Pramod"
# 3. Dictionary is also an unordered collection of data

# can have multiple key and values
student_info = {
    "name" : "Pramod",
    "Age" : 25,
    "Address" : "TN",
    "Age" : 37 # latest value will be replaced
}

print(student_info)
print(student_info["name"])
print(student_info["Age"])
print(student_info["Address"])

student_info["Age"] = 100
print(student_info)

# another way to create dictionary list
stud_info = dict(name="Pramod", age=56, Address = "KA")
print(stud_info)

# dictionary inside dictionary
stu_info = {
    "address" : {
        "home address" : "TN",
        "Office address" : "KA"
    }
}

student_list = [stud_info,stu_info]
print(student_list)

# dictionary is very important in JSON format in API