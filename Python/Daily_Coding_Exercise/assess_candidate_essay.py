#----------------------------------------Code written by Sachin Negi-----------------------------------------------------
#-----------------------------------------Ambiguity and other comments---------------------------------------------------
#The question says to mark matching words with charater more than 7 as 3 but the solution shows it as 1 for calender word
#----------------The code makes sure the punctuations and leading/tailing spaces are removed before matcing---------------
#-----------------the codes uses regular expression, list, string and for loops for logic---------------------------------


import re

#function takes the response and correct answer in string format and returns the result
def results(response,correctanswer):
    correct_answer_list = []
    #splitting the correct anser with spaces in storing in list
    for word in [word.lower() for word in list(correctanswer.split(" "))]:
        #removing punctuation from the words
        correct_answer_list.append(re.sub(r'[^\w\s]','',word))

    response_list = []
    #splitting the response answer with spaces in storing in list  
    for word in [word.lower() for word in list(response.split(" "))]:
        #removing punctuation from the words
        response_list.append(re.sub(r'[^\w\s]','',word))

    #declaring variable to store the result
    marks = 0

    for word in response_list:
        if word in correct_answer_list:
            #check if the response contains the numbers from correct list
            if word == '30' or word == '12':
                marks+=4
            #check if matching response contains the words with more than 7 characters 
            if len(word) > 7:
                marks+=3
            #check if matching response contains the words with less than 5 characters 
            if len(word) > 4 and len(word) < 8:
                marks+=1
            #no need to count the marks for the matched word with character between 5 to 7

    return marks
                
#Sample running of the results functions for a dummy candidate
correctanswer = "There are twenty-four hours in a day, 30 days in a month, and 12 months in the calendar year."
response = "There are Twenty-Four hours in a day. A year has 14 months."

#makes obtained by candidate
R = results(response,correctanswer)

#percentage obtained by candidate
P = (R/16)*100

print("Th candidate scored {} and got percentage {} ".format(R,P))


