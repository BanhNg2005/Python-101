# August 21: Learned how to use tkinter to create a simple notepad application

import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button

class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Bao Anh\'s notepad')

        # Text widget
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

        # Overwrite button
        self.overwrite_button: Button = Button(self.button_frame, text='Overwrite', command=self.overwrite_file)
        self.overwrite_button.pack(side=tk.LEFT)

        # Current file path
        self.current_file_path: str = ""

    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt',
                                                      filetypes=[('Text files', '*.txt')])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
                # Update current file path
            self.current_file_path = file_path
            print(f'File saved to: {file_path}')

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                    filetypes=[('Text files', '*.txt')])
        if file_path:
            with open(file_path, 'r') as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
            self.current_file_path = file_path
            print(f'File loaded from: {file_path}')

    def overwrite_file(self) -> None:
        if self.current_file_path:
            with open(self.current_file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f'File overwritten: {self.current_file_path}')
        else:
            self.save_file()

    def run(self) -> None:
        self.root.mainloop()

def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()

if __name__ == '__main__':
    main()