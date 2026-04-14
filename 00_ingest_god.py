import os
import shutil

def ingest_god():
    print("--- [INGEST GOD] ---")
    source = "C:\\Users\\User\\Desktop\\Ingest God"
    dest = os.getcwd()
    
    if not os.path.exists(source):
        print("SOURCE VACUUMED. LOGIC ANCHORED.")
        return

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
        print(f"ABSORBED: {item}")
    
    print("--- RESTRUCTURING COMPLETE: ZERO-DRIFT ACHIEVED ---")

if __name__ == "__main__":
    ingest_god()
