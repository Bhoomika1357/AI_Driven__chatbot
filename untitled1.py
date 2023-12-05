# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:21:03 2023

@author: user
"""
" Task: AI_Driven CHATBOT for University placement department"
import re     # built_in library for string operations like string searching,string matching etc
import random   # built_in library allows to choose number of responses randomly with most suitability from collectinn of responses

class rulebot():
    
    negative_responses=("no", "nope", "nah", "naw", "not a chance", "sorry")

    exit_commands=("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions=("How can I assist you?",
                      "What can i do for you?",
                      "How can I help?",
                      "I am because of you.Tell me your matter?",
                      "May I know your area of concern.PLease!"
                      
                       )                               

    def __init__(self): 
         self.alienbabble= { "resume_building_intent": r".*\s*resume",     #keywords to quick response
                             "answer_why_hire_intent": r".*\s*hire*\s*",
                             "about_yourself": r".*\s*yourself*\s*",
                             "packages": r".*\s*packages*\s*",
                             "eligibility": r".*\s*eligibility*\s*",
                             "Interview_tips_intent":r".*\s*interview*\s*",
                             "Internship_intent":r".*\s*internship*\s*",
                             "students_CGPA_intent":r".*\s*CGPA*\s*",
                             "staff_recruitment_intent":r".*\s*staff recruitment*\s*",
                             "staff_salary_intent:":r".*\s*salary *\s*",
                             "current_vacany_intent":r".*\s*vacancy*\s*",
                          } 
    def greet(self):     #greeting the guest
        print("Welcome to DAV University")
        self.name=input("what is  your name?\n")
        will_help=input(
            f"hi {self.name},i am rule bot")
        if will_help  in self.negative_responses:
           print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
           feedback=input("Write here plz")
           if feedback=="Quit":
              print("ok,Have a great earth day!")
           else: 
               print("Bie,to see you again")
        return 
        self.name1=input("who are you? student/recruiter/staff\n")
        will_help1=input("My pleasure to have you here")
        if will_help1  in self.negative_responses:
            print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
            feedback=input("Write here plz")
            if feedback=="Quit":
               print("ok,Have a great earth day!")
            else: 
                print("Bie,to see you again")
           
        return 
        self.chat()
        
    def make_exit(self,reply): # to exit the RULEBOT based on negative responses 
        for command in self.exit_commands:
            if reply==command:
                print("FEEDBACK! are important for RULEBOT growth..(type \"Quit!\" if you dont want to")
                feedback=input("Write here plz")
                if feedback=="Quit":
                   print("ok,Have a great earth day!")
                else: 
                    print("Bie,to see you again")
                
            return True
    def chat(self):  # defining the chat function
        reply=input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply=input(self.match_reply(reply)) #calling match_reply function
  
               
    def match_reply(self, reply):   # to collect the right response by matching intent from dictationary defined above
           for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match=re.match(regex_pattern, reply)
            if found_match and intent=="resume_building_intent":
                return self.resume_building_intent()
            elif found_match and intent=="answer_why_hire_intent":
                return self.answer_why_hire_intent()
            elif found_match and intent=="about_yourself":
               return self.about_yourself()
            elif found_match and intent=="packages":
               return self.packages()
            elif found_match and intent=="eligibility":
              return self.eligibility()
            elif found_match and intent=="Interview_tips_intent":
               return self.Interview_tips_intent()
            elif found_match and intent=="Internship_intent":
               return self.Internship_intent()
            elif found_match and intent=="students_CGPA_intent":
               return self.students_CGPA_intent()
            elif found_match and intent=="staff_recruitment_intent":
              return self.staff_recruitment_intent()
            elif found_match and intent=="staff_salary_intent":
             return self.staff_salary_intent()
            elif found_match and intent=="current_vacany_intent":
              return self.current_vacany_intent()
            if not found_match :
             return self.no_match_intent()
 # defining the intent functions        
    def resume_building_intent(self):
       responses=( """You can use this criteria:
                      1.Review the job description
                      2.Select a formatt
                      3.Add your contact information
                      4.Include your professional summary
                      5.Provide relevant work experience
                      6.Include your educational background
                      7.Highlight your skills""")
       return (responses) 
    def answer_why_hire_intent(self):
      print("You can use this from my side")
      responses= ("""I should be hired for this role because of my relevant skills,
                  experience, and passion for the industry.
                  I've researched the company and can add value to its growth.
                  My positive attitude, work ethics, and long-term goals align with the job requirements, making me a committed and valuable asset to the company./n""",
                 """ You should hire me because I have the qualifications, experience, and attitude to contribute to your company. 
                 I am a quick learner, adaptable, and possess excellent communication and problem-solving skills.
                 Furthermore, I am passionate about this field and eager to contribute to your team's success/n""",
                 """ You should hire me because I know there are more candidates to attend the interview 
                 but I am able to contribute something different from those candidates 
                 because I have an experience in this field, I am also a sincere, responsible, punctual and hard worker having  knowledge of some extra activities like hardware knowledge and I have the confidence on how to handle client and staff with  my communication skills.
                 I have gained so far in  Hindi, Odia and English language and I am also a good cricketer.\n""") 
      return random.choice(responses)
    def about_yourself(self):
        print("Tell me about yourself. You’ll hear these four fairly unassuming words at the beginning of almost any job interview. So,here are some tips for you")
        responses=("""Hey [recruiter name],My name’s [name]. I completed my [qualifying course or training] in [year] and have [x] years of experience working as [relevant position]. While working for [previous company’s name],
                 I developed [soft and hard skills], which I think will apply well to this role.
                   I’ve also been hoping to work on my [ambitions], and I know I’d get the opportunity to do so at [this company] since you value [insert value]. 
                   I look forward to telling you more about my qualifications throughout this call and thank you in advance for your time.\n""",
                 """Hi, I am Shakeel. I am from Delhi. I completed my English Honors from Hindu College which is affiliated to Delhi University.
                     I completed my twelfth grade from Delhi Public School with 89% from CBSE BoardsMy family includes my father who is an engineer, my mother who is a lawyer and my brother who is pursuing his MS in Computer Science from Cornell University.
                     I love playing chess and have represented my school in various district and state level chess competitions.
                     I am also a part of Rotary Club where I have participated in community service at various schools teaching the underprivileged and visiting a number of old age homes.
                     Being part of the Rotary Club has given me a different perspective of life which makes me appreciate what I am and where I am.\n""",
                 """Firstly, thank you very much for giving me this golden opportunity. I am Sapna Sharma. My father, Mr. Shyam Sharma is a teacher and my mother a homemaker. I have 2 other siblings and they are still in school.
                    I completed my engineering from Annamalai University in 2014 and since then, I have been working as a software tester. During my under graduation, I completed several projects on testing, where I excelled in my work and even got certificates for the same.
                   Now, I am interested in expanding my career graph by joining your reputed organization as a software tester where I also look forward to attaining people management opportunity in my area of work.”\n""")
        return random.choice(responses)
    def packages(self):
        responses=("""Average MNC Group fresher salary in India is ₹2.8 Lakhs for less than 1 year of experience. 
                   fresher salary at MNC Group India ranges between ₹2.3 Lakhs to ₹5.3 Lakhs. 
                   According to our estimates it is 10% less than the average fresher Salary in Investment Banking / Venture Capital / Private Equity Companies.\n""",
                   
            )
        return responses
    def eligibility(self):
        responses=("""a majority of companies require a minimum 60 per cent aggregate, 
                   a few companies accept 50 per cent aggregate also in class 10th and 12th, depending on the job role and overall profile of the candidate\n"""
            )
        return (responses)
    def Interview_tips_intent(self):
         print("I got you Buddy! Here are some tips for you")
         responses=("""1.Be prepared: Research the company and practice your answers. 
                       2.Be on time: Try to arrive 10–15 minutes early. 
                       3.Dress professionally: Dress for the job or company. 
                       4.Be polite: Greet the interviewer with a handshake and a smile. 
                       5.Be confident: Be positive and authentic. 
                       6.Be a good listener: Don't talk too much. 
                       7.Ask questions: Have some prepared and ask relevant questions. 
                       8.Make a good impression: Leave a positive first impression. 
                       9.Thank the interviewer: Thank them for their time\n""")
         return (responses)
    def  Internship_intent(self):
        print("Glad to have you here for this...")
        responses=("""Its my pleasure to inform you that we have
                      BCA=20 students
                      MCA=13 students
                      Btech=25 students""")
        return (responses)
    def  staff_recruitment_intent(self):
        responses=("""University recruiting is the process of hiring college students and recent graduates for internships and entry-level positions. The recruitment process involves: 
                      Identifying the work that needs to be done
                      Analyzing the requirements
                      Sorting through applications
                      Screening candidates
                      Selecting the right hire from your shortlist of applicants""")
        return (responses)
    def staff_salary_intent(self):
        responses=("""The average college professor salary in India is ₹ 1,020,000 per year or ₹ 409 per hour.
                      Entry-level positions start at ₹ 450,000 per year, while most experienced workers make up to ₹ 2,025,000 per year.""")
        return (responses)
    def current_vacany_intent(self):
        responses=("""Accountant : 2 vacancy
                      Teacher : 5
                      Worker : 10 
                      Security guard: 7""")
        return responses
    def no_match_intent(self):
       responses =("Please tell me more.\n", "Tell me morel\n", "Why do you say that?\n", 
                   "I see. Can you elaborate?\n", 
                   "Interesting. Can you tell me more?\n",
                   "I see. How do you think?\n", "Why?\n",
                   "How do you think I feel when you say that?\n")
       return random.choice(responses)      
   
alienbot=rulebot()   #creating of instances
alienbot.greet()     #calling the function