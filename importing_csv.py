import pandas

  #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

def add_full_name(path_to_csv, path_to_new_csv):
    data_baseball = pandas.read_csv(path_to_csv)
    data_baseball['nameFull'] = data_baseball['nameFirst'] +" "+ data_baseball['nameLast']
    data_baseball.to_csv(path_to_new_csv)