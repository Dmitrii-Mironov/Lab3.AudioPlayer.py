# 11) Напишите программу для воспроизведения аудиофайлов.

import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

class AudioPlayer:
    def __init__(self, master):
        self.master = master# для создания других виджетов(кнопок) в пределах этого окна
        self.master.title("Audio Player")
        self.master.geometry("500x450")

        pygame.mixer.init()# Инициализация pygame mixer
        self.create_widgets()# Создание элементов интерфейса

    def create_widgets(self):

        self.load_button = tk.Button(self.master, text="Load", command=self.load_audio, \
                                     bg="orange", fg="black", font=("Helvetica", 12, "bold"), width=30, height=3)
        self.load_button.pack(pady=20)

        self.play_button = tk.Button(self.master, text="Play", command=self.play_audio, \
                                     bg="blue", fg="white", font=("Helvetica", 12, "bold"), width=30, height=3)
        self.play_button.pack(pady=20)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_audio, \
                                     bg="purple", fg="pink", font=("Helvetica", 12, "bold"), width=30, height=3)
        self.stop_button.pack(pady=20)

        self.size_button = tk.Button(self.master, text="Set Window Size", command=self.set_window_size, \
                                     bg="brown", fg="yellow", font=("Helvetica", 12, "bold"), width=30, height=3)
        self.size_button.pack(pady=20)

    def load_audio(self):
        try:
            self.file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
            if not self.file_path:
                raise ValueError("No file selected")
            pygame.mixer.music.load(self.file_path)
            messagebox.showinfo("Success", "Audio file loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading audio file: {str(e)}")
