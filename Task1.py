import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()

print("User Details:\n")

for user in users:
            name = user.get("name", "N/A")
            email = user.get("email", "N/A")
            address = user.get("address", {})
            street = address.get("street", "N/A")
            city = address.get("city", "N/A")
            
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Address: {street}, {city}\n")
