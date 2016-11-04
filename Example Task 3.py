def validate_number():
    while True:
        MyNumber = input("Please enter a number: ")
        try:
            valid_number = int(MyNumber)
            if 0 < valid_number < 31:
                break
            else:
                print("please enter a number between 1 & 30")

        except ValueError:
            print("Please enter a number!")

    print("Number entered",valid_number)
    MyNumber=int(MyNumber)
    return MyNumber;

#Create Monster Card
Name = input("What is the monster's name?")
Origin = input("Where did the monster come from?")
Description = input("Describe the monster: ")
print("Attack Force")
Attack = validate_number()
print("Magical Force")
Magical_Force = validate_number()
print("Magical Defence")
Magical_Defence = validate_number()
print("Defence")
Defence = validate_number()
print("Intelligence")
Intelligence = validate_number()
print("Health")
Health = validate_number()

#Print Monster Card
print("Monster Card")
print("\nName: ", Name)
print("Origin: ",Origin)
print("Description ",Description)
print("\nAttack Force: ",Attack)
print("Magical Force: ",Magical_Force)
print("Magical Defence: ",Magical_Defence)
print("Defence: ",Defence)
print("Intelligence: ",Intelligence)
print("Health: ",Health)