import tkinter as tk

def translator (input: str, direction: str = "en2he") -> str:
    en2he = {
    "q": "/", "w": "'", "e": "ק", "r": "ר", "t": "א", "y": "ט", "u": "ו", "i": "ן", "o": "ם", "p": "פ",
    "a": "ש", "s": "ד", "d": "ג", "f": "כ", "g": "ע", "h": "י", "j": "ח", "k": "ל", "l": "ך", ";": "ף",
    "z": "ז", "x": "ס", "c": "ב", "v": "ה", "b": "נ", "n": "מ", "m": "צ", ",": "ת", ".": "ץ",
    }
    he2en = {v:k for k,v in en2he.items()}

    ret = ""
    if direction == "he2en":
        for ch in input:
            ret += he2en.get(ch,ch)
    elif direction == "en2he":
        for ch in input:
            ret += en2he.get(ch,ch)
    return ret

def translate_from_button(direction: str):
    input = input_box.get("1.0", tk.END)
    translated_txt = translator(input, direction)

    output_box.delete("1.0", tk.END) #delete output box content
    output_box.insert(tk.END, translated_txt)


# Create main window
root = tk.Tk()
root.title("English ↔ Hebrew Translator")
root.geometry("400x300")  # optional, sets window size
 #widget of the input box
input_box = tk.Text(root, height=5, width=40)
input_box.pack()
# widget of the output box
output_box = tk.Text(root, height=5, width=40)
output_box.pack()
#button en2he
btn_en2he = tk.Button(root, text="English → Hebrew", command= lambda: translate_from_button("en2he"))
btn_en2he.pack()
#button he2en
btn_he2en = tk.Button(root, text="Hebrew → English", command=lambda: translate_from_button("he2en"))
btn_he2en.pack()



# Run the GUI
root.mainloop()

# print(translator("I ישהק איק כומבאןםמץ Hם' גם I בםמאןמוק כרםצ יקרק?", "he2en"))