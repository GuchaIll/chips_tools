import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

data = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)

print(data)
#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data

#Part 2

f = open("data/pfgd_test.txt", "a")
f.write(str(data))
f.close()

'''
Modify  part_1_read_test_dat.py to load the file  data/pfgd_test.dat in Python and print out its string representation. Use the function make_cc_level_pack_from_dat(dat_file) in cc_dat_utils.py to do this. Copy this output to a text file and save it in the data folder as pfgd_test.txt.
Load and run pfgd_test.dat in TileWorld. Take a screenshot of the level running in TileWorld and save it in the data folder as pfgd_test_screenshot.png (or .jpg)
Commit and push your files to your github repository.

'''
