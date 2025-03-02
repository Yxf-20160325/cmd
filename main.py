import tkinter as tk
import subprocess as sp
root = tk.Tk()
root.title("cmd工具")
root.geometry("600x600")
label = tk.Label(root, text="命令")
label.pack()
entry = tk.Entry(root)
entry.pack()
command_1 = entry.get()
def run_command():
	command = entry.get()
	sp.Popen(command, shell=True)
	
	
button = tk.Button(root,text="执行",command=lambda:run_command())
button.pack()

def kill_python():
	
	command3 = "taskkill /f /im ping.exe"
	sp.Popen(command3, shell=True)
	command_2 = "taskkill /f /im cmd.exe"
	sp.Popen(command_2, shell=True)
	command = "taskkill /f /im python.exe"
	
	sp.Popen(command, shell=True)
button2 = tk.Button(root,text="停止并关闭",command=lambda:kill_python())
button2.pack()
root.mainloop()
