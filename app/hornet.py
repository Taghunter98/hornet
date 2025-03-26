from PySide6 import QtCore, QtWidgets, QtGui
from search import search
import sys

class HornetGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Main container
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Components
        self.title = QtWidgets.QLabel("Hornet")
        self.description = QtWidgets.QLabel("Generate suitable Spelling Bee words from letters.")
        self.result = QtWidgets.QTextEdit()
        self.button = QtWidgets.QPushButton("Generate Words")

        # Style header
        self.title.setFont(QtGui.QFont("Arial", 32, QtGui.QFont.Bold))
        self.description.setFont(QtGui.QFont("Arial", 18))
        
        # Letter container
        self.letter_container = QtWidgets.QHBoxLayout()

        # Generate letter inputs and labels dynamically
        self.letters = [] 

        for i in range(6): 
            container = QtWidgets.QHBoxLayout() 
            label = QtWidgets.QLabel(f"Letter {i+1}")  
            letter = QtWidgets.QLineEdit()  
            letter.setFixedSize(30, 30)  # Set size
    
            self.letters.append(letter)  

            container.addWidget(letter) 
            container.addWidget(label)  
            self.letter_container.addLayout(container)  
            
        # Create main character input with a label
        primary_container = QtWidgets.QHBoxLayout()
        self.main_label = QtWidgets.QLabel("Main Char")
        self.main_char = QtWidgets.QLineEdit()
        self.main_char.setFixedSize(30, 30)

        primary_container.addWidget(self.main_char)
        primary_container.addWidget(self.main_label)
        self.letter_container.addLayout(primary_container)

        # Output box
        self.result.setPlaceholderText("Letters will appear here...")
        self.result.setReadOnly(True)

        # Build main layout
        self.main_layout.addWidget(self.title)
        self.main_layout.addWidget(self.description)
        self.main_layout.addLayout(self.letter_container)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.result)

        # Connect button
        self.button.clicked.connect(self.getWords)

    def getWords(self):
        # Get all the letters from the input
        letters = [letter.text().strip() for letter in self.letters if letter.text().strip()]
        
        main_letter = self.main_char.text().strip()
        
        if not main_letter:
            self.result.setText("Error, invalid characters.")
            return
        
        letters.append(main_letter[0]) # Append the main letter before calling function

        dictionary = set(open("words.txt", 'r').read().lower().splitlines())

        words = search(dictionary, letters, main_letter)
        
        # Update result 
        if words:
            self.result.setText(",\n".join(words)) 
        else:
            self.result.setText("No valid words found.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = HornetGUI()
    # widget.resize(650, 500)
    widget.show()
    sys.exit(app.exec())