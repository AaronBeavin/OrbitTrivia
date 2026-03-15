import tkinter as tk
from tkinter import messagebox
import random
import json
import os 

planets = {
    "Mercury": {
        "fact": "Mercury is the closest planet to the Sun.\nA year there lasts only 88 Earth days.",
        "distance": "57.9 million km",
        "size": "4,879 km diameter",
        "moons": 0,
        "day_length": "59 Earth days",
        "year_length": "88 Earth days",
        "fun_fact": "A year on Mercury is shorter than its day!"
    
    },
    "Venus": {
        "fact": "Venus is the hottest planet in the solar system.\nSurface temperatures reach 475°C.",
        "distance": "108.2 million km",
        "size": "12,104 km diameter",
        "moons": 0,
        "day_length":"243 Earth days",
        "year_length":"225 Earth days",
        "fun_fact": "Venus spins backwards compared to most planets!"

    },
    "Earth": {
        "fact": "Earth is the only known planet with life.\nAbout 71% of Earth's surface is water.",
        "distance": "149.6 million km",
        "size": "12,742 km diameter",
        "moons": 1,
        "day_length":"24 hours",
        "year_length":"355.25 days ",
        "fun_fact": "Earth is the densest planet in the solar system!"
    },
    "Mars": {
        "fact": "Mars is called the Red Planet.\nIt has the largest volcano in the solar system.",
        "distance": "227.9 million km",
        "size": "6,779 km diameter",
        "day_length":"24.6 hours",
        "year_length":"687 Earth days",
        "moons": 2,
        "fun_fact": "Olympus Mons on Mars is 3x taller than Mount Everest!"
    },
    "Jupiter": {
        "fact": "Jupiter is the largest planet in the solar system.\nIt has a huge storm called the Great Red Spot.",
        "distance": "778.5 million km",
        "size": "139,820 km diameter",
        "day_length":"10 hours",
        "year_length":"12 Earth years",
        "moons": 95,
        "fun_fact": "Jupiter's Great Red Spot is a storm bigger than Earth!"
    },
    "Saturn": {
        "fact": "Saturn is famous for its beautiful rings made of ice and rock.",
        "distance": "1.43 billion km",
        "size": "116,460 km diameter",
        "day_length":"10.7 hours",
        "year_length":"29 Earth years",
        "moons": 146,
        "fun_fact": "Saturn is so light it could float in water!"
    },
    "Uranus": {
        "fact": "Uranus rotates on its side.\nIt appears blue because of methane gas.",
        "distance": "2.87 billion km",
        "size": "50,724 km diameter",
        "day_length":"17.2 hours",
        "year_length":"84 Earth years",
        "moons": 27,
        "fun_fact": "Uranus was the first planet discovered with a telescope!"
    },
    "Neptune": {
        "fact": "Neptune is the farthest planet from the Sun.\nIt has the fastest winds in the solar system.",
        "distance": "4.50 billion km",
        "size": "49,244 km diameter",
        "day_length":"16 hours",
        "year_length":"165 Earth years",
        "moons": 16,
        "fun_fact": "Neptune was discovered using math before anyone saw it!"
    }
}


quiz_questions = {
    "easy": [
        {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Mercury", "Earth", "Mars"], "answer": "Mercury"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Jupiter", "Saturn", "Mars", "Venus"], "answer": "Mars"},
        {"question": "Which is the largest planet?", "options": ["Saturn", "Jupiter", "Neptune", "Uranus"], "answer": "Jupiter"},
        {"question": "Which planet has beautiful rings?", "options": ["Jupiter", "Uranus", "Neptune", "Saturn"], "answer": "Saturn"},
        {"question": "Which planet supports life?", "options": ["Mars", "Earth", "Venus", "Mercury"], "answer": "Earth"},
        {"question": "How many planets are in our solar system?", "options": ["7", "8", "9", "10"], "answer": "8"},
        {"question": "What is the Sun?", "options": ["Planet", "Moon", "Star", "Asteroid"], "answer": "Star"},
        {"question": "Which planet is farthest from the Sun?","options": ["Uranus","Saturn","Neptune","Pluto"], "answer":"Neptune"},
        {"question": "Which planet is the smallest?","options": ["Mars", "Mercury", "Venus", "Earth"], "answer":"Mercury"},
        {"question": "What does Earth mostly have on its surface?", "options": ["Sand", "Ice", "Water", "Lava"], "answer":"Water"},
    ],
    "medium": [
        {"question": "Which planet rotates on its side?", "options": ["Neptune", "Uranus", "Saturn", "Jupiter"], "answer": "Uranus"},
        {"question": "Which planet is the hottest?", "options": ["Mercury", "Venus", "Mars", "Jupiter"], "answer": "Venus"},
        {"question": "Which planet has the fastest winds?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": "Neptune"},
        {"question": "Which planet has the Great Red Spot?", "options": ["Mars", "Saturn", "Jupiter", "Neptune"], "answer": "Jupiter"},
        {"question": "Which planet spins backwards?", "options": ["Mars", "Venus", "Uranus", "Mercury"], "answer": "Venus"},
        {"question": "Which planet could float in water?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"], "answer": "Saturn"},
        {"question": "Which planet has 95+ known moons?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": "Jupiter"},
        {"question": "How long  is a day on Jupiter?", "options": ["5 hours","10 hours","24 hours","48 hours"],"answer":"10 hours"},
        {"question": "Which planet has the most moons?", "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],"answer":"Saturn" },
        {"question": "Which planet appears blue due to methane?", "options":["Neptune","Earth","Uranus","Both Uranus and Neptune"],"answer":"Both Uranus and Neptune"},
    ],
    "hard": [
        {"question": "What is the tallest volcano in the solar system?", "options": ["Mount Everest", "Olympus Mons", "Mauna Kea", "Mount Etna"], "answer": "Olympus Mons"},
        {"question": "How long is a year on Neptune?", "options": ["84 years", "165 years", "29 years", "12 years"], "answer": "165 years"},
        {"question": "Which planet was discovered using math?", "options": ["Uranus", "Pluto", "Neptune", "Saturn"], "answer": "Neptune"},
        {"question": "How many moons does Mars have?", "options": ["0", "1", "2", "4"], "answer": "2"},
        {"question": "Which planet's day is longer than its year?", "options": ["Mars", "Venus", "Mercury", "Jupiter"], "answer": "Venus"},
        {"question": "What are Saturn's rings made of?", "options": ["Gas", "Fire", "Ice and rock", "Dust only"], "answer": "Ice and rock"},
        {"question": "What percentage of the solar systems's mass is the Sun?","options":["50%","75%","90%","99.86%"],"answer":"99.86%"},
        {"question": "Which moon might have an ocean under its ice?", "options": ["Titan", "Europa", "Ganymede", "Io"], "answer": "Europa"},
        {"question": "How many Earth days is a year on Mercury?", "options": ["88", "165", "225", "365"], "answer": "88"},
        {"question": "Which planet was first discovered with a telescope?", "options": ["Neptune", "Saturn", "Uranus", "Pluto"], "answer": "Uranus"},
    ]
}


score = 0
current_question = 0
selected_questions = []
difficulty = "easy"
timer_seconds = 0
timer_id = None
timer_label = None
answer_buttons = []

window = tk.Tk()
window.title("OrbitTrivia 🌌")
window.geometry("500x600")
window.configure(bg="black")
window.resizable(False, False)

def clear_screen():
    global timer_id
    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None
    for widget in window.winfo_children():
        widget.destroy()


def show_main_menu():
    clear_screen()

    title = tk.Label(window, text="🪐 OrbitTrivia", font=("Arial", 28, "bold"),
                     fg="cyan", bg="black")
    title.pack(pady=25)

    subtitle = tk.Label(window, text="Explore planets & test your space knowledge!",
                        font=("Arial", 11), fg="gray", bg="black")
    subtitle.pack(pady=5)

    line = tk.Label(window, text="━" * 35, fg="#333333", bg="black")
    line.pack(pady=10)

    explore_btn = tk.Button(window, text="🌍  Explore Planets", font=("Arial", 13),
                            width=22, bg="darkblue", fg="white",
                            command=show_planet_list)
    explore_btn.pack(pady=10)

    quiz_btn = tk.Button(window, text="🧠  Start Quiz", font=("Arial", 13),
                         width=22, bg="darkblue", fg="white",
                         command=choose_difficulty)
    quiz_btn.pack(pady=10)

    help_btn = tk.Button(window, text="❓  How to Play", font=("Arial", 13),
                         width=22, bg="darkblue", fg="white",
                         command=show_help)
    help_btn.pack(pady=10)

    footer = tk.Label(window, text="Made by Aaron 🚀 | Flavorthon",
                      font=("Arial", 10), fg="gray", bg="black")
    footer.pack(side="bottom", pady=15)


def show_help():
    clear_screen()

    title = tk.Label(window, text="❓ How to Play", font=("Arial", 22, "bold"),
                     fg="cyan", bg="black")
    title.pack(pady=20)

    instructions = """
🌍 EXPLORE PLANETS
Click on any planet to learn fun facts,
distance from Sun, size, moons, and more!

🧠 QUIZ MODE
Choose Easy, Medium, or Hard difficulty.
Answer 5 random space questions.
You get 15 / 10 / 7 seconds per question!

🏆 SCORING
Each correct answer = 1 point.
Try to get a perfect 5/5!

💡 TIP
Explore planets FIRST to learn facts,
then take the quiz to test yourself!
    """

    info = tk.Label(window, text=instructions, font=("Arial", 11),
                    fg="white", bg="black", justify="left")
    info.pack(pady=10)

    back = tk.Button(window, text="⬅  Back to Menu", font=("Arial", 11),
                     bg="gray", fg="white", command=show_main_menu)
    back.pack(pady=15)


def show_planet_list():
    clear_screen()

    title = tk.Label(window, text="🌌 Choose a Planet", font=("Arial", 22, "bold"),
                     fg="cyan", bg="black")
    title.pack(pady=15)

    for planet in planets:
        btn = tk.Button(window, text=f" {planet}", font=("Arial", 11),
                        width=22, bg="darkblue", fg="white",
                        command=lambda p=planet: show_planet_info(p))
        btn.pack(pady=3)

    back_btn = tk.Button(window, text="⬅ Back to Menu", font=("Arial", 11),
                         bg="gray", fg="white", command=show_main_menu)
    back_btn.pack(pady=15)

def show_planet_info(planet):
    clear_screen()
    data = planets[planet]

    title = tk.Label(window, text=f" {planet}", font=("Arial", 24, "bold"),
                     fg="gold", bg="black")
    title.pack(pady=15)

    
    fact = tk.Label(window, text=data["fact"], font=("Arial", 12),
                    fg="white", bg="black", wraplength=400, justify="center")
    fact.pack(pady=10)

    
    details_frame = tk.Frame(window, bg="#111133", relief="ridge", bd=1)
    details_frame.pack(pady=10, padx=30, fill="x")

    details = [
        f"📏  Distance from Sun: {data['distance']}",
        f"📐  Size: {data['size']}",
        f"🌙  Moons: {data['moons']}",
        f"🌅 Day Length: {data['day_length']}",
        f"📅 Year Length: {data['year_length']}",
    ]

    for d in details:
        lbl = tk.Label(details_frame, text=d, font=("Arial", 11),
                       fg="#cccccc", bg="#111133", anchor="w")
        lbl.pack(pady=3, padx=15, fill="x")

    # Fun fact
    fun = tk.Label(window, text=f"💡 {data['fun_fact']}", font=("Arial", 11, "italic"),
                   fg="gold", bg="black", wraplength=400, justify="center")
    fun.pack(pady=15)

    back_btn = tk.Button(window, text="⬅ Back to Planets", font=("Arial", 11),
                         bg="gray", fg="white", command=show_planet_list)
    back_btn.pack(pady=10)


def choose_difficulty():
    clear_screen()

    title = tk.Label(window, text="🎯 Choose Difficulty", font=("Arial", 22, "bold"),
                     fg="cyan", bg="black")
    title.pack(pady=30)

    easy_btn = tk.Button(window, text="🟢  Easy (15 sec/question)", font=("Arial", 13),
                         width=25, bg="darkgreen", fg="white",
                         command=lambda: start_quiz("easy"))
    easy_btn.pack(pady=10)

    med_btn = tk.Button(window, text="🟡  Medium (10 sec/question)", font=("Arial", 13),
                        width=25, bg="darkorange", fg="white",
                        command=lambda: start_quiz("medium"))
    med_btn.pack(pady=10)

    hard_btn = tk.Button(window, text="🔴  Hard (7 sec/question)", font=("Arial", 13),
                         width=25, bg="darkred", fg="white",
                         command=lambda: start_quiz("hard"))
    hard_btn.pack(pady=10)

    info = tk.Label(window, text="Harder = harder questions + less time!",
                    font=("Arial", 11), fg="gray", bg="black")
    info.pack(pady=15)

    back = tk.Button(window, text="⬅  Back to Menu", font=("Arial", 11),
                     bg="gray", fg="white", command=show_main_menu)
    back.pack(pady=10)


def start_quiz(diff):
    global score, current_question, selected_questions, difficulty
    score = 0
    current_question = 0
    difficulty = diff
    questions = quiz_questions.get(difficulty, quiz_questions["easy"])
    selected_questions = random.sample(questions, min(5, len(questions)))
    show_question()

def get_timer_seconds():
    if difficulty == "easy":
        return 15
    elif difficulty == "medium":
        return 10
    else:
        return 7

def show_question():
    global current_question, timer_seconds, answer_buttons, timer_label
    clear_screen()

    if current_question >= len(selected_questions):
        show_result()
        return

    q = selected_questions[current_question]

    
    top_frame = tk.Frame(window, bg="black")
    top_frame.pack(fill="x", padx=20, pady=10)

    progress = tk.Label(top_frame,
                        text=f"Q{current_question + 1}/{len(selected_questions)}",
                        font=("Arial", 12, "bold"), fg="gray", bg="black")
    progress.pack(side="left")

    diff_colors = {"easy": "lime", "medium": "yellow", "hard": "red"}
    diff_label = tk.Label(top_frame,
                          text=f"  {difficulty.upper()}",
                          font=("Arial", 11, "bold"),
                          fg=diff_colors.get(difficulty, "white"), bg="black")
    diff_label.pack(side="left", padx=10)

    score_label = tk.Label(top_frame,
                           text=f"Score: {score}",
                           font=("Arial", 12, "bold"), fg="gold", bg="black")
    score_label.pack(side="right")

    
    timer_seconds = get_timer_seconds()
    timer_label = tk.Label(window, text=f"⏱️ {timer_seconds}s",
                           font=("Arial", 18, "bold"), fg="lime", bg="black")
    timer_label.pack(pady=5)

    
    question_label = tk.Label(window, text=q["question"],
                              font=("Arial", 15, "bold"),
                              fg="white", bg="black", wraplength=420, justify="center")
    question_label.pack(pady=25)

    
    answer_buttons = []
    for option in q["options"]:
        btn = tk.Button(window, text=option, font=("Arial", 12),
                        width=22, bg="darkblue", fg="white",
                        command=lambda o=option: check_answer(o, q["answer"]))
        btn.pack(pady=5)
        answer_buttons.append(btn)

    
    run_timer(q["answer"])

def run_timer(correct_answer):
    global timer_seconds, timer_id

    if timer_seconds > 0:
        timer_label.config(text=f"⏱️ {timer_seconds}s")

        if timer_seconds <= 3:
            timer_label.config(fg="red")
        elif timer_seconds <= 5:
            timer_label.config(fg="orange")
        else:
            timer_label.config(fg="lime")

        timer_seconds -= 1
        timer_id = window.after(1000, lambda: run_timer(correct_answer))
    else:
        timer_label.config(text="⏱️ TIME'S UP!", fg="red")
        for btn in answer_buttons:
            btn.config(state="disabled")
        messagebox.showwarning("⏱️ Time's Up!",
                               f"The correct answer was: {correct_answer}")
        global current_question
        current_question += 1
        window.after(500, show_question)

def check_answer(selected, correct):
    global score, current_question, timer_id

    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

    for btn in answer_buttons:
        btn.config(state="disabled")

    if selected == correct:
        score += 1
        messagebox.showinfo("✅ Correct!", f"'{selected}' is right! 🎉")
    else:
        messagebox.showerror("❌ Wrong!", f"The correct answer was '{correct}'")

    current_question += 1
    show_question()

def show_result():
    clear_screen()

    title = tk.Label(window, text="🏆 Quiz Complete!", font=("Arial", 24, "bold"),
                     fg="gold", bg="black")
    title.pack(pady=20)

    score_text = f"Your Score: {score}/{len(selected_questions)}"
    score_label = tk.Label(window, text=score_text, font=("Arial", 20, "bold"),
                           fg="white", bg="black")
    score_label.pack(pady=10)

    percentage = int((score / len(selected_questions)) * 100)
    pct_label = tk.Label(window, text=f"{percentage}%",
                         font=("Arial", 32, "bold"), fg="gold", bg="black")
    pct_label.pack(pady=5)

    if score == len(selected_questions):
        msg = "🌟 PERFECT! You're a Space Master!"
        color = "lime"
    elif score >= 4:
        msg = "🚀 Amazing! You really know space!"
        color = "cyan"
    elif score >= 3:
        msg = "⭐ Good job! Keep exploring!"
        color = "gold"
    elif score >= 2:
        msg = "🌌 Not bad! Try exploring planets first!"
        color = "orange"
    else:
        msg = "💫 Keep learning — the universe is huge!"
        color = "red"

    feedback = tk.Label(window, text=msg, font=("Arial", 13),
                        fg=color, bg="black")
    feedback.pack(pady=10)

    diff_label = tk.Label(window, text=f"Difficulty: {difficulty.upper()}",
                          font=("Arial", 11), fg="gray", bg="black")
    diff_label.pack(pady=5)

    retry_btn = tk.Button(window, text="🔄  Try Again", font=("Arial", 12),
                          width=20, bg="darkblue", fg="white",
                          command=lambda: start_quiz(difficulty))
    retry_btn.pack(pady=10)

    menu_btn = tk.Button(window, text="🏠  Back to Menu", font=("Arial", 12),
                         width=20, bg="gray", fg="white",
                         command=show_main_menu)
    menu_btn.pack(pady=5)

show_main_menu()
window.mainloop()