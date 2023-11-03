# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write('Hello, world!'.encode('utf-8'))
#         return


from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import time
import threading

count = 0

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        global count
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str(count).encode('utf-8'))
        return

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
        raise Exception(f"Error executing try.py: {e}")

def main():
    try:
        execute_python_script()
        execute_mail_script()
        print("main run")
    except Exception as e:
        print(e)

def start_server():
    try:
        server = HTTPServer(('localhost', 8000), handler)
        print('Started HTTP server')
        server.serve_forever()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        threading.Thread(target=start_server).start()

        while True:
            main()
            print(count)
            count = count + 1  # Increment count
            time.sleep(5)  # Send email every 5 seconds
    except Exception as e:
        print(e)
