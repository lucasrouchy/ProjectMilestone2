 def decision():

        while True:
            prompt = "Would you like to travel to a random planet? "
            print(prompt)
            choice = input("Y or N ")
            

            if choice.upper() in ['Y','N']:
                
                break
            else:
                print("Sorry I didn't get that")
        return choice
def getplanet(choice):
        planet = None
        if choice == 'Y':
            print("Travelling to Pluto...")
            print("arrived at pluto the ninth-largest and tenth-most-massive known object directly orbiting the Sun.")
        else:
            planet =input("What planet would you like to travel? ")
        return planet
def planetdesc(planet):

    if planet == "Earth":
        print("arrived at Earth is the third planet from the Sun and the only astronomical object known to harbour and support life.")
    elif planet == "Mars":
        print("arrived at Mars the fourth planet from the Sun and the second-smallest planet in the Solar System")
    elif planet == "Mercury":
        print("arrived at Mercury the smallest planet in the Solar System and the closest to the Sun")
    elif planet == "Venus":
        print("arrived at Venus the second planet from the Sun. It is named after the Roman goddess of love and beauty.")
    elif planet == "Saturn":
        print("arrived at Saturn the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth")
    elif planet =="Jupiter":
        print("arriving at Jupiter the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined")
    elif planet == "Neptune":
        print("arriving at Neptune the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet")
    elif planet == "Uranus":
        print("arriving at Uranus the seventh planet from the Sun. Its name is a reference to the Greek god of the sky")
        print("Hello traveler welcome to the milky way galaxy where we have 9 planets if you include pluto")
    
    name= input("Enter your name ")
    print(name)
    print("Nice to meet you "+ name + " my name is Eliza, Alexas evil assistant")
    
    choice = decision()
    planet = getplanet(choice)
    planetdesc(planet)