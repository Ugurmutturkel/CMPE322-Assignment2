
from flask import Flask, request
import threading
import ssl
#import the libraries

#create flask application
app = Flask(__name__)

#route decorator for the reverse URL
@app.route('/reverse', methods=['POST'])
def reverse():
    text = request.form['text']
    reversed_text = text[::-1]
    return reversed_text#reverses the text and returns it

#route decorator for the fibonacci url
@app.route('/fibonacci', methods=['POST'])
def fibonacci():
    position = int(request.form['position'])
    fib_number = calculate_fibonacci(position)
    return str(fib_number)#function to return the fibonacci number

#function to calculate the fibonacci number
def calculate_fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def run_http_server():
    app.run(port=80)#run the http server on the port

def run_https_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('./certificate.crt', './private_key.key')#load the ssl certificate and private key
    app.run(port=443, ssl_context=context)#run the https server on the port

if __name__ == '__main__':
    http_thread = threading.Thread(target=run_http_server)
    https_thread = threading.Thread(target=run_https_server)
#create threads for running http and https servers
    http_thread.start()
    https_thread.start()

    http_thread.join()
    https_thread.join()