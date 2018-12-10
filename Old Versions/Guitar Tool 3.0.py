"""Ultimate Guitar Practice Tool"""


import time
import random
import sys




from database import notes, standard_chords, seventh_chords, st_formula


print("\v\v\t"+time.strftime("%d.%m.%Y\t - \t %H:%M"))

print("\n\n  Ultimate Challenger Guitar Practice Tool. \n")

# ---- main menu ---- 
def main_menu():

    while True:
    
        print("\n\t1 Random Notes\n\t2 Random Chords\n\t3 Scales\n\t4 Technique Exercises\n\t5 Play a Song\n\t6 Get in tune\n\t7 Metronome\n\t8 Get out.\n\n")

        user_input = input("Your choice: ")

        # --- exit ---

        if user_input.lower() in ("8","get out","bye","out"):
            print("\nSee you next time. Have a nice day!")
            sys.exit()
            
        # --- backing tracks ----
        
        #to be implemented
        
        # --- not yet implemented ---

        elif int(user_input) > 2 and int(user_input) < 8:
            print("\nSorry, this feature is not yet implemented, but I'm working hard to make it work soon!")
            
        
        # --- random notes ---
        elif user_input in ("1","notes","note"):

             
            print("\n\tRandom Notes")
            rando = random.choice(notes)
            print("\n\nStart out with this note:\t" + rando)
        
            while True:

                user_input = input("\n1 Next note \n2 Main menu\n\n")
       
                if user_input == "1":
               
                    def randchoice():
                        rando2 = random.choice(notes)
                        
                        if rando == rando2:
                            randchoice()
                            
                        else:
                            print("\n\t" + rando2)
                            rando2 = rando
                            
                    randchoice()
                    
                elif user_input == "2":
                    main_menu()
                else:
                    print("Invalid input")

        # --- chords --- 

        elif user_input in ("2","chords","chords"):

            while True:
            
                print("\n\t1  Standard Chords\n\t2  Seventh Chords\n\t3  Extended Chords\n\t4  Other Chords (sixth, ninth,...)\n\t5  Standard + Seventh Chords\n\t6  Standard + Seventh + Others" + \
                      "\n\t7  Seventh + Extended Chords\n\t8  Extended + Others\n\t9  Advanced (All)\n\t10 Back to Main Menu\n\n")

                user_input = input("Choose: ")


                # --- the random chord ---

                def random_chords(chord_name,chords):

                    
                    print("\n\t"+ str(chord_name))
                    
                    random_pick = random.choice(list(chords.keys()))
        

                    print("\nFirst chord is " + random_pick)

                    while True:
                    

                        # --- Seventh Chord name ---

                        def name_chord():
                            

                            if "(maj7)" in random_pick:
                                return("\t- Minor/Major Seventh")
                            if "maj)" in random_pick:
                                return("\t- Major Seventh")
                            if "dom7" in random_pick:
                                return("\t- Dominant Seventh")
                            if "min7" in random_pick:
                                return("\t- Minor Seventh")
                            if "m7b5" in random_pick:
                                return("\t- Minor Seven Flat Five  /  half-diminished Seventh")
                            if "dim7" in random_pick:
                                return("\t- Diminished Seventh")
                            if "7#5" in random_pick:
                                return("\t- Augmented Seventh" )
                            if "7b5" in random_pick:
                                return("\t- Dominant Seven Flat Five")


                        # --- Seventh formula ---

                        #def seventh_formula():
                         #    
                         #   if random_pick == 1:
                        # --- chord submenu ---
                        user_input = input("\n1 Next chord \n2 Tabs \n3 Formula \n4 Change chord type\n5 Main Menu\n\n")
                        
                        if user_input == "1":
                            random_pick = random.choice(list(chords.keys()))
                            print("\n\t" + random_pick)
                        
                        elif user_input == "2":
                            print("\n\t" + random_pick + "\t" + chords[random_pick] + name_chord())
                        
                        elif user_input == "3":
                            if random_pick in standard_chords:
                                if "m" not in random_pick:
                                    print("\n\t" + random_pick + "\tMajor \t" + st_formula[0])
                                else:
                                    print("\n\t" + random_pick + "\tMinor \t" + st_formula[1])
                            elif random_pick in seventh_chords: 
                                print(name_chord() + "\t- " + "Hier kommt noch was") #yet to be implemented
                        elif user_input == "4":
                            break
                        elif user_input == "5":
                            main_menu()
                        else:
                            print("Invalid input")


                
                
                if user_input == "1":
                              
                    random_chords("Standard Chords",standard_chords)

                elif user_input == "2":
                    random_chords("Seventh Chords", seventh_chords) 
                else: 
                    print("\n\t Invalid input.")

main_menu()



"""
                    
                elif user_input == "3":
                    chord_func("Extended Chords",extended_chords, ext_tabs)
                    
                elif user_input == "4":
                    chord_func("Other Chords",other_chords,other_tabs)

                elif user_input == "5":
                    chord_func("Standard & Seventh Chords",standard_chords + seventh_chords)

                elif user_input == "6":
                    chord_func("Standard & Seventh & Other Chords",standard_chords + seventh_chords + other_chords)
                
                elif user_input == "7":
                    chord_func("Seventh + Extended Chords",seventh_chords + extended_chords)
                    
                elif user_input == "8":
                    chord_func("Extended & Other Chords",extended_chords + other_chords)

                elif user_input == "9":
                    chord_func("Advanced == All Chord types",standard_chords + seventh_chords + other_chords + extended_chords)

                elif user_input in ("10","back"):
                    main_menu()


                else:
                    print("Invalid input")
    else:
      print("\nUnknown input")
    
main_menu()

"""


