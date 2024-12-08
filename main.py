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
