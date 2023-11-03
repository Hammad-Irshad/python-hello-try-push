import subprocess
import time


def execute_python_script():
    try:
        subprocess.run(['python', 'code/main.py'], check=True)
        print("python complete")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing main.py: {e}")

def execute_mail_script():
    try:
        subprocess.run(['python', 'code/try.py'], check=True)
        print("Message sent")
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error executing main.js: {e}")

def main():
    try:
        # execute_python_script()
        # execute_mail_script()
        print("main run")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        # Uncomment the lines below if you want to run initialization and installation
        # initialize_project()
        # install_nodemailer()

        while True:
            main()
            time.sleep(5)  # Send email every 15 minutes
    except Exception as e:
        print(e)
