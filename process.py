log_file = open("um-server-01.txt") #sets the constant of log_file to be the opened text file on the server. Going to be looping over each line of the data in the file.


def sales_reports(log_file):        #defines the function sales report that requires the input of the log_file constant.
    for line in log_file:           #start of the loop. looping over every line in the log_file data. 
        line = line.rstrip()        #removes any trailing characters on the line in the log file.
        day = line[0:3]             #read thru lines 0-3 to find day listed
        if day == "Mon":            #Filter the file to only print where the day is equal to tuesday/updated to monday
            print(line)             #makes the output be equal for what the line is equal to


sales_reports(log_file)              #executes the function "sales report" using the input value of the log_file constant defined above.
