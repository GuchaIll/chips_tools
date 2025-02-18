import test_data
import json


'''
Create a JSON file called test_data.json that encodes a game library. A game library consists of a list of games, each game being defined by a title, platform (consisting of launch year, and name), and year. The data must contain the following 2 entries plus a third you add yourself (for a total of 3):
<game 1>
platform:
launch year : 1989
name: Atari Lynx
 title: “Chip’s Challenge”
Year: 1989
<game 2>
platform:
launch year : 2003
name: Steam
 title: “Chip’s Challenge 2”
Year: 2015
Add code to part_2_read_test_json.py to load the JSON file, convert the JSON data to a GameLibrary object. Follow the provided structure and comments in part_2_read_test_json.py. Look at family_data.jsonLinks to an external site., family_test.pyLinks to an external site., and family_classes.pyLinks to an external site. for an example of how this code should work.
Commit and push test_data.json and you changes to the code to your GitHub repository
Submit a link to the latest github commit with your work (the URL will look like "[...]/commit/[9a0220110...]"
(I do not want all of your work to be in a single commit. I just want you to figure out how to link to a specific version of your project.)
'''
#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library

    for game in json_data["games"]:
        game_title = game["title"]
        game_year = game["year"]
        platform_name = game["platform"]["name"]
        platform_launch_year = game["platform"]["launch_year"]

        new_game = test_data.Game(game_title, test_data.Platform(platform_name, platform_launch_year), game_year)
        game_library.add_game(new_game)
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()




with open(input_json_file, "r") as file:
    json_data = json.load(file)

game_library = make_game_library_from_json(json_data)

print(game_library)



### End Add Code Here ###
