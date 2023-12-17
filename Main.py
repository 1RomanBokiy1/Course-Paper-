import tkinter as tk
from tkinter import ttk


class VideoConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Видеоконвертер")
        self.master.config(bg="white")
        self.master.resizable(width=False, height=False)

        self.source_file_label1 = tk.Label(master, text="Выберите первый видеофайл:", bg="white", fg="black")
        self.source_file_label1.grid(row=0, column=0, padx=2, pady=10, sticky="w")

        self.source_file_label1 = tk.Label(master, text="Путь до первого файла:", bg="white", fg="black")
        self.source_file_label1.grid(row=1, column=0, padx=2, pady=10, sticky="w")
        self.source_file_entry1 = tk.Entry(master, width=30, bg="lightgray")
        self.source_file_entry1.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.browse_button1 = tk.Button(master, text="Обзор", bg="white", command=lambda: self.browse_file(1))
        self.browse_button1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.codec_label1 = tk.Label(master, text="Выберите кодек для первого файла:", bg="white", fg="black")
        self.codec_label1.grid(row=2, column=0, padx=1, pady=5, sticky="w")

        self.codecs = ["mp4", "flv", "mov", "avi"]
        self.codec_var1 = tk.StringVar(master)
        self.codec_var1.set(self.codecs[0])

        self.codec_menu1 = ttk.Combobox(master, values=self.codecs, textvariable=self.codec_var1, state="readonly", justify="center")
        self.codec_menu1.set(self.codecs[0])

        self.codec_menu1.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.source_file_label2 = tk.Label(master, text="Выберите второй видеофайл:", bg="white", fg="black")
        self.source_file_label2.grid(row=0, column=2, padx=2, pady=10, sticky="w")

        self.source_file_label1 = tk.Label(master, text="Путь до второго файла:", bg="white", fg="black")
        self.source_file_label1.grid(row=1, column=2, padx=2, pady=10, sticky="w")
        self.source_file_entry2 = tk.Entry(master, width=30, bg="lightgray")
        self.source_file_entry2.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        self.browse_button2 = tk.Button(master, text="Обзор", bg="white", command=lambda: self.browse_file(2))
        self.browse_button2.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.codec_label2 = tk.Label(master, text="Выберите кодек для второго файла:", bg="white", fg="black")
        self.codec_label2.grid(row=2, column=2, padx=1, pady=5, sticky="w")

        self.codec_var2 = tk.StringVar(master)
        self.codec_var2.set(self.codecs[0])

        self.codec_menu2 = ttk.Combobox(master, values=self.codecs, textvariable=self.codec_var2, state="readonly", justify="center")
        self.codec_menu2.set(self.codecs[0])

        self.codec_menu2.grid(row=2, column=3, padx=10, pady=10, sticky="ew")

        self.convert_button = tk.Button(master, text="Конвертировать", bg="white", fg="black", command=self.convert_video)
        self.convert_button.grid(row=3, column=0, columnspan=4, padx=2, pady=10, sticky="nsew")
    def browse_file(self, file_number):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mpeg;*.mov;*.flv;*.webm;*.mkv")])
        if file_number == 1:
            self.source_file_entry1.delete(0, tk.END)
            self.source_file_entry1.insert(0, file_path)
        elif file_number == 2:
            self.source_file_entry2.delete(0, tk.END)
            self.source_file_entry2.insert(0, file_path)