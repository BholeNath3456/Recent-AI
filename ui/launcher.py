import tkinter as tk
from tkinter import font as tkfont
import subprocess
import os
import shutil
import sys

# Ensure root path is accessible
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LauncherGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QuantSignal Launcher")
        self.root.geometry("340x480")
        self.root.configure(bg="#08080e")
        self.root.resizable(False, False)

        # Variables
        self.tf_var = tk.StringVar(value="1m")
        self.dur_var = tk.StringVar(value="1")
        self.engine_process = None

        # Fonts
        self.f_title = tkfont.Font(family="Consolas", size=14, weight="bold")
        self.f_sub = tkfont.Font(family="Consolas", size=10, weight="bold")
        self.f_btn = tkfont.Font(family="Consolas", size=10, weight="bold")

        self.setup_ui()

    def setup_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg="#0e0e18", height=40)
        hdr.pack(fill="x", pady=(0, 10))
        hdr.pack_propagate(False)
        tk.Label(hdr, text="QUANT SIGNAL ENGINE", font=self.f_title, fg="#00f0ff", bg="#0e0e18").pack(pady=8)

        # Timeframe Selection
        tf_frame = tk.Frame(self.root, bg="#08080e")
        tf_frame.pack(fill="x", padx=20, pady=10)
        tk.Label(tf_frame, text="CHART TIMEFRAME:", font=self.f_sub, fg="#888", bg="#08080e").pack(anchor="w")
        
        tf_btn_frame = tk.Frame(tf_frame, bg="#08080e")
        tf_btn_frame.pack(fill="x", pady=5)
        for tf in ["1m", "2m", "3m", "5m"]:
            btn = tk.Radiobutton(tf_btn_frame, text=tf.upper(), variable=self.tf_var, value=tf,
                                 indicatoron=0, width=6, font=self.f_btn, bg="#1a1d24", fg="#fff",
                                 selectcolor="#00f0ff", activebackground="#2a2d34", activeforeground="#00f0ff")
            btn.pack(side="left", padx=2)

        # Duration Selection
        dur_frame = tk.Frame(self.root, bg="#08080e")
        dur_frame.pack(fill="x", padx=20, pady=10)
        tk.Label(dur_frame, text="TRADE DURATION (MIN):", font=self.f_sub, fg="#888", bg="#08080e").pack(anchor="w")
        
        dur_btn_frame = tk.Frame(dur_frame, bg="#08080e")
        dur_btn_frame.pack(fill="x", pady=5)
        for dur in ["1", "2", "3", "5"]:
            btn = tk.Radiobutton(dur_btn_frame, text=dur, variable=self.dur_var, value=dur,
                                 indicatoron=0, width=6, font=self.f_btn, bg="#1a1d24", fg="#fff",
                                 selectcolor="#ff00ff", activebackground="#2a2d34", activeforeground="#ff00ff")
            btn.pack(side="left", padx=2)

        # Actions
        act_frame = tk.Frame(self.root, bg="#08080e")
        act_frame.pack(fill="x", padx=20, pady=20)
        
        self.btn_launch = tk.Button(act_frame, text="▶ START ENGINE", font=self.f_btn, bg="#00aa00", fg="#fff",
                                    activebackground="#00ff00", command=self.launch_engine, height=2, bd=0)
        self.btn_launch.pack(fill="x", pady=5)

        self.btn_stop = tk.Button(act_frame, text="■ STOP ENGINE", font=self.f_btn, bg="#aa0000", fg="#fff",
                                  activebackground="#ff0000", command=self.stop_engine, height=2, bd=0, state="disabled")
        self.btn_stop.pack(fill="x", pady=5)

        self.btn_clean = tk.Button(act_frame, text="⟳ CLEAR CACHES & RESTART", font=self.f_btn, bg="#444", fg="#fff",
                                   activebackground="#666", command=self.clear_and_restart, height=2, bd=0)
        self.btn_clean.pack(fill="x", pady=5)
        
        self.lbl_status = tk.Label(self.root, text="Status: Ready", font=self.f_sub, fg="#888", bg="#08080e")
        self.lbl_status.pack(side="bottom", pady=10)

    def launch_engine(self):
        if self.engine_process is None or self.engine_process.poll() is not None:
            self.lbl_status.config(text=f"Status: Running ({self.tf_var.get()} TF, {self.dur_var.get()}m Dur)", fg="#00f0ff")
            self.btn_launch.config(state="disabled")
            self.btn_stop.config(state="normal")
            
            # Start main.py as a subprocess
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            main_script = os.path.join(root_dir, "main.py")
            
            # Start main.py as a subprocess with a new dedicated console window so logs are visible
            # and stdout doesn't block/crash the background process.
            creationflags = 0
            if sys.platform == "win32":
                creationflags = subprocess.CREATE_NEW_CONSOLE
                
            self.engine_process = subprocess.Popen(
                [sys.executable, main_script, "--timeframe", self.tf_var.get(), "--duration", self.dur_var.get()],
                cwd=root_dir,
                creationflags=creationflags
            )
            # Minimize launcher so they can see the chart and overlay
            self.root.iconify()
            
            # Poll to see if it dies
            self.root.after(1000, self.check_engine_status)

    def check_engine_status(self):
        if self.engine_process is not None:
            if self.engine_process.poll() is not None:
                # Process ended
                self.engine_process = None
                self.lbl_status.config(text="Status: Stopped", fg="#ff00ff")
                self.btn_launch.config(state="normal")
                self.btn_stop.config(state="disabled")
                self.root.deiconify() # Bring launcher back up
            else:
                self.root.after(1000, self.check_engine_status)

    def stop_engine(self):
        if self.engine_process and self.engine_process.poll() is None:
            self.engine_process.terminate()
            try:
                self.engine_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
        self.engine_process = None
        self.lbl_status.config(text="Status: Stopped", fg="#ff00ff")
        self.btn_launch.config(state="normal")
        self.btn_stop.config(state="disabled")
        self.root.deiconify()

    def clear_and_restart(self):
        self.stop_engine()
        self.lbl_status.config(text="Status: Clearing caches...", fg="#ffaa00")
        self.root.update()
        
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # 1. Clear __pycache__
        for dirpath, dirnames, _ in os.walk(root_dir):
            for d in dirnames:
                if d == '__pycache__':
                    try:
                        shutil.rmtree(os.path.join(dirpath, d), ignore_errors=True)
                    except:
                        pass
                        
        # 2. Clear data/ files
        data_dir = os.path.join(root_dir, "data")
        if os.path.exists(data_dir):
            for f in os.listdir(data_dir):
                if f.endswith(".json") or f.endswith(".log") or f.endswith(".pyc"):
                    try:
                        os.remove(os.path.join(data_dir, f))
                    except:
                        pass
                        
        self.lbl_status.config(text="Status: Caches Cleared. Restarting...", fg="#00ff00")
        self.root.update()
        self.root.after(500, self.launch_engine)

if __name__ == "__main__":
    app = LauncherGUI()
    app.root.mainloop()
