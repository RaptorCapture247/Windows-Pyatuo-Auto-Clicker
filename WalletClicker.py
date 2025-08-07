import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import os

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort
pyautogui.PAUSE = 0.01    # Reduced pause for faster execution

# Print screen size for debugging
screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width}x{screen_height} pixels")

# Base directory for images (Windows path)
BASE_DIR = "C:\\Users\\YourUsername\\Pyautogui\\error"

# Define image conditions: (image_name, action)
IMAGE_CONDITIONS = [
    {"name": "mine.png", "action": "confirm"},
    {"name": "confirm1.png", "action": "confirm"},
    {"name": "confirm2.png", "action": "confirm"},
    {"name": "cancel1.png", "action": "cancel"},
    {"name": "cancel2.png", "action": "cancel"},
    {"name": "confirm3.png", "action": "confirm"},
    {"name": "confirm4.png", "action": "confirm"},
    {"name": "confirm5.png", "action": "confirm"},
    {"name": "cancel3.png", "action": "cancel"},
    {"name": "cancel4.png", "action": "cancel"},
    {"name": "cancel5.png", "action": "cancel"}
]

# Global variables for offsets, running state, and message flag
running = False
confirm_offset_x = 100
confirm_offset_y = 115
cancel_offset_x = -100
cancel_offset_y = 145
message_printed = False  # Flag to ensure message prints only once

# GUI Class
class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoClicker v1.0")
        self.root.geometry("400x500")
        
        # Set background color
        self.root.configure(bg="#2E1A47")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TLabel", background="#2E1A47", foreground="white", font=("Arial", 12))
        style.configure("TEntry", font=("Arial", 12))
        
        # Custom styles for Start and Stop buttons
        style.configure("Start.TButton", font=("Arial", 12, "bold"), foreground="black", background="#00FF00")
        style.map("Start.TButton", background=[("active", "#00CC00")], foreground=[("active", "black")])
        
        style.configure("Stop.TButton", font=("Arial", 12, "bold"), foreground="black", background="#FF0000")
        style.map("Stop.TButton", background=[("active", "#CC0000")], foreground=[("active", "black")])
        
        # Title
        self.title_label = ttk.Label(root, text="Wallet Clicker", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Start/Stop Buttons
        self.start_button = ttk.Button(root, text="Start", style="Start.TButton", width=15, command=self.start_script)
        self.start_button.pack(pady=5)
        print("Start button created")
        
        self.stop_button = ttk.Button(root, text="Stop", style="Stop.TButton", width=15, command=self.stop_script)
        self.stop_button.pack(pady=5)
        print("Stop button created")
        
        # Confirm Offsets
        self.confirm_frame = ttk.LabelFrame(root, text="Confirm Offsets", padding=10)
        self.confirm_frame.pack(pady=10, padx=10, fill="x")
        
        self.confirm_x_label = ttk.Label(self.confirm_frame, text="X Offset:")
        self.confirm_x_label.pack()
        self.confirm_x_entry = ttk.Entry(self.confirm_frame)
        self.confirm_x_entry.insert(0, str(confirm_offset_x))
        self.confirm_x_entry.pack()
        
        self.confirm_y_label = ttk.Label(self.confirm_frame, text="Y Offset:")
        self.confirm_y_label.pack()
        self.confirm_y_entry = ttk.Entry(self.confirm_frame)
        self.confirm_y_entry.insert(0, str(confirm_offset_y))
        self.confirm_y_entry.pack()
        
        # Cancel Offsets
        self.cancel_frame = ttk.LabelFrame(root, text="Cancel Offsets", padding=10)
        self.cancel_frame.pack(pady=10, padx=10, fill="x")
        
        self.cancel_x_label = ttk.Label(self.cancel_frame, text="X Offset:")
        self.cancel_x_label.pack()
        self.cancel_x_entry = ttk.Entry(self.cancel_frame)
        self.cancel_x_entry.insert(0, str(cancel_offset_x))
        self.cancel_x_entry.pack()
        
        self.cancel_y_label = ttk.Label(self.cancel_frame, text="Y Offset:")
        self.cancel_y_label.pack()
        self.cancel_y_entry = ttk.Entry(self.cancel_frame)
        self.cancel_y_entry.insert(0, str(cancel_offset_y))
        self.cancel_y_entry.pack()
        
        # Status Label
        self.status_label = ttk.Label(root, text="Status: Stopped", font=("Arial", 12, "italic"))
        self.status_label.pack(pady=10)
        
        # Bind entry updates to dynamically change offsets
        self.confirm_x_entry.bind("<KeyRelease>", self.update_offsets)
        self.confirm_y_entry.bind("<KeyRelease>", self.update_offsets)
        self.cancel_x_entry.bind("<KeyRelease>", self.update_offsets)
        self.cancel_y_entry.bind("<KeyRelease>", self.update_offsets)

    def update_offsets(self, event=None):
        global confirm_offset_x, confirm_offset_y, cancel_offset_x, cancel_offset_y
        try:
            confirm_offset_x = int(self.confirm_x_entry.get())
            confirm_offset_y = int(self.confirm_y_entry.get())
            cancel_offset_x = int(self.cancel_x_entry.get())
            cancel_offset_y = int(self.cancel_y_entry.get())
            print(f"Updated offsets - Confirm: ({confirm_offset_x}, {confirm_offset_y}), Cancel: ({cancel_offset_x}, {cancel_offset_y})")
        except ValueError:
            print("Invalid offset value entered - please enter integers")

    def start_script(self):
        global running, message_printed
        if not running:
            running = True
            message_printed = False  # Reset flag when starting
            self.status_label.config(text="Status: Running")
            print("Script started")
            self.run_script()

    def stop_script(self):
        global running
        running = False
        self.status_label.config(text="Status: Stopped")
        print("Script stopped")

    def run_script(self):
        global message_printed
        if not running:
            return

        try:
            found = False
            for condition in IMAGE_CONDITIONS:
                image_path = os.path.join(BASE_DIR, condition["name"])
                action = condition["action"]

                # Check if file exists before attempting to locate it
                if not os.path.exists(image_path):
                    if not message_printed:
                        print("additional confirm and cancel image checks available")
                        message_printed = True
                    continue

                # Check for image on screen in real-time
                try:
                    location = pyautogui.locateCenterOnScreen(image_path, confidence=0.9)
                except pyautogui.ImageNotFoundException:
                    continue  # Image exists but isn't on screen, keep checking others
                except Exception as e:
                    continue  # Suppress other errors silently and continue

                if location:
                    found = True
                    x, y = location

                    # Use dynamic offsets (no Retina scaling needed for Windows)
                    if action == "confirm":
                        button_x = x + confirm_offset_x
                        button_y = y + confirm_offset_y
                        button_position = (button_x, button_y)
                        button_name = "Confirm"
                    else:  # action == "cancel"
                        button_x = x + cancel_offset_x
                        button_y = y + cancel_offset_y
                        button_position = (button_x, button_y)
                        button_name = "Cancel"

                    # Check if the coordinates are within screen bounds
                    if (button_x < 0 or button_x >= screen_width or 
                        button_y < 0 or button_y >= screen_height):
                        print(f"{button_name} coordinates ({button_x}, {button_y}) are off-screen!")
                        continue

                    print(f"Found {condition['name']} at: ({x}, {y})")
                    print(f"Clicking {button_name} button at: {button_position}")
                    pyautogui.click(button_position)
                    
                    print(f"Clicked {button_name} button at {button_position}")
                    # Schedule the next check after a delay
                    self.root.after(1000, self.run_script)  # 2 seconds after clicking
                    return

            if not found:
                print("No target pop-up found - waiting...")

        except pyautogui.FailSafeException:
            print("Fail-safe triggered - exiting...")
            self.stop_script()
            return

        except Exception as e:
            print(f"Unexpected error: {str(e)} - continuing...")

        # Schedule the next check if nothing was found
        self.root.after(200, self.run_script)  # Check every 200ms if no image found

# Main execution
if __name__ == "__main__":
    try:
        print("Attempting to initialize Tkinter...")
        root = tk.Tk()
        print("Tkinter initialized successfully.")
        app = AutoClickerGUI(root)
        print("Starting Tkinter mainloop...")
        root.mainloop()
    except tk.TclError as e:
        print(f"Tkinter TclError: {str(e)}")
    except Exception as e:
        print(f"Failed to start GUI: {str(e)}")