import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image


class HappinessCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Happiness Level Calculator")
        self.geometry("1000x700")  # Increased width to accommodate the image

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ctk.CTkFrame(self)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.right_frame = ctk.CTkFrame(self)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(1, weight=1)

        self.hours_relaxing = ctk.DoubleVar(value=4)
        self.hours_socializing = ctk.DoubleVar(value=2)
        self.hours_working = ctk.DoubleVar(value=8)

        self.create_sliders()
        self.create_results_display()
        self.create_chart()
        self.create_message_display()
        self.create_image_display()

        self.update_results()

    def create_sliders(self):
        sliders = [
            ("Hours Relaxing", self.hours_relaxing),
            ("Hours Socializing", self.hours_socializing),
            ("Hours Working", self.hours_working)
        ]

        for i, (label, variable) in enumerate(sliders):
            ctk.CTkLabel(self.left_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            slider = ctk.CTkSlider(self.left_frame, from_=0, to=24, number_of_steps=48, variable=variable)
            slider.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            slider.bind("<ButtonRelease-1>", self.update_results)

    def create_results_display(self):
        self.result_label = ctk.CTkLabel(self.left_frame, text="Happiness Level: 0", font=("Arial", 16, "bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def create_chart(self):
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.left_frame)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def create_message_display(self):
        self.message_label = ctk.CTkLabel(self.left_frame, text="", font=("Arial", 22), wraplength=500)
        self.message_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def create_image_display(self):
        # Replace 'path_to_your_image.png' with the actual path to your image file
        image_path = '/Users/hamiltonn/PycharmProjects/ConceptualCodingAssignment/Week_4_Functions/HappinessGoal.png'

        try:
            image = Image.open(image_path)
            photo = ctk.CTkImage(light_image=image, size=(400, 400))  # Adjust size as needed
            image_label = ctk.CTkLabel(self.right_frame, image=photo, text="")
            image_label.pack(expand=True, fill="both")
        except FileNotFoundError:
            error_label = ctk.CTkLabel(self.right_frame, text="Image not found. Please check the file path.",
                                       wraplength=200, font=("Arial", 12))
            error_label.pack(expand=True)

    def update_results(self, event=None):
        relax_score = self.hours_relaxing.get() * 2
        social_score = self.hours_socializing.get() * 3
        work_score = self.hours_working.get() * -2
        work_life_balance_score = work_score + relax_score
        happiness_level = (relax_score + social_score + work_life_balance_score) // 3

        self.result_label.configure(text=f"Happiness Level: {happiness_level:.0f}")

        self.update_chart(relax_score, social_score, work_life_balance_score)
        self.update_message(happiness_level)

    def update_chart(self, relax_score, social_score, work_life_balance_score):
        self.ax.clear()
        scores = [relax_score, social_score, work_life_balance_score]
        labels = ['Relax Score\n(Hours Relaxing * 2)',
                  'Social Score\n(Hours Socializing * 3)',
                  'Work Life Balance\n(Work Score + Relax Score)']
        bars = self.ax.bar(labels, scores)
        self.ax.set_ylabel('Score')
        self.ax.set_title('Component Scores')

        for bar in bars:
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width() / 2, height,
                         f'{height:.1f}', ha='center', va='bottom')

        self.figure.tight_layout()
        self.canvas.draw()

    def update_message(self, happiness_level):
        message = f"Your Happiness Rating is: {happiness_level:.0f}.\n"
        if happiness_level >= 10:
            message += "You are very happy! Keep up the good work!"
        else:
            message += "You could be happier. Try to improve your scores in each category."
        self.message_label.configure(text=message)


if __name__ == "__main__":
    app = HappinessCalculator()
    app.mainloop()