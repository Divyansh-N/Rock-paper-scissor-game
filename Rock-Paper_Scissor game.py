import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="#fef9f4")  


def load_image(name):
   
    img = Image.open(name).resize((150, 150))
    return ImageTk.PhotoImage(img)

rock_img = load_image("rock.png")
paper_img = load_image("paper.png")
scissors_img = load_image("scissors.png")

images = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}


def play(choice):
    player_label.config(image=images[choice])
    comp_choice = random.choice(["rock", "paper", "scissors"])
    computer_label.config(image=images[comp_choice])

    if choice == comp_choice:
        result = "🤝 It's a Tie!"
        color = "#777777"
    elif (choice == "rock" and comp_choice == "scissors") or \
         (choice == "paper" and comp_choice == "rock") or \
         (choice == "scissors" and comp_choice == "paper"):
        result = "🎉 You Win!"
        color = "#28a745"
    else:
        result = "😢 Computer Wins!"
        color = "#dc3545"

    result_label.config(text=result, fg=color)


top_frame = tk.Frame(window, bg="#fef9f4")
top_frame.pack(pady=25)

player_label = tk.Label(top_frame, image=rock_img, bg="#ffffff", bd=3, relief="solid")
player_label.grid(row=0, column=0, padx=40)

vs_label = tk.Label(top_frame, text="VS", font=("Helvetica", 26, "bold"), bg="#fef9f4", fg="#444")
vs_label.grid(row=0, column=1, padx=10)

computer_label = tk.Label(top_frame, image=paper_img, bg="#ffffff", bd=3, relief="solid")
computer_label.grid(row=0, column=2, padx=40)


result_label = tk.Label(window, text="", font=("Comic Sans MS", 24, "bold"), bg="#fef9f4")
result_label.pack(pady=20)


button_frame = tk.Frame(window, bg="#fef9f4")
button_frame.pack(pady=20)


def styled_button(img, move):
    return tk.Button(button_frame, image=img, command=lambda: play(move),
                     bd=2, relief="groove", bg="#ffffff", activebackground="#e6f7ff", cursor="hand2")

styled_button(rock_img, "rock").grid(row=0, column=0, padx=25)
styled_button(paper_img, "paper").grid(row=0, column=1, padx=25)
styled_button(scissors_img, "scissors").grid(row=0, column=2, padx=25)


player_label.image = rock_img
computer_label.image = paper_img


window.mainloop()
