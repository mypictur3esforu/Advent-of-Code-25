#!/usr/bin/env python3
# inputhandler.py
# Small GUI to accept user input via text field or by loading a file.

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from day2 import day2
from day2_2 import day2_2

def process_input(text: str):
   # day = day2
   print(day2_2.solve(text))

def load_file_into_text(widget: scrolledtext.ScrolledText):
   path = filedialog.askopenfilename(title="Open input file")
   if not path:
      return
   try:
      with open(path, "r", encoding="utf-8") as f:
         data = f.read()
   except Exception as e:
      messagebox.showerror("Error", f"Could not read file:\n{e}")
      return
   widget.delete("1.0", tk.END)
   widget.insert(tk.END, data)

def save_text_to_file(widget: scrolledtext.ScrolledText):
   path = filedialog.asksaveasfilename(title="Save input as", defaultextension=".txt")
   if not path:
      return
   try:
      with open(path, "w", encoding="utf-8") as f:
         f.write(widget.get("1.0", tk.END).rstrip("\n"))
   except Exception as e:
      messagebox.showerror("Error", f"Could not save file:\n{e}")
      return
   messagebox.showinfo("Saved", f"Saved to {path}")

def main():
   root = tk.Tk()
   root.title("Input Handler")
   root.geometry("700x500")

   txt = scrolledtext.ScrolledText(root, wrap=tk.NONE, undo=True)
   txt.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

   frm = tk.Frame(root)
   frm.pack(fill=tk.X, padx=8, pady=(0,8))

   btn_load = tk.Button(frm, text="Load File...", command=lambda: load_file_into_text(txt))
   btn_save = tk.Button(frm, text="Save As...", command=lambda: save_text_to_file(txt))
   btn_clear = tk.Button(frm, text="Clear", command=lambda: txt.delete("1.0", tk.END))
   btn_process = tk.Button(frm, text="Process Input", command=lambda: process_input(txt.get("1.0", tk.END)))

   btn_load.pack(side=tk.LEFT, padx=4)
   btn_save.pack(side=tk.LEFT, padx=4)
   btn_clear.pack(side=tk.LEFT, padx=4)
   btn_process.pack(side=tk.RIGHT, padx=4)

   root.mainloop()

if __name__ == "__main__":
   main()