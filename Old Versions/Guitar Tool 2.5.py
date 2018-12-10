"""Ultimate Guitar Practice Tool"""


import time
import random
import sys

from database_old import notes, standard_chords, st_form, st_tabs, seventh_chords, svth_form, svth_form, svth_tabs, extended_chords, ext_tabs, altered_chords, alt_tabs, other_chords, other_tabs




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

    # --- the random chord function ---
                
                def chord_func_st(chord_name,chords,tabs):

                    
                    print("\n\t"+ str(chord_name))
                    n = random.randint(0,len(chords))
                                       
                    print("\nFirst chord is " + chords[n])

                    while True:
                    
                        user_input = input("\n1 Next chord \n2 Tabs \n3 Formula \n4 Change chord type\n5 Main Menu\n\n")
                                            
                        if user_input == "1":
                            n = random.randint(0,len(chords))
                            print("\n\t" + chords[n])
                        elif user_input == "2":
                            print("\n\t" + chords[n] + "\t" + tabs[n])
                        elif user_input == "3":
                            if n % 2 == 0:
                                print("\n\t" + chords[n] + "\tMajor \t" + st_form[0])
                            else:
                                print("\n\t" + chords[n] + "\tMinor \t" + st_form[1])
                        elif user_input == "4":
                            break
                        elif user_input == "5":
                            main_menu()
                        else:
                            print("Invalid input")
                        
     # --- Seventh Chord Function ---
                def chord_func_svth (chord_name,chords,tabs):

                    
                    print("\n\t"+ str(chord_name))
                    n = random.randint(0,len(chords))
                                       
                    print("\nFirst chord is " + chords[n])

                    while True:
                    
                        user_input = input("\n1 Next chord \n2 Tabs \n3 Formula \n4 Change chord type\n5 Main Menu\n\n")
                                            
                        if user_input == "1":
                            n = random.randint(0,len(chords))
                            print("\n\t" + chords[n])

            			
            
                        elif user_input == "2":
                            print("\n\t" + chords[n] + "\t" + tabs[n])
                        elif user_input == "3":
                            if str(n) in ("0","8","16","24","32","40","48","56","64","72","80","88","96","104","112","120","128","136","144","152","160"):
                                print("\n\t" + chords[n] + "\t - Major Seventh -\t" + svth_form[0])
                            elif str(n) in ("1","9","17","25","33","41","49","57","65","73","81","89","97","105","113","121","129","137","145","153","161"):
                                print("\n\t" + chords[n] + "\t - Dominant Seventh -\t" + svth_form[1])
                            elif str(n) in ("2","10","18","26","34","42","50","58","66","74","82","90","98","106","114","122","130","138","146","154","162"):
                                print("\n\t" + chords[n] + "\t - Minor Seventh Flat Five -\t" + svth_form[2])
                            elif str(n) in ("3","11","19","27","35","43","51","59","67","75","83","91","99","107","115","123","131","139","147","155","163"):
                                print("\n\t" + chords[n] + "\t - Minor Seventh -\t" + svth_form[3])
                            elif str(n) in ("4","12","20","28","36","44","52","60","68","76","84","92","100","108","116","124","132","140","148","156","164"):
                                print("\n\t" + chords[n] + "\t - Diminished Seventh -\t" + svth_form[4])
                            elif str(n) in ("5","13","21","29","37","45","53","61","69","77","85","93","101","109","117","125","133","141","149","157","165"):
                                print("\n\t" + chords[n] + "\t - Augmented Seventh -\t" + svth_form[5])
                            elif str(n) in ("6","14","22","30","38","46","54","62","70","78","86","94","102","110","118","126","134","142","150","158","166"):
                                print("\n\t" + chords[n] + "\t - Dominant Seven Flat Five -\t" + svth_form[6])
                            elif str(n) in ("7","15","23","31","39","47","55","63","71","79","87","95","103","111","119","127","135","143","151","159","167"):
                                print("\n\t" + chords[n] + "\t - Minor/Major Seventh  -\t" + svth_form[7])

                        elif user_input == "4":
                            break
                        elif user_input == "5":
                            main_menu()
                        else:
                            print("Invalid input")
                        
                



                if user_input == "1":
                              
                    chord_func_st("Standard Chords",standard_chords,st_tabs)

                elif user_input == "2":
                    chord_func_svth("Seventh Chords",seventh_chords,svth_tabs)
                    
                    
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
