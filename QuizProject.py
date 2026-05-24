from abc import ABC,abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self,answer_user):
        pass

class YesNoQuestion(Question):
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer
    
    def print(self):
        print(f"[?] {self.question} (yes/no)")
    
    def check(self,user_ans):
        if (user_ans=='yes' and self.answer==True) or (user_ans=='no' and self.answer==False):
            return True
        return False

class OpenQuestion(Question):
    def __init__(self,question,answers):
        self.question=question
        self.answers=answers

    def print(self):
        print(f'[?] {self.question}')
    
    def check(self,user_ans):
        return user_ans in self.answers

class MultiOptionsQuestion(Question):
    def __init__(self,question,options,answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index
    
    def print(self):
        print(f"[?] {self.question}\n")
        for i in range(len(self.options)):
            print(f"[{i+1}] {self.options[i]}")
    
    def check(self,user_ans):
        return self.answer_index+1==int(user_ans)

class Quiz:
    def __init__(self,list_questions):
        self.questions=list_questions
    
    def start(self):
        for question in questions:
            question.print()
            print()
            ans=input("[+] ")
            #question.check()
            print()
            print()

    def print_results(self,answers):
        good_ans=sum([1 if x else 0 for x in answers])
        total = len(answers)
        print(f"Your score is {good_ans}/{total}")
        print()
        for i in range(total):
            print(f"[{i+1}] {'Pass' if answers[i] else 'Fail'}")


