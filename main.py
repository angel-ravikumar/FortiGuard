username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "forti123":

    print("✅ Level 1 Passed")

    pin = input("Enter 4-digit PIN: ")

    if pin == "1234":

        print("✅ Level 2 Passed")

        answer = input("What is your favourite colour? ")

        if answer.lower() == "blue":

            print("✅ Level 3 Passed")
            print("🎉 ACCESS GRANTED 🎉")

        else:

            print("❌ Level 3 Failed")

    else:

        print("❌ Level 2 Failed")

else:

    print("❌ Level 1 Failed")