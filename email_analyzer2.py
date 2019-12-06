 #create file for testing
createFile = open("input.txt", 'w')
createFile.write("aa@manchestercc.edu bb@manchestercc.edu 19:24\n")
createFile.write("aa@manchestercc.edu bb@manchestercc.edu 12:17\n")
createFile.write("bb@manchestercc.edu cc@capitalcc.edu 03:58\n")
createFile.write("aa@manchestercc.edu kk@asnuntuckcc.edu 05:45\n")
createFile.write("bb@manchestercc.edu cc@capitalcc.edu 11:14\n")
createFile.write("bb@manchestercc.edu kk@capitalcc.edu 02:15\n")
createFile.write("cc@manchestercc.edu kk@capitalcc.edu 06:23\n")
createFile.write("kk@capitalcc.edu uu@capitalcc.edu 04:22\n")
createFile.close()

list1 = []

def uploadtextdata():
    filename = input("Enter name of email data file: ")
    file = open(filename , "r")
    for line in file:
        splitline = line.split(" ")
        list1.append(splitline)

    print("Data successfully loaded from" , filename)
    file.close()
    print()
    main()

def display():
    for item in list1:
        print(item[1] , "sent an email to" , item[0] , "at" , item[2] , end='')
    main()

def PrintEmails():
    email = input("Enter Receiver's email address: ")
    print(email, "received the following emails: ")
    for item in list1:
        if item[0] == email:
            print(" -  From:", item[1], "at" , item[2], end='')
    print('')
    main()


def createstatsfile():
    filename = input('Please enter statistics file name to create: ')
    stats_received_emails = {}
    stats_sent = {}
    stats_domain = {}

    
    for received_email_addr in list1:
        if received_email_addr[0] in stats_received_emails:
            stats_received_emails[received_email_addr[0]] += 1
        else:
            stats_received_emails[received_email_addr[0]] = 1

    
    for email_domain in list1:
        name = email_domain[0].split('@')[0]
        domain = email_domain[0].split('@')[1]

        if domain in stats_sent:
            stats_sent[domain] += 1
        else:
            stats_sent[domain] = 1

        if domain in stats_domain:
            if name not in stats_domain[domain]:
                stats_domain[domain].append(name)
        else:
            stats_domain[domain] = [name]

        name = email_domain[1].split('@')[0]
        domain = email_domain[1].split('@')[1]

        if domain in stats_domain:
            if name not in stats_domain[domain]:
                stats_domain[domain].append(name)
        else:
            stats_domain[domain] = [name]


    most_emailed_address = ''
    counter = 0
    for k,v in stats_received_emails.items():
        if v > counter:
            counter = v
            most_emailed_address = k

    with open(filename, 'w') as fn:
        for item in list1:
            fn.write(f"From {item[1]} to {item[0]}  at {item[2]}")
        fn.write('\n')
        fn.write(f'\nAddress "{most_emailed_address}" received the most emails: {counter}\n')
        fn.write('\n')

        for k, v in stats_domain.items():
            fn.write(f'Domain {k} had {len(v)} internal emails\n')
        
        fn.write('\n')
        counter = 0
        for k,v in stats_sent.items():
            if counter == 0:
                fn.write(f'Domain {k} was used to send {v} emails.\n')
                counter += 1
            else:
                fn.write(f'Domain {k} was used to send {v} emails.')
    print("Statistics successfully written to " + filename)
    print()
    print()
    main()

    

def main():
    print("Welcome to the Email Analyzer program.")
    print("Please choose from the following options:")
    print("1. Upload text data")
    print("2. Print Data")
    print("3. Find by Receiver")
    print("4. Download statistics")
    print("5. Exit the program")
    main_choice = int(input(""))
    if main_choice < 1 or main_choice > 5:
        print("Invalid input")
    else:
        if main_choice == 1:
            uploadtextdata()
        if main_choice == 2:
            display()
        if main_choice == 3:
            PrintEmails()
        if main_choice == 4:
            createstatsfile()
        if main_choice == 5:
            print()

main()