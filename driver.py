import Format_Coords
import T_Map

coordsDir = '/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/coordstest.csv'
output1 = '/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/output1.json'
output2 = '/mnt/c/Users/Tomca/OneDrive/Documents/ML/Project/output2.json'
Format_Coords.save_csv(coordsDir, output1, output2)
T_Map.make_t_map(coordsDir, 1080)