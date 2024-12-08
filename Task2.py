import requests

def fetch_users():
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        return response.json()


def filter_users(users, search_term):
    search_term = search_term.lower()
    return [
        user for user in users
        if search_term in user.get("name", "").lower()
    ]

def print_users(users):
    
    print("\nFiltered User Details:")
    for user in users:
        name = user.get("name", "N/A")
        email = user.get("email", "N/A")
        address = user.get("address", {})
        street = address.get("street", "N/A")
        city = address.get("city", "N/A")
        
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Address: {street}, {city}\n")

def main():
    users = fetch_users()
    if users:
        search_term = input("Enter keyword to filter users by name: ")
        filtered_users = filter_users(users, search_term)
        if filtered_users:
            print_users(filtered_users)
        else:
            print("Users are not found.")

main()
