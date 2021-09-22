print('''
***************************************************************************
           .          .
 .          .                  .          .              .
       +.           ______  .        .        + .                    .
   .        .   ,-~"       "~-.                                +
              ,^ ___           ^. +                  .    .       .
             / .^   ^.           \         .      _ .
            Y  l  o  !            Y  .         __CL\H--.
    .       l_ `.___.'        _,  [           L__/_\H' \\--_-          +
            |^~"-----------""~ ^  |       +    __L_(=): ]-_ _-- -
  +       . !                     !     .     T__\ /H. //---- -       .
         .   \                   /               ~^-H--'
              ^.               .^            .      "       +.
                "-.._____.,-" .                    .
         +           .                .   +                       .
  +          .             +                                  .
         .             .      .       -Row
                                                        .
***************************************************************************
''')
input("INSTRUCTION! \n Just type a letter of choice, and press ENTER.\n To start the game, press Enter!\n")
print("Welcome to the Rogue Wars")
print("Your mission is to destroy the Deathstar!")
mission_incomplete = "MISSION INCOMPLETE"

name = input("Type your name soldier: ")
print(f"\n\nWelcome {name}\nYour goal is:\n"
      f"- find a way inside and infiltrate the most important target \n"
      f"the Deathstar!\n"
      f"Now is the greatest time, as our spy said, there will be increased maintenance activity\n"
      f"so some actions will not cause the security to react.\n"
      f"Our Spy said at this time the working maintenance doors are in the south\n"
      f"- If you get in, you need to plant a bomb in the main reactor chamber and flee unseen\n"
      f"But watch out! There are some traps like LaserDetectionSystems,\n"
      f" eye-scanning, cameras and Troops!\n"
      f"Get into the Rescue/Recon ship and good luck, {name}!\n\n")

wait = input("ARE YOU READY? When ready press enter\n")

action = input("The pilot: Where do you will to be dropped?\n"
               "type: E - to pick east side. N - north side or S - south side.\n"
               "After choosing press enter:\n")
action = action.upper()
if action == "S":
    action = input(f"\nYou are near the Maintenance door, what you want to do?\n"
                   f"B for Breach in, H for Hide and wait, O for Open the door\n")
    action = action.upper()
    if action == "H":
        print("\nThe worker came the doors are left open")
        action = input("What you want to do? \n"
                       "E - Engage with the worker,\n"
                       "D - Distract him with a stone\n"
                       "S - Sneak in\n")

        action = action.upper()
        if action == "S":
            print("\nYou're in! You've looked around and you choose your path\n")
            action = input("C - open the ceiling and go along green pipes\n"
                           "F - open the floor and go along with black cables\n"
                           "R - you see a reactor sign pointing left, go this direction\n")

            action = action.upper()
            if action == "C":
                print("\nYou've been sneaking for about 5 min now, but you are in the crossing\n"
                      "Choose the way you want to go")
                action = input("B - Go where the pipes are getting bigger\n"
                               "F - Go back to the Floor\n"
                               "S - Go where the pipes are getting smaller\n")
                action = action.upper()
                if action == "B":
                    print("\nYou are in the Reactor chamber. You plant the bomb,\n"
                          "but you need to set the time for the explosion\n")
                    action = input("10 - for 10 minutes\n"
                                   "2 - for 2 hours\n"
                                   "20 - for 20 seconds\n")
                    action = action.upper()
                    if action == "10":
                        print("\nNow you need to evacuate quickly...\n"
                              "whats the plan?")
                        action = input("C -Call command to pick you up while you sneaking out to randezvous point\n"
                                       "R - Run to randezvous point and call command for pick up\n"
                                       "S - Call command to pick you up and sneak to randezvous point\n")
                        action = action.upper()
                        if action == "C":
                            print(f"\nMISSION ACCOMPLISHED!\n"
                                  f"CONGRATS {name}!")
                            input("\nPress Enter to close the game\n")
                        elif action == "R":
                            print(f"\nYou were caught. The explosion killed you and the pilot\n"
                                  f"who was supposed to pick you up\n"
                                  f"{mission_incomplete}")
                            input("\nPress Enter to close the game\n")
                        else:
                            print(f"You were too slow at randezvous point.\n"
                                  f"The explosion killed you and the pilot\n"
                                  f"who was supposed to pick you up\n"
                                  f"{mission_incomplete}")
                            input("\nPress Enter to close the game\n")
                    elif action == "2":
                        print(f"\nBomb found and defused by troops, after you left the Deathstar.\n"
                              f"{mission_incomplete}")
                        input("\nPress Enter to close the game\n")
                    else:
                        print(f"\nGot killed by the bomb\n"
                              f"{mission_incomplete}")
                        input("\nPress Enter to close the game\n")
                elif action == "F":
                    print(f"\nYou were discover in the kitchen and now your status is K.I.A.\n"
                          f"{mission_incomplete}")
                    input("\nPress Enter to close the game\n")
                else:
                    print(f"\nYou were heard. A trooper raised alarm. Couple meters later, you got caught\n"
                          f"and taken to prison\n"
                          f"{mission_incomplete}")
                    input("\nPress Enter to close the game\n")
            elif action == "F":
                print(f"\nIt got you to the command center, from where you were taken to prison!\n"
                      f"{mission_incomplete}")
                input("\nPress Enter to close the game\n")
            else:
                print(f"\nYou've got to be kidding! First trooper saw you, seconds later you were death\n"
                      f"{mission_incomplete}")
                input("\nPress Enter to close the game\n")
        elif action == "D":
            print(f"\nThere are no stones on Deathstar, Moron.\n"
                  f"You've used your air tank instead and \n"
                  f"you died before the troops came for you.\n"
                  f"{mission_incomplete}")
            input("\nPress Enter to close the game\n")
        else:
            print("\nYou're brave! Pick what to do with this person\n")
            action = input("I - Scary her and Interrogate\n"
                           "K - kill and search the body\n"
                           "S - Shush and make her cooperate")
            action = action.upper()
            if action == "S":
                print(f"\nHer coworker, came unseen and hit you in the head with metal pipe\n"
                      f"{mission_incomplete}")
                input("\nPress Enter to close the game\n")
            elif action == "I":
                print(f"\nYou've got killed, by her 20\" wrench \n"
                      f"{mission_incomplete}")
                input("\nPress Enter to close the game\n")
            else:
                print(f"\nAlarm activated, because of her wristband sensing no pulse\n"
                      f"You were caught and thrown to prison\n"
                      f"{mission_incomplete}")
                input("\nPress Enter to close the game\n")
    elif action == "B":
        print(f"\nAlarm activated, you were take to prison\n"
              f"{mission_incomplete}")
        input("\nPress Enter to close the game\n")
    else:
        print(f"\nWarning in security system detected. Troops came and took you to prison\n"
              f"{mission_incomplete}")
        input("\nPress Enter to close the game\n")
elif action == "E":
    print("\nWARNING! You've been targeted with Deathstars LDS!")
    action = input("\nChoose direction to dodge the laser, QUICKLY!!\n L for Left, D for Down, R for Right\n")
    action = action.upper()
    if action == "R":
        print(f"\nYou've dodge the laser, but the command orders you to return to base \n"
              f"{mission_incomplete}")
        input("\nPress Enter to close the game\n")
    else:
        print(f"\nKilled by LDS \n"
              f"{mission_incomplete}")
        input("\nPress Enter to close the game\n")
else:
    print(f"\nAfter half an hour of searching, no doors were found, returning to base\n"
          f"{mission_incomplete}")
    input("Press enter to close the game")
