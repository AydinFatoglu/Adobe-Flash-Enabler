import tkinter as tk
import tkinter.font as tkFont
import subprocess
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def register_ocx(file_path):
    command = f'regsvr32 /s "{file_path}"'
    try:
        subprocess.run(command, check=True, shell=True)
        result_label.config(text=f"Successfully registered")
    except subprocess.CalledProcessError as e:
        result_label.config(text=f"Failed to register : {e}")

def unregister_ocx(file_path):
    command = f'regsvr32 /s /u "{file_path}"'
    try:
        subprocess.run(command, check=True, shell=True)
        result_label.config(text=f"Successfully unregistered")
    except subprocess.CalledProcessError as e:
        result_label.config(text=f"Failed to unregister: {e}")

def on_register_button_click():
    if not is_admin():
        result_label.config(text="You don't have administrative privileges. Please run the program as an administrator.", fg='red')
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    ocx_file = os.path.join(current_dir, 'Flash32_34_0_0_301.ocx')

    if os.path.exists(ocx_file):
        register_ocx(ocx_file)
    else:
        result_label.config(text="Some files are not found. Please ensure they are in the same directory as this program.", fg='black')

def on_unregister_button_click():
    if not is_admin():
        result_label.config(text="You don't have administrative privileges. Please run the program as an administrator.", fg='red')
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    ocx_file = os.path.join(current_dir, 'Flash32_34_0_0_301.ocx')

    if os.path.exists(ocx_file):
        unregister_ocx(ocx_file)
    else:
        result_label.config(text="Some files are not found. Please ensure they are in the same directory as this program.", fg='black')

root = tk.Tk()
root.title("Flash Player ActiveX x86 Enabler")
# this removes the maximize button
root.resizable(0,0)

# Set window dimensions and center
window_width = 480
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((screen_width/2) - (window_width/2))
center_y = int((screen_height/2) - (window_height/2))
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

instruction_label = tk.Label(root, text="This program will enable or disable the Flash Player ActiveX control on Windows 10 / 11\nPlease ensure you have administrative privileges before proceeding.\nKeep in mind that a reboot is required changes to take effect.", justify=tk.LEFT)
instruction_label.pack(pady=10)

bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
bold_label = tk.Label(root, text="BY AYDIN FATOGLU", font=bold_font)
bold_label.pack()

register_button = tk.Button(root, text="Enable Flash Player ActiveX (x86)", command=on_register_button_click)
register_button.pack(pady=5)

unregister_button = tk.Button(root, text="Disable Flash Player ActiveX (x86)", command=on_unregister_button_click)
unregister_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

