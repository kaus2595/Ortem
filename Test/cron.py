"""mobileNumberExecuted = int(mobileNumberExecuted)
       if mobileNumberExecuted <= breakPoint:
        #crontab stop
        changeStatus(1)
        #writefile with new status and message
        #read file with new mobileNumberExecuted
        execute the other cron manually from new mobileNumberExecuted till startingMobileNumber - range+1
        write the last startingMobileNumber - range+1 in csv
        with open('Phone.csv', 'w') as writeFile:
            csv_write = csv.writer(writeFile)
            row[1] = 1"""