import tkinter as tk
import random

# ---------------- GAME VARIABLES ---------------- #

secret_number = random.randint(1, 100)
attempts = 0

# ---------------- FUNCTIONS ---------------- #

def check_guess(event=None):
    global attempts

    try:
        guess = int(entry.get())

        if guess < 1 or guess > 100:
            result_label.config(
                text="⚠ Please enter a number between 1 and 100",
                fg="red"
            )
            return

        attempts += 1
        attempt_label.config(text=f"Attempts: {attempts}")

        if guess < secret_number:
            result_label.config(
                text="📉 Too Low! Try Again.",
                fg="orange"
            )

        elif guess > secret_number:
            result_label.config(
                text="📈 Too High! Try Again.",
                fg="orange"
            )

        else:
            winner_label.config(
                text="🏆 YOU WIN! 🏆"
            )

            result_label.config(
                text=f"🎉 Congratulations! You guessed the number in {attempts} attempts.",
                fg="green"
            )

            guess_btn.config(state="disabled")
            entry.config(state="disabled")

        entry.delete(0, tk.END)

    except ValueError:
        result_label.config(
            text="⚠ Please enter a valid number",
            fg="red"
        )

def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempt_label.config(text="Attempts: 0")

    result_label.config(
        text="Guess a number between 1 and 100",
        fg="#1f4e79"
    )

    winner_label.config(text="")

    entry.config(state="normal")
    guess_btn.config(state="normal")

    entry.delete(0, tk.END)
    entry.focus()

def backspace(event=None):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def exit_fullscreen(event):
    root.attributes("-fullscreen", False)

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Number Guessing Game")
root.attributes("-fullscreen", True)
root.configure(bg="#dfeaf5")

# ---------------- MAIN FRAME ---------------- #

frame = tk.Frame(
    root,
    bg="white",
    bd=4,
    relief="ridge"
)

frame.pack(
    expand=True,
    fill="both",
    padx=60,
    pady=60
)

# ---------------- TITLE ---------------- #

title = tk.Label(
    frame,
    text="🎯 Number Guessing Game",
    font=("Arial", 40, "bold"),
    bg="white",
    fg="#1f4e79"
)

title.pack(pady=40)

# ---------------- INSTRUCTION ---------------- #

instruction = tk.Label(
    frame,
    text="Guess a Number Between 1 and 100",
    font=("Arial", 22),
    bg="white"
)

instruction.pack(pady=10)

# ---------------- ENTRY ---------------- #

entry = tk.Entry(
    frame,
    font=("Arial", 24),
    justify="center",
    width=20
)

entry.pack(pady=20)
entry.focus()

# ---------------- ATTEMPTS ---------------- #

attempt_label = tk.Label(
    frame,
    text="Attempts: 0",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#555"
)

attempt_label.pack(pady=10)

# ---------------- BUTTONS ---------------- #

guess_btn = tk.Button(
    frame,
    text="Check Guess",
    command=check_guess,
    font=("Arial", 18, "bold"),
    bg="#28a745",
    fg="white",
    width=20,
    height=2
)

guess_btn.pack(pady=15)

restart_btn = tk.Button(
    frame,
    text="Restart Game",
    command=restart_game,
    font=("Arial", 18, "bold"),
    bg="#dc3545",
    fg="white",
    width=20,
    height=2
)

restart_btn.pack(pady=15)

# ---------------- WINNER LABEL ---------------- #

winner_label = tk.Label(
    frame,
    text="",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="green"
)

winner_label.pack(pady=20)

# ---------------- RESULT ---------------- #

result_label = tk.Label(
    frame,
    text="Guess a number between 1 and 100",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#1f4e79",
    wraplength=1000
)

result_label.pack(pady=20)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Press Enter to Check | Backspace to Delete | ESC to Exit Full Screen",
    font=("Arial", 12),
    bg="#dfeaf5",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- KEYBOARD SUPPORT ---------------- #

root.bind("<Return>", check_guess)
root.bind("<BackSpace>", backspace)
root.bind("<Escape>", exit_fullscreen)

# ---------------- RUN ---------------- #

root.mainloop()