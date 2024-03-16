import tkinter as tk
import pyperclip
import pyshorteners

def shorten_url():
    """
    Shorten the URL entered by the user and copy it to the clipboard.
    """
    original_url = url_entry.get()
    try:
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(original_url)
        pyperclip.copy(shortened_url)
        result_label.config(text="Shortened URL copied to clipboard!")
    except pyshorteners.exceptions.ShorteningErrorException as e:
        result_label.config(text="Error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Create URL entry field
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create shorten button
shorten_button = tk.Button(root, text="Shorten", command=shorten_url)
shorten_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the GUI
root.mainloop()
