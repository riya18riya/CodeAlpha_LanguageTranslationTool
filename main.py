import tkinter as tk 
from tkinter import ttk
from deep_translator import GoogleTranslator

#Available languages
languages = [
    "English",
    "Hindi",
    "French", 
    "Spanish",
    "German",
    "Japanese",
    "Chinese"
]
# Language codes for translator
language_codes = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}
def translate_text():
    text = input_text.get("1.0",tk.END)

    if text.strip() == "":
        output_text.delete("1.0",tk.END)
        output_text.insert(tk.END,"Please enter some text.")
        return
    
    try:
        source_language=source_combo.get()
        target_language=target_combo.get()

        source_code = language_codes[source_language]
        target_code = language_codes[target_language]

        translator = GoogleTranslator(
            source=source_code,
            target=target_code
        )

        translated_text = translator.translate(text)

        output_text.delete("1.0",tk.END)
        output_text.insert(tk.END,translated_text)

    except Exception:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END,"Translation failed.\nPlease check your internet connection.")    

#create the main window
window = tk.Tk()

# Set the title
window.title("Language Translation Tool")

#Set the window size
window.geometry("700x500")

heading = tk.Label(
    window,
    text="Language Translation Tool",
    font=("Arial",18,"bold")
)
heading.pack(pady=15)

input_label = tk.Label(
    window,
    text="Enter Text:",
    font=("Arial",12)
)
input_label.pack(anchor="w",padx=20)

input_text=tk.Text(
    window,
    height=5,
    width=45,
    font=("Arial",11)
)
input_text.pack(pady=10)

source_label=tk.Label(
    window,
    text="Source Language:",
    font=("Arial",12)
)
source_label.pack(anchor="w",padx=20)

source_combo=ttk.Combobox(
    window,
    values=languages,
    state="readonly",
    width=30
)
source_combo.pack(pady=5)
source_combo.set("English")

target_label=tk.Label(
    window,
    text="Target Language:",
    font=("Arial",12)
)
target_label.pack(anchor="w",padx=20)

target_combo=ttk.Combobox(
    window,
    values=languages,
    state="readonly",
    width=30
)
target_combo.pack(pady=5)
target_combo.set("Hindi")

translate_button=tk.Button(
    window,
    text="Translate",
    font=("Arial",12,"bold"),
    command=translate_text
)
translate_button.pack(pady=15)

output_label=tk.Label(
    window,
    text="Translated Text:",
    font=("Arial",12)
)
output_label.pack(anchor="w",padx=20)

output_text=tk.Text(
    window,
    height=5,
    width=45,
    font=("Arial",11)
)
output_text.pack(pady=10)

#Run the application 
window.mainloop() 