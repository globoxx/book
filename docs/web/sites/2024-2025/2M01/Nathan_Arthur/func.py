import os
from tools.interface import *
from tools.parser import *

ui = Interface()
results = None

def init():
    global results
    ui.printmsg("Welcome to your results management console!")

    detectedFile = refresh_files()
    if len(detectedFile) == 0:
        menu = ["Create a results sheet","Exit"]

        choice = ui.showmenu("No result sheet was detected in you directory, what do you want to do ?", menu)

        if menu[choice] == "Create a results sheet":
            while True:
                fn = ui.showaskbox("Enter the name of your new result file")
                file_path = f'{fn}.sm'

                if os.path.exists(file_path):
                    ui.printerrmsg("This file already exists !")
                else:
                    break
        else:
            exit(0)
            

        with open(file_path, 'w') as file:
            file.write("version: " + getVersion())
            file.close()
        
        refresh_files()
        display_main_menu()

    elif len(detectedFile) > 1:

        path = detectedFile[ui.showmenu("We have detected multiple files. Which one do you want to use?", detectedFile)]
        results = Results(path, getVersion())

    else:
        results = Results(detectedFile[0], getVersion())
        
    err = results.init()
    if err != 0:
        ui.printerrmsg(err)
        exit(1)

def refresh_files():
    detectedFiles = []
    for file in os.listdir(): 
        if file.endswith(".sm"):
            detectedFiles.append(file)
    return detectedFiles

def display_main_menu():
    global results
    menu = []
    menu.append("Modify/add results to your sheet")
    menu.append("Exit")
    
    choice = ui.showmenu("What do you want to do?", menu)

    
    if menu[choice] == "Exit":
        results.write_changes_to_file()
        ui.printmsg("Bye bye")
        exit(0)

    elif choice < len(detectedFile):
        chosen_file = detectedFile[choice]
        print(f"File selected: {chosen_file}")
        results_sheet = Results(getVersion())
        results_sheet.parse_file(chosen_file)
        
        branch = ui.showaskbox("Enter the branch of the test")
        score = ui.showaskbox("Enter the score of this test")
        
        try:
            score = float(score)
            results_sheet.add_note(branch, score)
        except ValueError:
            ui.printmsg("Error: Invalid score value. Please enter a numeric value.")
            return
        
        print(results_sheet.display_averages())

def getVersion():
    return "1.0"
