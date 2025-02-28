#Sample data
mission_names = [' Apollo 11 ', ' Challenger ', ' Curiosity Rover ', ' Viking 1 ', ' Mars Pathfinder ', ' Hubble Telescope ', ' Apollo 13 ']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
#create variables and lists
total_missions=0
successful_missions=0
#start with empty string to concatenate names
missions_before_2000=""
#Loop through the data 
for i in range(len(mission_names)):
    total_missions+=1
    if mission_success[i]:
        successful_missions +=1
    if mission_years[i]<2000:
        #Concatenate the mission names to the string
        if missions_before_2000:
            missions_before_2000+=","
            missions_before_2000+=mission_names[i]
        #shorthand ???missions_before_2000.append(mission_names[i])
#Calculate the success rate
if total_missions >0:
    success_rate=(successful_missions/total_missions)*100
else:
    success_rate=0
#Print the results
print("Total number of space missions",total_missions)  
print("Number of successful missions", successful_missions)
print("Success rate of the missions:{:.2f}%".format(success_rate)) 
print("Missions launched befor 2000:",''.join(missions_before_2000))     