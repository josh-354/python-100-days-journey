import tkinter as tk
from tkinter import messagebox
import time
import threading

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        
        # Sample text
        self.sample_text = "Brylle very handsome and intelligent good coder too hehe"
        
        # Variables
        self.start_time = None
        self.timer_running = False
        self.user_input = ""
        
        # GUI Elements
        self.sample_label = tk.Label(root, text="Sample Text:", font=("Arial", 12))
        self.sample_label.pack(pady=10)
        
        self.sample_text_widget = tk.Text(root, height=4, wrap=tk.WORD, font=("Arial", 10))
        self.sample_text_widget.insert(tk.END, self.sample_text)
        self.sample_text_widget.config(state=tk.DISABLED)
        self.sample_text_widget.pack(pady=5)
        
        self.input_label = tk.Label(root, text="Type here:", font=("Arial", 12))
        self.input_label.pack(pady=10)
        
        self.input_text = tk.Text(root, height=4, wrap=tk.WORD, font=("Arial", 10))
        self.input_text.pack(pady=5)
        self.input_text.bind('<KeyRelease>', self.on_key_release)
        
        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test)
        self.reset_button.pack(pady=10)
        
        self.time_label = tk.Label(root, text="Time: 0.00s", font=("Arial", 12))
        self.time_label.pack()
        
        self.wpm_label = tk.Label(root, text="WPM: 0", font=("Arial", 12))
        self.wpm_label.pack()
        
        self.accuracy_label = tk.Label(root, text="Accuracy: 0%", font=("Arial", 12))
        self.accuracy_label.pack()
        
        # Timer thread
        self.timer_thread = None
    
    def start_test(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.input_text.delete(1.0, tk.END)
            self.input_text.focus()
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.start()
    
    def update_timer(self):
        while self.timer_running:
            elapsed = time.time() - self.start_time
            self.time_label.config(text=f"Time: {elapsed:.2f}s")
            time.sleep(0.1)
    
    def on_key_release(self, event):
        if self.timer_running:
            self.user_input = self.input_text.get(1.0, tk.END).strip()
            if self.user_input == self.sample_text:
                self.end_test()
            self.calculate_stats()
    
    def calculate_stats(self):
        if self.start_time:
            elapsed = time.time() - self.start_time
            words_typed = len(self.user_input.split())
            wpm = (words_typed / elapsed) * 60 if elapsed > 0 else 0
            self.wpm_label.config(text=f"WPM: {int(wpm)}")
            
            # Accuracy calculation
            correct_chars = sum(1 for a, b in zip(self.user_input, self.sample_text) if a == b)
            accuracy = (correct_chars / len(self.sample_text)) * 100 if self.sample_text else 0
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
    
    def end_test(self):
        self.timer_running = False
        messagebox.showinfo("Test Complete", "You finished the test!")
    
    def reset_test(self):
        self.timer_running = False
        self.start_time = None
        self.input_text.delete(1.0, tk.END)
        self.time_label.config(text="Time: 0.00s")
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 0%")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
