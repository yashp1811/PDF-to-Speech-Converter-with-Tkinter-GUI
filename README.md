
*PDF to Speech Converter with Tkinter GUI*

This Python script offers a versatile and user-friendly solution for converting PDF files into speech using a graphical user interface (GUI) built with the Tkinter library. The application is designed to enhance accessibility and convenience, allowing users to listen to the contents of PDF documents rather than reading them.

**Key Features:**

1. **Tkinter-based GUI:**
   - The application boasts an intuitive Tkinter-based interface, ensuring ease of use for users with varying levels of technical expertise.

2. **Text-to-Speech Conversion:**
   - Utilizing the powerful pyttsx3 library, the script converts extracted text from PDF files into speech, providing an auditory experience for users.

3. **PDF File Extraction:**
   - PyPDF2 is employed to extract text from PDF files. The script iterates through each page of the PDF, extracting the text content and presenting it in the GUI.

4. **Responsive Threading:**
   - To maintain a responsive user interface, the PDF reading and conversion process is executed in a separate thread. This design choice prevents the GUI from freezing during lengthy operations.

5. **Fullscreen Mode Toggle:**
   - Users can toggle fullscreen mode with the F11 key, optimizing the viewing experience. This feature is especially useful for users who prefer an immersive, distraction-free environment.

**Usage:**

1. **Run the Script:**
   - Execute the script and follow the prompt to enter the path of the PDF file you want to convert.

2. **GUI Display:**
   - The Tkinter window displays the extracted text in a scrolled text widget, allowing users to scroll through the content easily.

3. **Text-to-Speech:**
   - As the text is displayed, the script simultaneously uses pyttsx3 to read the content aloud, providing an accessible and inclusive experience.

4. **Fullscreen Toggle:**
   - Press the F11 key to toggle fullscreen mode, enhancing the visibility of the content.

**Contribution:**
   - Contributions are welcome! Whether you want to add new features, improve existing functionality, or address issues, your input is valued.

**Feedback:**
   - Feel free to provide feedback, report issues, or suggest improvements. Your feedback helps enhance the functionality and usability of the application.

Enhance your PDF reading experience with this PDF to Speech Converter. Experience the convenience of listening to your documents with just a few clicks!
