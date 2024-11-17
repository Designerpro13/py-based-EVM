import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass
import logging
from contextlib import contextmanager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='voting_system.log'
)

@dataclass
class PollData:
    name: str
    candidates: List[str]
    images: List[str]

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def initialize_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS poll (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            """)
            conn.commit()

    def create_poll_db(self, poll_data: PollData) -> bool:
        try:
            # Create main poll entry
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO poll (name) VALUES (?)', (poll_data.name,))
                conn.commit()

            # Create individual poll database
            poll_db = f"{poll_data.name}.db"
            with sqlite3.connect(poll_db) as poll_conn:
                poll_cursor = poll_conn.cursor()
                poll_cursor.execute("""
                    CREATE TABLE polling (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        votes INTEGER DEFAULT 0,
                        image TEXT
                    )
                """)
                
                # Insert candidates
                for candidate, image in zip(poll_data.candidates, poll_data.images):
                    poll_cursor.execute(
                        'INSERT INTO polling (name, image) VALUES (?, ?)',
                        (candidate, image)
                    )
                poll_conn.commit()
            return True
        except Exception as e:
            logging.error(f"Error creating poll: {str(e)}")
            return False

class VotingSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager('voting_system.db')
        self.setup_ui()
        self.configure_styles()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.configure('TButton', padding=6, relief="flat", background="#333")
        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'))

    def setup_ui(self):
        self.title("Voting System")
        self.geometry("800x600")
        self.configure(bg='#f0f0f0')
        
        # Create main container
        self.main_container = ttk.Frame(self)
        self.main_container.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Label(
            self.main_container, 
            text="Advanced Voting System", 
            style='Header.TLabel'
        )
        header.pack(pady=20)

        # Buttons container
        buttons_frame = ttk.Frame(self.main_container)
        buttons_frame.pack(pady=20)

        buttons = [
            ("Create New Poll", self.create_poll),
            ("View Polls", self.view_polls),
            ("Results", self.show_results),
            ("Settings", self.show_settings),
            ("Exit", self.quit)
        ]

            btn.pack(pady=10)

    def create_poll(self):
        self.poll_window = PollCreationWindow(self)

    def view_polls(self):
        self.polls_window = PollListWindow(self)

    def show_results(self):
        self.results_window = ResultsWindow(self)

    def show_settings(self):
        self.settings_window = SettingsWindow(self)

class PollCreationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create New Poll")
        self.geometry("600x400")
        self.setup_ui()

    def setup_ui(self):
        # Implementation for poll creation UI
        pass

class ResultsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Poll Results")
        self.geometry("600x400")
        self.setup_ui()

    def setup_ui(self):
        # Implementation for results UI
        pass

    def generate_chart(self, poll_data):
        try:
            plt.figure(figsize=(10, 8))
            plt.pie(
                poll_data['votes'],
                labels=poll_data['names'],
                autopct='%1.1f%%',
                shadow=True,
                startangle=90
            )
            plt.axis('equal')
            plt.title(f"Results: {poll_data['poll_name']}")
            plt.show()
        except Exception as e:
            logging.error(f"Error generating chart: {str(e)}")
            messagebox.showerror("Error", "Failed to generate chart")

def main():
    try:
        app = VotingSystem()
        app.mainloop()
    except Exception as e:
        logging.critical(f"Application failed to start: {str(e)}")
        messagebox.showerror("Error", "Application failed to start")

if __name__ == "__main__":
    main()
