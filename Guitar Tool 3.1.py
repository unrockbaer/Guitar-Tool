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
                    

                        # --- Seventh Chord name and formula ---

                        def chord_struc():
                            
                            def inside_struc(name_var, form):
                                
                                name = ("\t" + name_var)
                                formula = (form)
                                return name, formula 

                            if "(maj7)" in random_pick:
                                return inside_struc(" Major/Minor Seventh", "1-b3-5-7")
                            elif "maj7" in random_pick:
                                return inside_struc(" Major Seventh", "1-3-5-7")
                            elif "dom7" in random_pick:
                                return inside_struc(" Dominant Seventh", "1-3-5-b7")
                            elif "min7" in random_pick:
                                return inside_struc(" Minor Seventh", "1-b3-5-b7")
                            elif "m7b5" in random_pick:
                                return inside_struc(" Minor Seven Flat Five / half-diminished Seventh", "1-b3-b5-b7")
                            elif "dim7" in random_pick:
                                return inside_struc(" Diminished Seventh", "1-b3-b5-bb7")
                            elif "7#5" in random_pick:
                                return inside_struc(" Augmented Seventh", "1-3-#5-b7")
                            elif "7b5" in random_pick:
                                return inside_struc(" Dominant Seven Flat Five", "1-3-b5-b7")
                            elif "m" in random_pick:
                                return inside_struc(" Minor", "1-b3-5")
                            else:
                                return inside_struc(" Major", "1-3-5")


                        # --- chord submenu ---
                        name, form = chord_struc()

                        user_input = input("\n1 Next chord \n2 Tabs \n3 Formula \n4 Change chord type\n5 Main Menu\n\n")
                        
                        if user_input == "1":
                            random_pick = random.choice(list(chords.keys()))
                            print("\n\t" + random_pick)
                        
                        elif user_input == "2":
                            
                            print("\n\t" + random_pick + "\t\t" + chords[random_pick] + "\t" + name)
                        
                        elif user_input == "3":
                            print( "\t" + form + name)                         
                            
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
                elif user_input == "3":
                    random_chords("Extended Chords", extended_chords)
                elif user_input == "4": 
                    random_chords("Other chords", other_chords)
                elif user_input == "5":
                    random_chords("Standard & Seventh Chords", standard_chords + seventh_chords)
                elif user_input == "6":
                    random_chords("Standard & Extended Chords", standard_chords + extended_chords)
                else: 
                    print("\n\t Invalid input.")

    else:
      print("\nUnknown input")

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
    
main_menu()

"""


