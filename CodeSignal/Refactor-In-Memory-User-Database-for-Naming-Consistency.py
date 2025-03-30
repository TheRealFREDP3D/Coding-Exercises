"""
**Good Naming at a Glance**

**Reveal Intent Through Names**:
Ensure names clearly convey the role and functionality of variables, classes, and functions. For instance, replacing calc with calculate_interest enhances code clarity. 🧠

**Avoid Misleading Names**:
Avoid names that imply incorrect assumptions, such as using user_list for a set, ensuring accuracy and understanding. 🚫

**Choose Descriptive**:

**Searchable Names**:
Opt for names like age instead of a, facilitating easy searchability and recognition within the codebase, which enhances maintainability. 🔍

**Consistent Naming Across the Codebase**:
Use uniform patterns like get_all_users instead of varied terms such as fetch_all_users, maintaining clarity and preventing confusion. 📚

**Provide Sufficient Context in Names**:
Include enough context, such as using file_size instead of size, to eliminate ambiguity, especially when components are used across different contexts. 🌐
"""


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name


class UserInMemoryDatabase:
    def __init__(self):
        self.user_set = []

    def add_user(self, user):
        self.user_set.append(user)

    def get_user(self, name):
        for user in self.user_set:
            if user.name == name:
                return user
        return None

    def retrieve_all_users(self):
        return self.user_set

    def remove_user(self, name):
        self.user_set = [user for user in self.user_set if user.name != name]

    def delete_all_users(self):
        self.user_set.clear()


def main():
    user_db = UserInMemoryDatabase()
    user_db.add_user(User(1, "Alice"))
    user_db.add_user(User(2, "Bob"))
    for user in user_db.retrieve_all_users():
        print(user.name)  # Outputs all users

    user = user_db.get_user("Alice")
    if user:
        print("Found user:", user.name)
    else:
        print("User not found")

    user_db.remove_user("Alice")
    for user in user_db.retrieve_all_users():
        print(user.name)  # Outputs remaining users

    user_db.delete_all_users()
    for user in user_db.retrieve_all_users():
        print(user.name)  # Outputs an empty list


if __name__ == "__main__":
    main()
