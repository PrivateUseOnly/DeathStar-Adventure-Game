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
input("INSTRUCTION! \n Just type a letter of choice, and press ENTER to start the game!")
print("Welcome to the Rogue Wars")
print("Your mission is to destroy the Deathstar!")
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
            print("\nYou're in! You've looked around and you choose your path")
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
                          " but you need to set the time for the explosion")
                    action = input("10 - for 10 minutes\n"
                                   "2 - for 2 hours\n"
                                   "20 - for 20 seconds\n")
                    action = action.upper()
                    if action == "10":
                        print("\nNow you need to evacuate quickly...\n"
                              "whats the plan?")
                        action = input("C -Call command to pick you up while you sneaking out to randezvous point\n"
                                       "R - run to randezvous point and call command for pick up\n"
                                       "S - Call command to pick you up and sneak to randezvous point\n")
                        action = action.upper()
                        if action == "C":
                            print(f"\nMISSION ACCOMPLISHED!\n"
                                  f"CONGRATS {name}!")
                        elif action == "R":
                            print("\nYou were caught. The explosion killed you and the pilot\n"
                                  "who was supposed to pick you up\n"
                                  "Mission Incomplete")
                        else:
                            print("You were too slow at randezvous point.\n"
                                  "The explosion killed you and the pilot\n"
                                  "who was supposed to pick you up\n"
                                  "Mission Incomplete")
                    elif action == "2":
                        print("\nBomb found and defused by troops, after you left the Deathstar.\n"
                              "Mission incomplete")
                    else:
                        print("\nGot killed by the bomb")
                elif action == "F":
                    print("\nYou were discover in the kitchen and now your status is K.I.A.\n"
                          "Mission Incomplete")
                else:
                    print("\nYou were heard. A trooper raised alarm. Couple meters later, you got caught\n"
                          "and taken to prison\n"
                          "Mission Incomplete")
            elif action == "F":
                print("\nIt got you to the command center, from where you were taken to prison!\n"
                      "Mission Incomplete")
            else:
                print("\nYou've got to be kidding! First trooper saw you, seconds later you were death\n"
                      "Mission Incomplete")
        elif action == "D":
            print("\nThere are no stones on Deathstar, Moron.\n"
                  "You've used your air tank instead and \n"
                  "you died before the troops came for you.\n"
                  "MISSION INCOMPLETE")
        else:
            print("\nYou're brave! Pick what to do with this person")
            action = input("I - Scary her and Interrogate\n"
                           "K - kill and search the body\n"
                           "S - Shush and make her cooperate")
            action.upper()
            if action == "S":
                print("\nHer coworker, came unseen and hit you in the head with metal pipe\n"
                      "MISSION INCOMPLETE")
            elif action == "I":
                print("\nYou've got killed, by her 20\" wrench")
            else:
                print("\nAlarm activated, because of her wristband sensing no pulse\n"
                      "You were caught and thrown to prison")
    elif action == "B":
        print("\nAlarm activated, you were take to prison")
    else:
        print("\nWarning in security system detected. Troops came and took you to prison")

elif action == "E":
    print("\nWARNING! You've been targeted with Deathstars LDS!")
    action = input("\nChoose direction to dodge the laser, QUICKLY!!\n L for Left, D for Down, R for Right")
    if action == "R":
        print(f"\nYou've dodge the laser, but the command orders you to return to base \n"
              f"Mission Incomplete")
    else:
        print("\nKilled by LDS \n"
              "Mission Incomplete")
else:
    print("\nAfter half an hour of searching, no doors were found, returning to base\n"
          "Mission Incomplete")
