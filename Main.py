import os
import sys
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from moviepy.editor import VideoFileClip
from tkinter import ttk
import shutil
from pathlib import Path

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
    def convert_video(self):
        source_file1 = self.source_file_entry1.get()
        source_file2 = self.source_file_entry2.get()

        if not source_file1 and not source_file2:
            messagebox.showerror("Ошибка", "Выберите хотя бы один исходный видеофайл")
            return

        try:
            script_dir = Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else Path(
                os.path.dirname(os.path.realpath(__file__)))

            if source_file1:
                temp_file_name_1 = script_dir / Path(f"temp_video_{Path(source_file1).stem}.mp4")

                clip_1 = VideoFileClip(source_file1)
                clip_1.write_videofile(str(temp_file_name_1), codec="libx264", audio_codec="aac")
                clip_1.close()

                output_folder_1 = filedialog.askdirectory()
                if not output_folder_1:
                    messagebox.showerror("Ошибка", "Выберите папку для сохранения первого файла")
                    return

                selected_codec_1 = self.codec_var1.get()
                output_file_name_1 = simpledialog.askstring('Название файла', 'Введите название первого файла')
                if not output_file_name_1:
                    messagebox.showerror("Ошибка", "Введите название первого файла")
                    return

                output_file_1 = Path(output_folder_1) / Path(f"{output_file_name_1}.{selected_codec_1}")

                shutil.move(str(temp_file_name_1), str(output_file_1))

            if source_file2:
                temp_file_name_2 = script_dir / Path(f"temp_video_{Path(source_file2).stem}.mp4")

                clip_2 = VideoFileClip(source_file2)
                clip_2.write_videofile(str(temp_file_name_2), codec="libx264", audio_codec="aac")
                clip_2.close()

                output_folder_2 = filedialog.askdirectory()
                if not output_folder_2:
                    messagebox.showerror("Ошибка", "Выберите папку для сохранения второго файла")
                    return

                selected_codec_2 = self.codec_var2.get()
                output_file_name_2 = simpledialog.askstring('Название файла', 'Введите название второго файла')
                if not output_file_name_2:
                    messagebox.showerror("Ошибка", "Введите название второго файла")
                    return

                output_file_2 = Path(output_folder_2) / Path(f"{output_file_name_2}.{selected_codec_2}")

                shutil.move(str(temp_file_name_2), str(output_file_2))

            messagebox.showinfo("Успех", "Видео успешно сконвертировано!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()
