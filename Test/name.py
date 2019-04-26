import csv


if __name__ == '__main__':
    mobileNumber, status, timestamp = 0,0,0
    startingMobile = 9999999999
    range = 50000000
    breakPoint = startingMobile - range + 1000



    #From start till breakPoint
    with open('Phone.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')

        for rows in csv_reader:
            mobileNumber = rows[0]
            status = rows[1]
            timestamp = rows[2]

    if(int(mobileNumber) <= breakPoint):
        status = 1
        line = [breakPoint, status, timestamp]   #Put the range
        with open('Phone.csv', 'w') as write_file:
            csv_writer = csv.writer(write_file)
            csv_writer.writerow(line)


    #From breakPoint till end
    with open('Phone.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file, delimiter=',')
        for rows in csv_reader:
            mobileNumber = rows[0]
            status = rows[1]
            timestamp = rows[2]


    if(int(mobileNumber) >= startingMobile-range+1):
        status = 1
        line = [startingMobile-range+1, status, timestamp]
        with open('Phone.csv', 'w') as write_file:
            csv_writer = csv.writer(write_file)
            csv_writer.writerow(line)


    # To change the status to 0 once the complete patch is executed
    with open('Phone.csv', 'r') as in_file:
        csv_reader = csv.reader(in_file)
        for rows in csv_reader:
            mobileNumber = rows[0]
            status = rows[1]
            timestamp = rows[2]

            if(int(mobileNumber) == startingMobile-range+1 and int(status) == 1):
                status = 0
                line = [mobileNumber, status, timestamp]
                with open('Phone.csv', 'w') as write_file:
                    csv_writer = csv.writer(write_file)
                    csv_writer.writerow(line)
                    #print(line)





