# root = tk.Tk()
# root.title("Thai Transliterator")


# thai_value = tk.StringVar()
# translit_value = tk.StringVar()

# def transliterate():
#     pass

# def copy():

#     pc.copy(text_translit.get("1.0","end"))

# def paste():
#     thai_value.set(pc.paste())



# main = ttk.Frame(root, padding=(30,15))
# # main.grid()

# text_thai = tk.Text(root, height=10)
# text_translit = tk.Text(root, height=10)
# text_translit["state"] = "disabled"

# submit_button = ttk.Button(main, text="Transliterate!", command=copy)
# text_translit.insert("1.0", "chan chawp maew")
# text_thai.pack(fill=tk.X)
# text_translit.pack(fill=tk.X)
# submit_button.pack(fill=tk.X)

# # text_thai.grid(column=0, row=0, columnspan=2)
# # text_translit.grid(column=0, row=1, columnspan=2)
# # submit_button.grid(column=0, row=2, columnspan=2, sticky="EW")

# root.bind("<Return>", transliterate)
# root.bind("<KP_Enter>", transliterate)



# root.mainloop()