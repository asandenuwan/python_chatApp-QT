<center><h1>How to Use</h1></center>

<h2>Before running <code>app.py</code>, ensure that the required dependencies are installed.</h2>
<h3>Install PyQt5 using:</h3>

<pre>
pip install PyQt5
</pre>

<h2>After installing the dependencies, you can launch the application without issues.</h2>

<hr>

<center><h1>Contents</h1></center>

<p>
  This project is built using Python's socket programming and PyQt5 for user interface development.
  The application is structured into modular components for clarity and scalability.
</p>

<h3>
  <ul>
    <li><strong><code>gui.py</code></strong> – Contains all GUI components written using PyQt5.</li>
    <li><strong><code>server.py</code></strong> – Handles socket initialization, broadcasting, and message routing.</li>
    <li><strong><code>client.py</code></strong> – Manages user-side socket connections and message sending.</li>
    <li><strong><code>app.py</code></strong> – The main application launcher that connects GUI and backend logic.</li>
  </ul>
</h3>

<hr>

<center><h1>Key Features</h1></center>

<ul>
  <li>✔ Real-time messaging using TCP sockets</li>
  <li>✔ Multi-client chat support</li>
  <li>✔ Clean and responsive PyQt5 interface</li>
  <li>✔ Modular backend and GUI separation</li>
  <li>✔ Lightweight, fast, and easy to run</li>
</ul>

<hr>

<center><h1>System Requirements</h1></center>

<ul>
  <li>Python 3.8 or higher</li>
  <li>PyQt5</li>
  <li>Windows, Linux, or macOS</li>
</ul>

<hr>

<center><h1>Project Architecture</h1></center>

<pre>
+------------------+
|     app.py       |  --> Runs the whole application
+---------+--------+
          |
          v
+------------------+      +-------------------+
|      gui.py      | ---> |   PyQt Interface  |
+---------+--------+      +-------------------+
          |
          v
+------------------+      +-------------------+
|    client.py     | ---> | Client Socket I/O |
+---------+--------+      +-------------------+
          |
          v
+------------------+
|    server.py     | ---> Central message handler
+------------------+
</pre>

<hr>

<center><h1>How It Works</h1></center>

<ol>
  <li>The server starts and waits for client socket connections.</li>
  <li>Each client connects via <code>client.py</code>.</li>
  <li>Messages are sent to the server, which forwards them to all connected clients.</li>
  <li>The GUI updates in real-time using signals and slots.</li>
</ol>

<hr>

<center><h1>Troubleshooting</h1></center>

<ul>
  <li>❗ <strong>Port already in use?</strong><br>
      Change the port number in <code>server.py</code>.</li>

  <li>❗ <strong>Messages not delivering?</strong><br>
      Check your firewall settings or LAN connection.</li>

  <li>❗ <strong>GUI not loading?</strong><br>
      Ensure PyQt5 is installed correctly.</li>
</ul>

<hr>

<center><h1>Future Improvements</h1></center>

<ul>
  <li>🔹 Add user authentication</li>
  <li>🔹 Add emojis & file sending</li>
  <li>🔹 Convert GUI to QML</li>
  <li>🔹 Add encryption to sockets</li>
</ul>

