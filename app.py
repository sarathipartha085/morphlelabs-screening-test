import os
import platform
import time
from datetime import datetime
import getpass
from flask import Flask

app = Flask(__name__)

@app.route("/htop")
def htop():
    username = getpass.getuser() 
    full_name = "Parthasarathi M" 
    mailid = "21z130@psgitech.ac.in"
    server_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S") 
    # Run the top command and capture output
    top_output = os.popen('top -bn1 | head -n 10').read()

    return f"""
    <html>
        <body>
            <h1>HTOP Information</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Mail ID:</strong> {mailid}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre><strong>Top Output:</strong>\n{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
