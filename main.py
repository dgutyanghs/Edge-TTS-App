from tkinter import Frame, Tk, BOTH, Text, Menu, END, StringVar, messagebox
from tkinter import filedialog as fd
import subprocess
import tkinter as tk
import os


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Edge-TTS Tool")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff=0)
        aboutMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Import", command=self.onOpen)
        aboutMenu.add_command(label="version: 1.0.0")
        aboutMenu.add_command(label="Author", command=self.onClick)
        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="About", menu=aboutMenu)

        self.filename = tk.StringVar()
        self.filename.set('please import the text file first!')

        labelFilename = tk.Label(
            self.parent, textvariable=self.filename, foreground='red', )
        labelFilename.pack()

        self.languages = ('zh-CN-YunjianNeural', 'zh-CN-XiaoxiaoNeural',
                          'zh-CN-shaanxi-XiaoniNeural', 'en-US-MichelleNeural', 'en-US-RogerNeural')
        self.option_var = tk.StringVar(self.parent)
        self.option_var.set(self.languages[0])

        label = tk.Label(self.parent, text='Select your destination voice')
        label.pack()

        option_menu = tk.OptionMenu(
            self.parent, self.option_var, self.languages[0], *
            self.languages, command=self.option_changed
        )
        option_menu.pack(pady=20)

        # self.output_label = tk.Label(self.parent, foreground='red')
        # self.output_label.pack()
        convertBtn = tk.Button(
            text='convert', command=self.onConvert, foreground='blue', font=('Arial', 14))
        convertBtn.pack(pady=60)

    def option_changed(self, *args):
        # Update the label with the selected option
        self.output_label['text'] = f'You selected: {self.option_var.get()}'

    def onClick(self):
        messagebox.showinfo(title='Contact me', message='dgutyang@gmail.com')

    def onConvert(self):
        print('on convert')
        if hasattr(self, 'fl'):
            convertText(self.fl, self.readTxt, self.option_var.get())
        else:
            messagebox.showerror(title='No text file imported',
                                 message='import text file first!')

    def onOpen(self):
        ftypes = [('Text file', '*.txt'), ('All files', '*')]
        dlg = fd.Open(self, filetypes=ftypes)
        fl = dlg.show()
        self.fl = fl

        if fl != '':
            text = self.readFile(fl)
            # self.txt.insert(END, text)
            self.readTxt = text
            baseFilename = os.path.basename(fl)
            self.baseFilename = baseFilename
            self.filename.set(baseFilename + ' has imported')
            print(self.fl)

    def readFile(self, filename):
        f = open(filename, "r", encoding='utf-8')
        text = f.read()
        return text

    def option_changed(self, *args):
        # Update the label with the selected option
        # self.output_label['text'] = f'You selected: {self.option_var.get()}'
        print(self.option_var.get())


def convertText(fullPathName, txt, voice):
    print('converting ... ', os.path.basename(fullPathName), voice)
    command = [
        'edge-tts',
        '--voice', voice,
        '--text', txt,
        '--write-media', fullPathName + '.mp3',
        '--write-subtitles', fullPathName + '.vtt'
    ]
    # subprocess.run(command, check=True)
    process = subprocess.Popen(command)
    process.wait()  # Wait for the process to finish

    if process.returncode == 0:
        print("Subprocess finished successfully.")
        messagebox.showinfo(message='success')
    else:
        print(f"Subprocess failed with return code: {process.returncode}")
        messagebox.showerror(message='convert error')

def CheckEdgeTTS():
    command = [
        'edge-tts',
        '--list-voices'
    ]
    try:
        ret = subprocess.run(command, check=True)
        print(ret)  # This will be printed after the subprocess has finished
        print("Subprocess finished successfully.")
        messagebox.showinfo(message='success')
    except subprocess.CalledProcessError as e:
        print("There was an error running the command:", e)
        messagebox.showerror(message='convert error')
# ret = subprocess.run(command, check=True)
# print(ret)


def main():
    root = Tk()
    root.geometry("600x450+300+300")
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
