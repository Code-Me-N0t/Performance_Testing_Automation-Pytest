# Performance Testing Automation
This repository contains performance testing scripts using pytest to evaluate load time, memory usage, and CPU usage of a web application, with results saved in JSON files for analysis.
</br>
<i><p>Note: This project is for personal usage only. This is designed for automating simple performance tests only and still being improved</p></i></br>
<h3>FEATURES</h3>
• <b>First Load:</b>&nbsp Measures and records the page load times during the first visit of the web application.</br>
• <b>Cached Load:</b>&nbsp Assesses the load times when the web application is accessed from the cache.</br>
• <b>Memory Usage:</b>&nbsp Tracks the initial and peak JavaScript heap size to evaluate memory consumption.</br>
• <b>CPU Usage:</b>&nbsp Monitors CPU usage during the application's operation to gauge performance impact.
</br></br>
<h3>USAGE</h3>
1. Clone the repository:
<pre><code id="code-block">git clone https://github.com/Code-Me-N0t/PerformanceTestingAutomation.git</br>
cd PerformanceTestingAutomation</code></pre>
</br>
2. Install the required dependecies:
<pre><code id="code-block">pip install -r requirements.txt</code></pre>
</br>
3. Run the tests:
<pre><code id="code-block">pytest -s -m firstload</code></pre>
<pre><code id="code-block">pytest -s -m cached</code></pre>
<pre><code id="code-block">pytest -s -m memory</code></pre>
<pre><code id="code-block">pytest -s -m cpu</code></pre>
</br>
<h3>OUTPUT</h3>
• <b>desktop_firstload.json:</b>&nbsp Contains load times and average load time for the first load performance test.</br>
• <b>desktop_cached.json:</b>&nbsp Contains load times and average load time for the cached load performance test.</br>
• <b>memory_stats.json:</b>&nbsp Includes initial and peak JavaScript heap sizes, along with their averages.</br>
• <b>cpu_stats.json:</b>&nbsp Provides initial and highest CPU usage values, along with their averages.
