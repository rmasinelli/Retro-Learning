# ui.py
import tkinter as tk
import json

class EduGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Educational Game")
        self.points = 0
        self.load_questions()
        self.create_main_menu()

    def load_questions(self):
        with open('questions.json', 'r') as file:
            self.questions = json.load(file)

    def create_main_menu(self):
        self.clear_window()
        title = tk.Label(self.root, text="Educational Game", font=("Arial", 24))
        title.pack(pady=20)

        # Add buttons for different courses
        intro_python_btn = tk.Button(self.root, text="Intro to Python", command=lambda: self.create_course_menu('intro_python'))
        intro_python_btn.pack(pady=10)

        comptia_core1_btn = tk.Button(self.root, text="CompTIA Core 1", command=lambda: self.create_course_menu('comptia_core1'))
        comptia_core1_btn.pack(pady=10)

        comptia_core2_btn = tk.Button(self.root, text="CompTIA Core 2", command=lambda: self.create_course_menu('comptia_core2'))
        comptia_core2_btn.pack(pady=10)

        server_class_btn = tk.Button(self.root, text="Server Class", command=lambda: self.create_course_menu('server_class'))
        server_class_btn.pack(pady=10)

        quit_btn = tk.Button(self.root, text="Quit", command=self.root.quit)
        quit_btn.pack(pady=10)

    def create_course_menu(self, course):
        self.clear_window()
        self.current_course = course
        
        level1_btn = tk.Button(self.root, text="Level 1", command=lambda: self.start_game(course, 'level1'))
        level1_btn.pack(pady=10)

        level2_btn = tk.Button(self.root, text="Level 2", command=lambda: self.start_game(course, 'level2'))
        level2_btn.pack(pady=10)

        level3_btn = tk.Button(self.root, text="Level 3", command=lambda: self.start_game(course, 'level3'))
        level3_btn.pack(pady=10)

        back_btn = tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu)
        back_btn.pack(pady=10)

    def start_game(self, course, level):
        self.current_course = course
        self.current_level = level
        self.question_index = 0
        self.points = 0
        self.previous_menu = lambda: self.create_course_menu(course)  # Save the previous menu state
        self.show_question()

    def show_question(self):
        self.clear_window()
        questions = self.questions[self.current_course][self.current_level]
        if self.question_index < len(questions):
            question_data = questions[self.question_index]
            question = tk.Label(self.root, text=question_data['question'], font=("Arial", 16))
            question.pack(pady=20)
            
            for option in question_data['options']:
                btn = tk.Button(self.root, text=option, command=lambda opt=option: self.check_answer(opt))
                btn.pack(pady=5)

            back_btn = tk.Button(self.root, text="Back to Course Menu", command=self.previous_menu)
            back_btn.pack(pady=20)

        else:
            self.show_result()

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_course][self.current_level][self.question_index]['answer']
        if selected_option == correct_answer:
            self.points += 10
        self.question_index += 1
        self.show_question()

    def show_result(self):
        self.clear_window()
        result = tk.Label(self.root, text=f"Congratulations! You scored {self.points} points.", font=("Arial", 18))
        result.pack(pady=20)

        main_menu_btn = tk.Button(self.root, text="Main Menu", command=self.create_main_menu)
        main_menu_btn.pack(pady=10)

        course_menu_btn = tk.Button(self.root, text="Back to Course Menu", command=self.previous_menu)
        course_menu_btn.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = EduGame(root)
    root.geometry("400x400")
    root.mainloop()
