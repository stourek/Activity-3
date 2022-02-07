#Scott Tourek
#ISQA 3900 2/6/22
#This is a program to calculate somesone's grade based on their total points


# Displays the title
def display_title() :
    print("Welcome to the grade calculator")

# Asks for total points and figures the average
def get_totalPoints() :
   number = int(input("Enter total accumulated points: "))
        if number >= 0 and number <= 1000:
            tavg = (number/1000)*100
            return tavg
        else:
            print("Invalid Input! Must be between 0 and 1000. Please enter a new value")
            main()


def get_letterGrade(tavg) :

        if tavg>=92 and tavg<=100:
            print("Your Grade is A")
            main()
        elif tavg>=88 and tavg<91.99:
            print("Your Grade is B+")
            main()
        elif tavg>=82 and tavg<87.99:
            print("Your Grade is B")
            main()
        elif tavg>=78 and tavg<81.99:
            print("Your Grade is C+")
            main()
        elif tavg>=70 and tavg<77.99:
            print("Your Grade is C")
            main()
        elif tavg>=60 and tavg<69.99:
            print("Your Grade is D")
            main()
        else:
            print("Your Grade is F")
            main()

#main method
def main() :
    display_title()
    get_totalPoints()
    get_letterGrade(tavg)


