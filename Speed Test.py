import random
import time

class Speed_Test:
    def init(self):
        self.highscore = 0
        self.previous_time = float(0)

    def compare_lines(self):

    def single_turn(self):
        print(self.current_line)
        self.start_current_user_input_time = time.perf_counter()
        self.current_user_input_line = input("")
        self.end_current_user_input_time = time.perf_counter()
        try:
            for i in range(0,len(self.current_line)):
                if self.current_line[i] == self.current_user_input_line[i]:
                    self.character_correct_count += 1
        except IndexError:
            self.character_correct_count = self.character_correct_count
        self.total_character_count = self.total_character_count + len(self.current_user_input_line)
        self.elapsed_time_current_line = self.start_current_user_input_time = self.end_current_user_input_time
        self.run_elapsed_time = self.run_elapsed_time + self.elapsed_time_current_line

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
            self.current_line = self.sentence_dictionary[self.first_line]
            if self.current_line == "":
                blank_line = True
            else:
                self.single_turn()
                self.first_line += 1
