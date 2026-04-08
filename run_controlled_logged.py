import subprocess
import time
from datetime import datetime

# All scripts (CPU + RAM)
scripts = [
    "cpu1.py",
    "cpu2.py",
    "cpu3.py",
    "ram1.py",
    "ram2.py",
    "ram3.py"
]

processes = []

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {message}"
    print(log_msg)

    # Save to file
    with open("execution.log", "a") as f:
        f.write(log_msg + "\n")

# -------------------------
# START PHASE
# -------------------------
log("🚀 Starting scripts sequentially...\n")

for script in scripts:
    log(f"Starting {script}...")
    p = subprocess.Popen(["python", script])
    processes.append(p)
    time.sleep(60)  # 1 minute delay

log("✅ All scripts started.\n")

# -------------------------
# STOP PHASE
# -------------------------
log("🛑 Stopping scripts sequentially...\n")

for i, p in enumerate(processes):
    script_name = scripts[i]
    log(f"Stopping {script_name}...")

    p.terminate()
    p.wait()

    log(f"{script_name} stopped.")
    time.sleep(60)

log("✅ All scripts stopped successfully.")