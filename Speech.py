import tkinter as tk
from idlelib import window
from tkinter import scrolledtext
import pyttsx3
import PyPDF2
import threading

def read_pdf(pdf_path, text_widget):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PdfFileReader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize text-to-speech engine
            speak = pyttsx3.init()

            # Loop through all pages and extract text
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()

                # Display the extracted text in the Tkinter window
                text_widget.insert(tk.END, text)
                text_widget.insert(tk.END, "\n\n")

                # Read the extracted text aloud
                speak.say(text)
                speak.runAndWait()

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    window.attributes('-fullscreen', fullscreen)

def start_gui(pdf_path):
    # Create a Tkinter window
    window = tk.Tk()
    window.title("PDF to Speech")

    # Create a scrolled text widget to display the text
    text_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20)
    text_widget.pack(padx=100, pady=10)
    text_widget.pack(fill=tk.BOTH, expand=True, padx=100, pady=10)

    # Create a thread to run the PDF reading function
    pdf_thread = threading.Thread(target=read_pdf, args=(pdf_path, text_widget))

    # Start the thread
    pdf_thread.start()

    # Bind the F11 key to toggle fullscreen
    fullscreen = False
    window.bind('<F11>', toggle_fullscreen)

    # Bind the Escape key to exit fullscreen
    window.bind('<Escape>', toggle_fullscreen)

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    # Prompt user for PDF file path
    pdf_path = input("Enter the path of the PDF file: ")

    # Call the function to start the Tkinter window and read the PDF
    start_gui(pdf_path)
