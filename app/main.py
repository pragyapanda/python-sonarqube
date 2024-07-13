from app.utils import greet_user

def main():
    user_name = input("Enter your name: ")
    print(greet_user(user_name))

if __name__ == "__main__":
    main()
