student={
    "name":"bablu",
    "subject":{
        "math":67,"phy":53,"che":47
    }
}
print(type(student))
print(student)
print(student["subject"])
print(student["subject"]["che"])

print(list(student.keys()))
print(len(student))
print(student.values())
print(student.get("subject"))
student.update({"name":"mahitha"})
print(student)
