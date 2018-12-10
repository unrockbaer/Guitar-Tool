"""Ultimate Guitar Practice App"""



print("Martins Ultimate Guitar Practice Tool. \n")

import random
import sys


notes = ("C","D","E","F","G","A","B","Cb","Db","Eb","Gb","Ab","Bb","C#","D#","E#","F#","G#","A#")
standard_chords = ("C","Cm","D","Dm","E","Em","F","Fm","G","Gm","A","Am","B","Bm",
                   "Cb","Cbm","Db","Dbm","Eb","Ebm","Gb","Gbm","Ab","Abm","Bb","Bbm",
                   "C#","C#m","D#","D#m","F#","F#m","G#","G#m","A#","A#m")
st_chord_formula = ("1-3-5","1-b3-5")
st_chord_tabs = ("X-3-5-5-5-3 / X-3-2-0-1-0 / 8-10-10-9-8-8", "X-3-5-5-4-3 / 8-10-10-8-8-8",            # C / Cm
                 "X-5-7-7-7-5 / X-X-0-2-3-2 / 10-12-12-11-10-10", "X-X-0-2-3-1 / 10-12-12-10-10-10",    # D / Dm
                 "X-7-9-9-9-7 / 0-2-2-1-0-0", "X-7-9-9-8-7 / 0-2-2-0-0-0",                              # E / Em
                 "1-3-3-2-1-1 / X-8-10-10-10-8", "1-3-3-1-1-1 / X-8-10-10-8-8",                         # F / Fm
                 "3-2-0-0-3-3 / 3-5-5-4-3-3 / X-10-12-12-12-10", "3-5-5-3-3-3 / X-10-12-12-11-10",      # G / Gm
                 "5-7-7-6-5-5 / X-0-2-2-2-0", "5-7-7-5-5-5 / X-0-2-2-1-0",                              # A / Am
                 "7-9-9-8-7-7 / X-2-4-4-4-2", "7-9-9-7-7-7 / X-2-4-4-3-2",                              # B / Bm
                 "7-9-9-8-7-7 / X-2-4-4-4-2", "7-9-9-7-7-7 / X-2-4-4-3-2",                              # Cb / Cbm
                 "9-11-11-10-9-9 / X-4-6-6-6-4", "9-11-11-9-9-9 / X-4-6-6-5-4",                         # Db / Dbm
                 "11-13-13-12-11-11 / X-6-8-8-8-6", "11-13-13-11-11-11 / X-6-8-8-7-6",                  # Eb / Ebm
                 "2-4-4-3-2-2 / X-9-11-11-11-9", "2-4-4-2-2-2 / X-9-11-11-10-9",                        # Gb / Gbm
                 "4-6-6-5-4-4 / X-11-13-13-13-11", "4-6-6-4-4-4 / X-11-13-13-11-11",                    # Ab / Abm
                 "6-8-8-7-6-6 / X-1-3-3-3-1", "6-8-8-6-6-6 / X-1-3-3-2-1",                              # Bb / Bbm
                 "9-11-11-10-9-9 / X-4-6-6-6-4", "9-11-11-9-9-9 / X-4-6-6-5-4",                         # C# / C#m
                 "11-13-13-12-11-11 / X-6-8-8-8-6", "11-13-13-11-11-11 / X-6-8-8-7-6",                  # D# / D#m
                 "2-4-4-3-2-2 / X-9-11-11-11-9", "2-4-4-2-2-2 / X-9-11-11-10-9",                        # F# / F#m
                 "4-6-6-5-4-4 / X-11-13-13-13-11", "4-6-6-4-4-4 / X-11-13-13-11-11",                    # G# / G#m
                 "6-8-8-7-6-6 / X-1-3-3-3-1", "6-8-8-6-6-6 / X-1-3-3-2-1")                              # A# / A#m                 

                 
seventh_chords = ("Cmaj7","C7","Cm7b5","Cm7","Cdim7","C7#5","C7b5","C-(maj7)",                          # C
                  "Dmaj7","D7","Dm7b5","Dm7","Ddim7","D7#5","D7b5","D-(maj7)",                          # D
                  "Emaj7","E7","Em7b5","Em7","Edim7","E7#5","E7b5","E-(maj7)",                          # E
                  "Fmaj7","F7","Fm7b5","Fm7","Fdim7","F7#5","F7b5","F-(maj7)",                          # F
                  "Gmaj7","G7","Gm7b5","Gm7","Gdim7","G7#5","G7b5","G-(maj7)",                          # G
                  "Amaj7","A7","Am7b5","Am7","Adim7","A7#5","A7b5","A-(maj7)",                          # A
                  "Bmaj7","B7","Bm7b5","Bm7","Bdim7","B7#5","B7b5","B-(maj7)",                          # B
                  "Cbmaj7","Cb7","Cbm7b5","Cbm7","Cbdim7","Cb7#5","Cb7b5","Cb-(maj7)",                  # Cb
                  "Dbmaj7","Db7","Dbm7b5","Dbm7","Dbdim7","Db7#5","Db7b5","Db-(maj7)",                  # Db
                  "Ebmaj7","Eb7","Ebm7b5","Ebm7","Ebdim7","Eb7#5","Eb7b5","Eb-(maj7)",                  # Eb
                  "Fbmaj7","Fb7","Fbm7b5","Fbm7","Fbdim7","Fb7#5","Fb7b5","Fb-(maj7)",                  # Fb
                  "Gbmaj7","Gb7","Gbm7b5","Gbm7","Gbdim7","Gb7#5","Gb7b5","Gb-(maj7)",                  # Gb
                  "Abmaj7","Ab7","Abm7b5","Abm7","Abdim7","Ab7#5","Ab7b5","Ab-(maj7)",                  # Ab
                  "Bbmaj7","Bb7","Bbm7b5","Bbm7","Bbdim7","Bb7#5","Bb7b5","Bb-(maj7)",                  # Bb
                  "C#maj7","C#7","C#m7b5","C#m7","C#dim7","C#7#5","C#7b5","C#-(maj7)",                  # C#
                  "D#maj7","D#7","D#m7b5","D#m7","D#dim7","D#7#5","D#7b5","D#-(maj7)",                  # D#
                  "E#maj7","E#7","E#m7b5","E#m7","E#dim7","E#7#5","E#7b5","E#-(maj7)",                  # E#
                  "F#maj7","F#7","F#m7b5","F#m7","F#dim7","F#7#5","F#7b5","F#-(maj7)",                  # F#
                  "G#maj7","G#7","G#m7b5","G#m7","G#dim7","G#7#5","G#7b5","G#-(maj7)",                  # G#
                  "A#maj7","A#7","A#m7b5","A#m7","A#dim7","A#7#5","A#7b5","A#-(maj7)",                  # A#
                  "B#maj7","B#7","B#m7b5","B#m7","B#dim7","B#7#5","B#7b5","B#-(maj7)",)                 # B#

extended_chords = ("Cmaj9","C9","Cm9","C11","Cm11","Cmaj13","C13","Cm13",
                   "Dmaj9","D9","Dm9","D11","Dm11","Dmaj13","D13","Dm13",
                   "Emaj9","E9","Em9","E11","Em11","Emaj13","E13","Em13",
                   "Fmaj9","F9","Fm9","F11","Fm11","Fmaj13","F13","Fm13",
                   "Gmaj9","G9","Gm9","G11","Gm11","Gmaj13","G13","Gm13",
                   "Amaj9","A9","Am9","A11","Am11","Amaj13","A13","Am13",
                   "Bmaj9","B9","Bm9","B11","Bm11","Bmaj13","B13","Bm13",
                   "Cbmaj9","Cb9","Cbm9","Cb11","Cbm11","Cbmaj13","Cb13","Cbm13",
                   "Dbmaj9","Db9","Dbm9","Db11","Dbm11","Dbmaj13","Db13","Dbm13",
                   "Ebmaj9","Eb9","Ebm9","Eb11","Ebm11","Ebmaj13","Eb13","Ebm13",
                   "Fbmaj9","Fb9","Fbm9","Fb11","Fbm11","Fbmaj13","Fb13","Fbm13",
                   "Gbmaj9","Gb9","Gbm9","Gb11","Gbm11","Gbmaj13","Gb13","Gbm13",
                   "Abmaj9","Ab9","Abm9","Ab11","Abm11","Abmaj13","Ab13","Abm13",
                   "Bbmaj9","Bb9","Bbm9","Bb11","Bbm11","Bbmaj13","Bb13","Bbm13",
                   "C#maj9","C#9","C#m9","C#11","C#m11","C#maj13","C#13","C#m13",
                   "D#maj9","D#9","D#m9","D#11","D#m11","D#maj13","D#13","D#m13",
                   "E#maj9","E#9","E#m9","E#11","E#m11","E#maj13","E#13","E#m13",
                   "F#maj9","F#9","F#m9","F#11","F#m11","F#maj13","F#13","F#m13",
                   "G#maj9","G#9","G#m9","G#11","G#m11","G#maj13","G#13","G#m13",
                   "A#maj9","A#9","A#m9","A#11","A#m11","A#maj13","A#13","A#m13",
                   "B#maj9","B#9","B#m9","B#11","B#m11","B#maj13","B#13","B#m13",)

altered_chords = ("C7b5",)
other_chords= ("C6","Cm6","C6/9","Csus2","Csus4","C7sus4","Cadd9","Cm(add9)",
               "D6","Dm6","D6/9","Dsus2","Dsus4","D7sus4","Dadd9","Dm(add9)",
               "E6","Em6","E6/9","Esus2","Esus4","E7sus4","Eadd9","Em(add9)",
               "F6","Fm6","F6/9","Fsus2","Fsus4","F7sus4","Fadd9","Fm(add9)",
               "G6","Gm6","G6/9","Gsus2","Gsus4","G7sus4","Gadd9","Gm(add9)",
               "A6","Am6","A6/9","Asus2","Asus4","A7sus4","Aadd9","Am(add9)",
               "B6","Bm6","B6/9","Bsus2","Bsus4","B7sus4","Badd9","Bm(add9)",
               "Cb6","Cbm6","Cb6/9","Cbsus2","Cbsus4","Cb7sus4","Cbadd9","Cbm(add9)",
               "Db6","Dbm6","Db6/9","Dbsus2","Dbsus4","Db7sus4","Dbadd9","Dbm(add9)",
               "Eb6","Ebm6","Eb6/9","Ebsus2","Ebsus4","Eb7sus4","Ebadd9","Ebm(add9)",
               "Fb6","Fbm6","Fb6/9","Fbsus2","Fbsus4","Fb7sus4","Fbadd9","Fbm(add9)",
               "Gb6","Gbm6","Gb6/9","Gbsus2","Gbsus4","Gb7sus4","Gbadd9","Gbm(add9)",
               "Ab6","Abm6","Ab6/9","Absus2","Absus4","Ab7sus4","Abadd9","Abm(add9)",
               "Bb6","Bbm6","Bb6/9","Bbsus2","Bbsus4","Bb7sus4","Bbadd9","Bbm(add9)",
               "C#6","C#m6","C#6/9","C#sus2","C#sus4","C#7sus4","C#add9","C#m(add9)",
               "D#6","D#m6","D#6/9","D#sus2","D#sus4","D#7sus4","D#add9","D#m(add9)",
               "E#6","E#m6","E#6/9","E#sus2","E#sus4","E#7sus4","E#add9","E#m(add9)",
               "F#6","F#m6","F#6/9","F#sus2","F#sus4","F#7sus4","F#add9","F#m(add9)",
               "G#6","G#m6","G#6/9","G#sus2","G#sus4","G#7sus4","G#add9","G#m(add9)",
               "A#6","A#m6","A#6/9","A#sus2","A#sus4","A#7sus4","A#add9","A#m(add9)",
               "B#6","B#m6","B#6/9","B#sus2","B#sus4","B#7sus4","B#add9","B#m(add9)",)

    
def main_menu():

    while True:
    
        print("\n    1 Random Fretboard Notes\n    2 Random Chords\n    3 Scales\n    4 Technique Exercises\n    5 Play a Song\n    6 Get in tune\n    7 Metronome\n    8 Get out.\n")

        user_input = input("Your choice: ")

        if user_input in ("8","get out","bye","Get out.","Get out","out"):
            print("\nSee you next time. Have a nice day!")
            sys.exit()
    
        elif user_input in ("1","notes","note"):
 
            print("\n     Random Notes")
            print("\nStart out with this note:     " + random.choice(notes))
        
            while True:

                user_input = input("\n1. Next note \n2. Main menu\n")
       
                if user_input == "1":
                    print("\n    " + random.choice(notes))
                elif user_input == "2":
                    main_menu()
                else:
                    print("Invalid input")
            

        elif user_input in ("2","chords","chords"):



            while True:
            
                print("\n    1  Standard Chords")
                print("    2  Seventh Chords")
                print("    3  Extended Chords")
                print("    4  Other Chords (sixth, ninth,...)")
                print("    5  Standard + Seventh Chords")
                print("    6  Standard + Seventh + Others")
                print("    7  Seventh + Extended Chords")
                print("    8  Extended + Others")
                print("    9  Advanced (All)")
                print("    10 Back to Main Menu\n")


            
                user_input = input("Choose: ")

                def chord_func(chord_name,chords):

                    
                    print("\n     "+ str(chord_name))
                    print("\nFirst chord is " + random.choice(chords))

                    while True:
                    
                        user_input = input("\n1 Next chord \n2 Change chord type\n3 Main Menu\n")

                        if user_input == "1":
                            print("\n    " + random.choice(chords))
                        elif user_input == "2":
                            break
                        elif user_input == "3":
                            main_menu()
                        else:
                            print("Invalid input")
                        



                if user_input == "1":
                    chord_func("Standard Chords",standard_chords)

                elif user_input == "2":
                    chord_func("Seventh Chords",seventh_chords)
                    
                elif user_input == "3":
                    chord_func("Extended Chords",extended_chords)
                    
                elif user_input == "4":
                    chord_func("Other Chords",other_chords)

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
      print("Unknown input")
    
main_menu()
