import numpy
users = {
    "username": "Gatik",
    "age": 18,
    "is_admin": True
}
print(users)

print(users.get("username"))
print(users.get("age"))
print(users.get("is_admin"))

users.pop("is_admin")
print(users)

users.update({"is_admin": True})
print(users)

for x in users:
    print(users[x])
