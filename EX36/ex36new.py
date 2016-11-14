#out
def Canada(out):
    print out, "Good job!"
    exit(0)


#voting
def vote():
    print "This game takes place in a fictional place called the USA."
    print """You are a citizen of the United States of America, like any citizen \nwho lives in a democracy, you should vote whenever you have the right to."""
    print "You are in a voting booth, you can either vote for:"

    can = ["Hilary Clinton (1)", "Donald J. Trump (2)", "Dr. Jill Stein (3)", "Gary Johnson (4)", "'Other Candidates' (5)"]

    for i in can:
        print i

    vote = raw_input("\t >> ")

    if vote == "1" or vote == "3" or vote == "4" or vote == "5":
        print "Thank you for your vote."
    elif vote == "2":
        print """You're obviously not very good at making decision, go home \nand ask yourself how you can make your life great again."""
    else:
        print "Either the system is rigged or you're too dumb to vote..."

    print "Donald J. Trump has won the election."

    if vote == "1" or vote == "3" or vote == "4" or vote == "5":
        print "Thanks for trying though."

    print "You can 'continue' and be Donald J. Trump or 'move to Canada'."

    choice = raw_input("\t >> ")

    if choice == "move to Canada":
        Canada("You're out!")
    elif choice == "continue":
        print "Let's get started Donald!"
        jail()
    else:
        print "What was that?"
        print "Do you want to continue?"
        choice = raw_input("\t >> ")
        if choice == "yes":
            jail()
        else:
            Canada()


#end
def riots():
    print "Well, the thing is... Everyone is fighting you. The system is rigged."
    print "You lost the war against Mexico because no one fights for you anymore..."
    print "Everyone says you screwed up 'biggly'!"
    print "The USA are defeated, you ruined the country (because the system \nwas rigged against you)."
    print "You just got 'trumped'!"


#women
def women():
    print "So, you also wanted to take care of women."
    print "Do you still want to do that?"

    choice = raw_input("\t >> ")

    if choice == "yes":
        print "But women don't want you're help..."
        print "I have an idea! We should declare war on women."
        print "Genius. That's great."
        print "Almost all the women are in jail now, no women anymore."
        print "But the prisons are too full!"
        print "People are very upset about you. They want their wifes and \ndaughters back! There are riots everywhere."
    elif choice == "no":
        print "People are really upset about you. There are riots everywhere."
    else:
        print "I didn't get it... Do you still want it?"
        choice_two = raw_input("\t >> ")
        if choice == "yes":
            print "But women don't want you're help..."
            print "I have an idea! We should declare war on women."
            print "Genius. That's great."
            print "Almost all the women are in jail now, no women anymore."
            print "But the prisons are too full!"
            print "People are very upset about you. They want their wifes and \ndaughters back! There are riots everywhere."
        elif choice == "no":
                print "People are really upset about you. There are riots everywhere."
    print "Let's just move on right?."
    riots()


#poverty
def poverty():
    print "You wanted to end poverty right?"
    print "How are you going to do that?"

    choice = raw_input("\t >> ")

    if choice == "declare war on poverty":
        print "Great idea, you must have the best brain in the world."
        print "Let's put all the poor people in jail."
        print "See, you fixed it. No poor people on the streets anymore."
        print "You're one hell of a leader!"
    else:
        print "I know what you mean man..."
        print "But shouldn't we declare war on poverty?"
        choice_pov = raw_input("\t >> ")
        if choice_pov == "yes":
            print "Sounds great, you must have the best brain in the world."
            print "Let's put all the poor people in jail."
            print "See, you fixed it. No poor people on the streets anymore."
            print "You're one hell of a leader. America is great again."
        elif choice_pov == "no":
            print "So you don't want it to change?"
            print "You really suck, people are really angry now."
        print "That's how you do it. What's next?"
    women()


#wall
def wall():
    print "You also promised to build a wall on the border to Mexico."
    print "Do you still want to do that?"

    choice = raw_input("\t >> ")

    if choice == "yes":
        print "Mexico doesn't want to pay."
        print "Do you want the USA to pay?"
        choice_pay = raw_input("\t >> ")
        if choice_pay == "yes":
            print "Woaw that's a lot of money and we don't have it."
            print "People are upset!"
        elif choice_pay == "no":
            print "Declare war to Mexico?"
            choice_war = raw_input("\t >> ")
            if choice_war == "yes":
                print "Yay we're at war, America is great again already!"
                print "Alright, we fixed that. Good job!"
            elif choice_war == "no":
                print "Well we're going to pay ourselves then..."
                print "Too bad, people don't like that, they are very upset!"
    elif choice == "no":
        print "Too bad, the people are angry!"
    else:
        print "Anyway..."
    print "Next issue."
    poverty()


#jail
def jail():
    print "First things first: you promised to put Hilary Clinton in jail."
    print "Do you still want to do it?"

    choice = raw_input("\t >> ")

    if choice == "yes":
        print "Great, that's the first step to dictatorship. Way to go buddy!"
    elif choice == "no":
        print "Too bad, the people are upset!"
    else:
        print "You should really play along man! Just type 'yes' or 'no'."
        print "Do you still want to do it?"
        choice_real = raw_input("\t >> ")
        if choice == "yes":
            print "Way to go buddy!"
        elif choice == "no":
            print "Too bad, the people are disappointed!"
    wall()


vote()
