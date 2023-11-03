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

        # Read the content of text.txt
        with open('text.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        count += 1  # Increment count
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
        return

###########################################################################################
def python_scrap():
    from selenium import webdriver
    import time

    import re

    import os

    url = "https://www.real.discount/udemy-coupon-code/"

    # Initialize a webdriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load completely (you can adjust the time as needed)
    driver.implicitly_wait(10)

    # Wait for an additional 10 minutes
    time.sleep(5)

    # Get the content after JavaScript execution
    dynamic_content = driver.page_source
    # Save dynamic_content to a text file
    with open('code/text.txt', 'w', encoding='utf-8') as file:
        file.write(dynamic_content)

    # Append additional text to the file
    # with open('dynamic_content.txt', 'a', encoding='utf-8') as file:
    #     file.write('\nappended text = dynamic_content')
    # Close the browser
    driver.quit()



    # Now 'dynamic_content' contains the HTML after JavaScript execution
    # You can parse it using BeautifulSoup or other methods if needed

    # the code3 which is extracting data from html site ends here##################################################################################
    
    # Part 1: Extract links from html.txt and write to link.txt
    with open('code/text.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    matches = re.findall(r'<a.*?href=[\'"](.*?/offer/.*?)["\']', html_content)

    with open('code/text.txt', 'w', encoding='utf-8') as file:
        for match in matches:
            file.write(match + '\n')

    # Part 2: Remove '/offer/`+ item[' from link.txt
    with open('code/text.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_links = [line.replace('/offer/`+ item[', '') for line in lines]

    with open('code/text.txt', 'w', encoding='utf-8') as file:
        file.writelines(cleaned_links)

    # the link.py which is use to write link like /offer/ ends here ######################################################################

    # Specify the file path
    # file_path = 'test.txt'

    # # Check if the file exists before attempting to delete it
    # if os.path.exists(file_path):
    #     os.remove(file_path)
    #     print(f'{file_path} has been deleted.')
    # else:
    #     print(f'{file_path} does not exist.')



    # Read links from link.txt
    with open('code/text.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()

    # Initialize a webdriver (e.g., Chrome)
    driver = webdriver.Chrome()

    all_contant = ''  # Initialize all_contant before the loop

    for url in links:
        # Construct the full URL
        full_url = "https://www.real.discount/" + url.strip()

        # Navigate to the URL
        driver.get(full_url)

        # Wait for the page to load completely (you can adjust the time as needed)
        driver.implicitly_wait(10)

        # Wait for an additional 3 seconds (if needed)
        time.sleep(3)

        # Get the content after JavaScript execution
        dynamic_content = driver.page_source
        all_contant += dynamic_content  # Concatenate the dynamic content

    # Save dynamic_content to a text file
    #with open('test.txt', 'w', encoding='utf-8') as file:
    with open('code/text.txt', 'w', encoding='utf-8') as file:
        file.write(all_contant + '\n')

    # Close the browser
    driver.quit()


    # the udlink.py which is use to join remaining link with /offer/ and jump to course link and extract each html page ######################

    # Part 1: Extract links from html.txt and write to link.txt
    with open('code/text.txt', 'r', encoding='utf-8') as file:
        html_content = file.read()

    matches = re.findall(r'<a.*?href=[\'"](.*?udemy.com/course.*?)["\']', html_content)

    with open('code/text.txt', 'w', encoding='utf-8') as file:
        for match in matches:
            # Remove text before "https://www.udemy.com/course"
            cleaned_match = re.sub(r'^.*https://www.udemy.com/course', 'https://www.udemy.com/course', match)
            file.write(cleaned_match + '\n')

    #the udlink.py which is use to extract udemy.com main course link for last sand link ends here #######################################




def python_try():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    import os


    def send_email(links, lines):
        lines_list = '\n'.join([f'<li>{line}</li>' for line in lines])
        links_list = '\n'.join([f'<li>{link}</li>' for link in links])

        html = f'''
            <h2>All Links:</h2>
            <ul>
                {lines_list}
            </ul>

            <h2>Interested Links:</h2>
            <ul>
                {links_list}
            </ul>
        '''

        sender_email = "hammadirshad305@outlook.com"
        receiver_emails = maillist

        message = MIMEMultipart()
        message['From'] = 'hammad irshad <hammadirshad305@outlook.com>'
        message['To'] = ', '.join(receiver_emails)
        message['Subject'] = 'Udemy coupon sender python'

        message.attach(MIMEText(html, 'html'))

        try:
            smtp_server = smtplib.SMTP('smtp.office365.com', 587)
            smtp_server.starttls()
            smtp_server.login(sender_email, 'tgyfajllloxuuuim')
            smtp_server.sendmail(sender_email, receiver_emails, message.as_string())
            smtp_server.quit()
            print("Message sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")


    # Initialize an empty list to store links
    links = []
    # Initialize an empty list to store lines
    lines = []
    temp = []

    # Define the list of email addresses
    maillist = [
        'hammadirshad300@gmail.com',
        'hammadirshad23@gmail.com',
        'iqna2018@gmail.com',
    ]

    # Read the contents of text.txt
    with open('code/text.txt', 'r') as file:
        data = file.read()

        with open('code/temp.txt', 'r') as word_file:
            word = word_file.read()
            temp = word.split('\n')

            # Split the file content into an array of lines
            lines = data.split('\n')

            # Iterate through the lines
            for line in lines:
                if any(keyword in line for keyword in ['php', 'python', 'google', 'aws', 'azure', 'scrap', 'bootcamp', 'js', 'language', 'microsoft', 'learn', 'react', 'gcp', 'project', 'learning']):
                    links.append(line.strip())  # Strip to remove any extra spaces
            print(word)
            print(data)
            # If there are links, send an email
            if word != data:
                print("send email run")
                #send_email(links, lines)

            with open('code/temp.txt', 'w') as temp_file:
                temp_file.write('\n'.join(lines))
                print("Data written to file successfully.")


    # def send_email(links, lines):
    #     lines_list = '\n'.join([f'<li>{line}</li>' for line in lines])
    #     links_list = '\n'.join([f'<li>{link}</li>' for link in links])

    #     html = f'''
    #         <h2>All Links:</h2>
    #         <ul>
    #             {lines_list}
    #         </ul>

    #         <h2>Interested Links:</h2>
    #         <ul>
    #             {links_list}
    #         </ul>
    #     '''

    #     sender_email = "hammadirshad305@outlook.com"
    #     receiver_emails = maillist

    #     message = MIMEMultipart()
    #     message['From'] = 'hammad irshad <hammadirshad305@outlook.com>'
    #     message['To'] = ', '.join(receiver_emails)
    #     message['Subject'] = 'Udemy coupon sender'

    #     message.attach(MIMEText(html, 'html'))

    #     try:
    #         smtp_server = smtplib.SMTP('smtp.office365.com', 587)
    #         smtp_server.starttls()
    #         smtp_server.login(sender_email, 'tgyfajllloxuuuim')
    #         smtp_server.sendmail(sender_email, receiver_emails, message.as_string())
    #         smtp_server.quit()
    #         print("Message sent successfully")
    #     except Exception as e:
    #         print(f"Error sending email: {e}")


###############################################################################################







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
        # execute_python_script()
        # execute_mail_script()
        python_scrap()
        python_try()
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
