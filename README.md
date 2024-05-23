<h1>TCP Port Scanner</h1>

<p>This script is a simple TCP port scanner that accepts a hostname or IP address along with a list of ports to scan.</p>

<h2>Usage</h2>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.x</li>
  <li><a href="https://nmap.org/">Nmap</a></li>
</ul>

<h3>Installation</h3>

<ol>
  <li>Clone the repository to your local machine:</li>
</ol>

<pre><code>git clone https://github.com/your_username/your_repository.git
</code></pre>

<ol start="2">
  <li>Install the required Python packages:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Running the Script</h3>

<p>Run the script with the following command:</p>

<pre><code>python port_scanner.py -o &lt;hostname or IP address&gt; -p &lt;comma-separated list of ports&gt;
</code></pre>

<p>Example:</p>

<pre><code>python port_scanner.py -o example.com -p 22,80,443,8080
</code></pre>

<h2>Command Line Arguments</h2>

<ul>
  <li><code>-o, --host</code>: Hostname or IP address to scan.</li>
  <li><code>-p, --ports</code>: Comma-separated list of ports to scan. Example: '22,80,443,8080'</li>
</ul>

<h2>Output</h2>

<p>The script will output the state of each scanned port along with its name (if available).</p>

<h2>Example</h2>

<pre><code>[*] example.com tcp/22 open ssh
[*] example.com tcp/80 closed http
[*] example.com tcp/443 open https
[*] example.com tcp/8080 open http-proxy
</code></pre>

<h2>Error Handling</h2>

<p>If there's an error in the input, the script will display a message prompting the user to provide the correct command line arguments.</p>
