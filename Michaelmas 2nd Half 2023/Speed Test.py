import random
import time
import datetime

class Speed_Test:
    def init(self):
        self.highscore = 0
        self.previous_time = float(0)
        self.information_package = []

    def compare_lines(self):
        try:
            for i in range(0,len(self.current_line)):
                if self.current_line[i] == self.current_user_input_line[i]:
                    self.character_correct_count += 1
        except IndexError:
            self.character_correct_count = self.character_correct_count

    def single_turn(self):
        print("")
        print(self.current_line)
        print("")
        self.start_current_user_input_time = time.perf_counter()
        self.current_user_input_line = input("")
        self.end_current_user_input_time = time.perf_counter()
        self.compare_lines()
        self.total_character_count = self.total_character_count + len(self.current_user_input_line)
        self.total_word_count = self.character_correct_count / 5
        self.elapsed_time_current_line = self.start_current_user_input_time = self.end_current_user_input_time
        self.run_elapsed_time = self.run_elapsed_time + self.elapsed_time_current_line
        self.run_elapsed_time_minutes = self.run_elapsed_time / 60
        self.correct_typing_speed = self.total_word_count / self.run_elapsed_time_minutes
        print(self.elapsed_time_current_line)
        print(self.run_elapsed_time)
    
    def run_test(self):
        self.scentence_file = open("scentences.txt","r") #file containing paragraphs, each paragraph starts on i *16 line
        self.sentence_dictionary = self.scentence_file.readlines()
        self.character_correct_count = 0
        self.total_character_count = 0
        self.run_elapsed_time = 0
        self.current_scentence_selection = random.randint(0,5)
        self.first_line = self.current_scentence_selection * 16
        blank_line = False
        while not blank_line:
            try:
                self.current_line = self.sentence_dictionary[self.first_line]
            except IndexError:
                pass
            if self.current_line == "":
                blank_line = True
            else:
                self.single_turn()
                self.first_line += 1
        self.information_package = [self.current_scentence_selection , self.correct_typing_speed, self.character_correct_count , self.run_elapsed_time]
        print("")
        print(f"You got {self.character_correct_count} characters correct, that makes {self.total_word_count} words, with an average typing speed of {self.correct_typing_speed} words/minute. This test was test number {self.current_scentence_selection} and took you {self.run_elapsed_time} seconds")
        self.save_run() 

    def save_run(self):
        self.highscore_wpm_file = open("wpm_highscores.txt","a")
        self.full_save_file = open("full_save_file.txt","a")
        self.highscore_wpm_file.write(f"{self.correct_typing_speed}")
        self.highscore_wpm_file.write("\n")
        self.full_save_file.write(f"-- Save at {datetime.datetime.today()} --")
        self.full_save_file.write(f"You got {self.character_correct_count} characters correct, that makes {self.total_word_count} words, with an average typing speed of {self.correct_typing_speed} words/minute. This test was test number {self.current_scentence_selection} and took you {self.run_elapsed_time} seconds")

def menu():
    entered = True
    while entered:
        print("Enter 1 to start or 2 to exit")
        user_input = input("")
        if user_input == "2":
            entered = False
        else:
            test.run_test()

test = Speed_Test()
menu()
