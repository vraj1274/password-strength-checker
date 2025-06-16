import tkinter as tk
from tkinter import ttk
import re

# Global dark mode toggle
is_dark_mode = False

def check_password_strength():
    password = password_entry.get()
    strength_score = 0
    feedback = []

    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("❌ At least 8 characters needed.")

    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Add a lowercase letter.")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one special character.")

    percentage = (strength_score / 5) * 100

    # Determine emoji and color
    if percentage == 100:
        result_text, color = "💪 Very Strong", "green"
    elif percentage >= 80:
        result_text, color = "🙂 Strong", "blue"
    elif percentage >= 60:
        result_text, color = "😐 Moderate", "orange"
    elif percentage >= 40:
        result_text, color = "😟 Weak", "orangered"
    else:
        result_text, color = "😢 Very Weak", "red"

    result_label.config(text=f"{result_text} - {int(percentage)}%", fg=color)

    # Feedback
    feedback_text.config(state="normal")
    feedback_text.delete("1.0", tk.END)
    if feedback:
        for line in feedback:
            feedback_text.insert(tk.END, f"{line}\n")
    else:
        feedback_text.insert(tk.END, "✅ Your password looks good!")
    feedback_text.config(state="disabled")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='Hide')

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    bg_color = "#1e1e1e" if is_dark_mode else "#f0f4f7"
    fg_color = "#ffffff" if is_dark_mode else "#000000"

    root.configure(bg=bg_color)
    for widget in [heading, result_label, feedback_label, password_label, input_frame]:
        widget.configure(bg=bg_color, fg=fg_color)
    feedback_text.configure(bg=bg_color, fg=fg_color, insertbackground=fg_color)
    theme_btn.config(text="🌞 Light Mode" if is_dark_mode else "🌙 Dark Mode")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("460x470")
root.configure(bg="#f0f4f7")
root.resizable(False, False)

# Heading
heading = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#f0f4f7")
heading.pack(pady=(20, 10))

# Input frame
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

password_label = tk.Label(input_frame, text="Enter Password:", font=("Arial", 12), bg="#f0f4f7")
password_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

password_entry = ttk.Entry(input_frame, width=30, show='*')
password_entry.grid(row=1, column=0, padx=5)

toggle_btn = ttk.Button(input_frame, text="Show", width=7, command=toggle_password)
toggle_btn.grid(row=1, column=1, padx=5)

# Check button
ttk.Button(root, text="Check Strength", command=check_password_strength).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f7")
result_label.pack(pady=5)

# Feedback
feedback_label = tk.Label(root, text="Feedback:", font=("Arial", 11), bg="#f0f4f7")
feedback_label.pack(pady=(10, 0))

feedback_text = tk.Text(root, height=7, width=52, font=("Arial", 10), state="disabled")
feedback_text.pack()

# Dark mode toggle
theme_btn = ttk.Button(root, text="🌙 Dark Mode", command=toggle_theme)
theme_btn.pack(pady=10)

root.mainloop()
