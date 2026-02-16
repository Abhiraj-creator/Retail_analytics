from database import create_tables
from analatics import revenue
create_tables()
print("progress successfully done")

while True:
    print("Enter 1 for Total Revenue")
    print("Enter 2 for Exit")
    choice = input ("Enter choice :")
    if choice == "1":
        print("Total Revenue",revenue())
    elif choice== "2":
        break
    