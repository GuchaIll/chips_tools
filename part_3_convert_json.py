import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

"""
Data loaded from your JSON file should create a fully initialized CCLevelPack object
○ It must support multiple levels
○ Each level must be initialized with:
■ valid level number (NOTE: this must be 1 or greater--0 doesn’t work)
■ valid time
■ valid chip number
■ valid upper layer
■ list of valid optional fields
○ You must support the following field types:
■ Field 3 is the map title.
■ Field 6 is used to specify an encoded password. NOTE: You should only use field 6,
an encoded password. Do not use field 8, an unencoded password
■ Field 7 is used to indicate hint text
■ Field 10 is used to indicate where moving objects (monsters) occur
○ Extra credit field types:
■ Field 4 is used to map brown buttons to traps.
■ Field 5 is used to map red buttons to cloning machines.
Look at the code in cc_classes.py for details on how to initialize the different field types


Extended the existing toolset with the functionality to load your JSON data files and save them as DAT files:
Use the existing part_3_convert_json.py to facilitate the loading of your JSON file and the saving of your DAT file.
It must save the JSON data as fully function Chip’s Challenge DAT file
Hint: This work follows a very similar pattern to Working with JSON (Step 2).
Create a new Chip’s Challenge level pack using your JSON format:
It must contain 2 playable levels meeting these requirements: Assignment #2 JSON & Level Requirements.pdfDownload Assignment #2 JSON & Level Requirements.pdf
Links to an external site.Save the JSON file and the DAT file in the data folder. Use the following naming convention:
your_andrew_id_cc1.dat
your_andrew_id_cc1.json
Commit and push all of your files and code changes to your GitHub repository
"""

def make_cc_level_pack_from_json(json_data):
    level_pack = cc_classes.CCLevelPack()

    for level in json_data["Levels"]:
        new_level = cc_classes.CCLevel()
        new_level.level_number = level["Level_Number"]
        new_level.time = level["Time"]
        new_level.num_chips = level["Num_Chips"]
        new_level.upper_layer = level["Upper_Layer"]
        new_level.optional_fields = []
        
        for field in level["Optional_Fields"]:
            for key, value in field.items():
                if key == "field 3":
                    new_level.add_field(cc_classes.CCMapTitleField(value))
                elif key == "field 6":
                    password = []
                    for c in value:
                        password.append(c)
                    new_level.add_field(cc_classes.CCEncodedPasswordField(password))
                elif key == "field 7":
                    new_level.add_field(cc_classes.CCMapHintField(value))
                elif key == "field 10":
                    monsters = []
                    for monster in value:
                        print(monster)
                        monsters.append(cc_classes.CCCoordinate(int(monster['x']), int(monster['y'])))
                    new_level.add_field(cc_classes.CCMonsterMovementField(monsters))
                elif key == "field 4":
                    Traps = []
                    for trap in value:
                        Traps.append(cc_classes.CCTrapControl(int(trap["bx"]), int(trap["by"]), int(trap["tx"]), int(trap["ty"])))
                    new_level.add_field(cc_classes.CCTrapControlsField(Traps))
                elif key == "field 5":
                    Cloning_Machines = []
                    for clone in value:
                        Cloning_Machines.append(cc_classes.CCCloningMachineControl(int(clone["bx"]), int(clone["by"]), int(clone["tx"]), int(clone["ty"])))
                    new_level.add_field(cc_classes.CCCloningMachineControlsField(Cloning_Machines))
        
        level_pack.add_level(new_level)

    print(len(level_pack.levels))
    print(level_pack.levels[0], level_pack.levels[1])
    return level_pack

input_json_file = "data/yacil_cc1.json"
output_dat_file = "data/yacil_cc1.dat"
with open(input_json_file, "r") as file:
    json_data = json.load(file)


cc_level_pack = make_cc_level_pack_from_json(json_data)

cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, output_dat_file)

print(cc_level_pack)


