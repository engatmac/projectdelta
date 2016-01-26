
import smtplib
rort = raw_input("Are you a refugee or a teacher? ")
run = True
run1 = True
run2 = True
run3 = True
run4 = True
run5 = True
while run == True:
#Teacher survey
    if rort == "teacher"
        teachers = open("teachers.txt","w")
        namet = raw_input ("What is your first name? ")
        name2t = raw_input("What is your last name? ")
        while run1 == True:
            aget = raw_input ("What is your age \n A 16-20 \n B 20-35 \n C 35-50 \n D 50+ \n ")
            if aget == "A" or aget == "B" or aget == "C" or aget == "D":
                run1 = False
            else:
                print "Invalid answer, please input either A,B,C,or D"
        while run2 == True:
            paget = raw_input("What is the preferred age range of the person you will be speaking to? \n A 16-20 \n B 20-35 \n C 35-50 \n D 50+ \n ")
            if paget == "A" or paget == "B" or paget == "C" or paget == "D":
                run2 = False
            else:
                print "Invalid answer, please input either A,B,C,or D"
        while run3 == True:
            gendert = raw_input("What is your gender? \n Male \n Female \n Other \n Prefer Not To Say \n ")
            if gendert == "Male" or gendert == "Female" or gendert == "Other" or gendert == "Prefer Not To Say":
                run3 = False
            else:
                print "Invalid answer, please input either Male, Female, Other, Prefer Not To Say"
        while run4 == True:
            pgendert = raw_input("What gender would you prefer to speak to? \n Male \n Female \n No Preference \n ")
            if pgendert == "Male" or pgendert == "Female" or pgendert == "No Preference":
                run4 = False
            else:
                print "Invalid answer, please input either Male, Female, Other, Prefer Not To Say"
        countryt = raw_input("What is your current country of residence? ")
        languaget = raw_input("If you are fluent in a language besides english, please specify ")
        skypet = raw_input("What is your Skype username? ")
        emailt = raw_input("What is your email? ")
        teachers.write(namet+"\t"+name2t+"\t"+aget+"\t"+paget+"\t"+gendert+"\t"+pgendert+"\t"+countryt+"\t"+languaget+"\t"+skypet+"\t"+emailt)
        teachers.close()
        print "Thanks for signing up! You will recieve an e-mail when you get matched."
        run = False
#Refugee survey
    elif rort == "refugee":
        refugees1 = open("refugees.txt", "w")
        namer = raw_input ("What is your first name? ")
        name2r = raw_input("What is your last name? ")
        while run1 == True:
            ager = raw_input ("What is your age \n A 16-20 \n B 20-35 \n C 35-50 \n D 50+ \n ")
            if ager == "A" or ager == "B" or ager == "C" or ager == "D":
                run1 = False
            else:
                print "Invalid answer, please input either A,B,C,or D"
        while run2 == True:
            pager = raw_input("What is the preferred age range of the person you will be speaking to? \n A 16-20 \n B 20-35 \n C 35-50 \n D 50+ \n ")
            if pager == "A" or pager == "B" or pager == "C" or pager == "D":
                run2 = False
            else:
                print "Invalid answer, please input either A,B,C,or D"
        while run3 == True:
            genderr = raw_input("What is your gender? \n Male \n Female \n Other \n Prefer Not To Say \n ")
            if genderr == "Male" or genderr == "Female" or genderr == "Other" or genderr == "Prefer Not To Say":
                run3 = False
            else:
                print "Invalid answer, please input either Male, Female, Other, Prefer Not To Say"
        while run4 == True:
            pgenderr = raw_input("What gender would you prefer to speak to? \n Male \n Female \n No Preference \n ")
            if pgenderr == "Male" or pgenderr == "Female" or pgenderr == "No Preference":
                run4 = False
            else:
                print "Invalid, please input Male, Female, or No Preference"

        countryr = raw_input("What is your current country of residence? ")
        while run5 == True:
            languager = raw_input("What is your proficiency in english?  \n Beginner \n Intermediate \n Advanced \n ")
            if languager == "Beginner" or languager == "Intermediate" or languager == "Advanced":
                run5 = False
            else:
                print "Invalid answer, please input Beginner, Intermediate, or Advanced"
        nlanguager = raw_input("What is your native language? ")
        skyper = raw_input("What is your Skype username? ")
        emailr = raw_input("What is your email? ")
        run = False
        Teachers = open("teachers.txt","r")
        refugees1.write(namer+"\t"+name2r+"\t"+ager+"\t"+pager+"\t"+genderr+"\t"+pgenderr+"\t"+countryr+"\t"+languager+"\t"+skyper+"\t"+emailr)

  #Matching Algorithm
        for line in Teachers:
            namet,name2t,aget,paget,gendert,pgendert,countryt,languaget,skypet,emailt = line.split("\t")
            if ager == paget:
                 if pager == aget:
                     if genderr == pgendert or pgendert == "No Preference":
                         if pgenderr == gendert or pgenderr == "No Preference":
                             if languager == "Beginner" and nlanguager == languaget:
                                 print "Match found! An e-mail has been sent to you with their contact information!"
                                 content = "Hello! Your Lingexchange match is", namet,"! Their gender is",gendert,". Their Skype name is",skypet,"and their email is",emailr,". \n Feel free to contact them. They would love to hear from you! \n Thanks, \n The LingExchange Team"
                                 mail = smtplib.SMTP("smtp.gmail.com",587)
                                 mail.ehlo()
                                 mail.starttls()
                                 mail.login ("lingexchange@gmail.com","Refugees!69")
                                 mail.sendmail ("lingexchange@gmail.com", str(emailr), str(content))
                                 mail.close()
                             elif languager != "Beginner" or nlanguager != languaget:
                                print "Match found! An e-mail has been sent to you with their contact information!"
                                content = "Hello! Your Lingexchange match is", namet,"! Their gender is",gendert,"and their age is between",aget,". Their Skype name is",skypet,"and their email is",emailr,". \n Feel free to contact them. They would love to hear from you! \n Thanks, \n The LingExchange Team"
                                mail = smtplib.SMTP("smtp.gmail.com",587)
                                mail.ehlo()
                                mail.starttls()
                                mail.login ("lingexchange@gmail.com","Refugees!69")
                                mail.sendmail ("lingexchange@gmail.com", str(emailr), str(content))
                                mail.close()
                           
                             else:
                                print "Sorry, no match found. We will send you an e-mail when we find one." 
                         else:
                             print "Sorry, no match found. We will send you an e-mail when we find one."
                     else:
                         print "Sorry. no match found. We will send you an e-mail when we find one."
                 else:
                     print "Sorry, no match found. We will send you an e-mail when we find one."
            else:
                print "Sorry, no match found. We will send you an e-mail when we find one."
    else:
        print "Invalid, please input either teacher or refugee"
