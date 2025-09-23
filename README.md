  <h1>Sentiment Analysis Visualization</h1>

  <p>
    This project visualizes sentiment distribution from a dataset using <b>Python</b>, <b>Pandas</b>, <b>Matplotlib</b>, and <b>Seaborn</b>.  
    It generates <b>enhanced pie charts</b> and <b>bar graphs</b> to help better understand the sentiment spread within a dataset.
  </p>

  <h2>📌 Features</h2>
  <ul>
    <li>Loads a sentiment dataset from CSV</li>
    <li>Handles missing or invalid files gracefully</li>
    <li>Filters out very low-frequency sentiments (&lt;1%)</li>
    <li>Maps <b>0 → Negative</b>, <b>1 → Positive</b>, and assigns automatic labels for other sentiment values</li>
    <li>Generates:
      <ul>
        <li><b>Pie Chart</b> with improved styling</li>
        <li><b>Bar Graph</b> with counts and percentage annotations</li>
      </ul>
    </li>
    <li>Saves charts as <code>.png</code> in the <b>Downloads</b> folder</li>
  </ul>

  <h2>🚀 Getting Started</h2>
  <h3>1. Clone the repository</h3>
  <pre><code>git clone https://github.com/your-username/sentiment-visualization.git
cd sentiment-visualization
</code></pre>

  <h3>2. Install dependencies</h3>
  <p>Make sure you have <b>Python 3.x</b> installed. Then run:</p>
  <pre><code>pip install pandas matplotlib seaborn
</code></pre>

  <h3>3. Add your dataset</h3>
  <p>
    Place your dataset CSV file in the desired location and update the file path in the script:
  </p>
  <pre><code>file_path = '.\\Downloads\\sentimentdataset.csv'
</code></pre>
  <p>⚠️ Your CSV must contain a column named <code>Sentiment</code>.</p>

  <h3>4. Run the script</h3>
  <pre><code>python sentiment_visualization.py
</code></pre>

  <h2>📊 Output Files</h2>
  <p>After running, two files will be generated in your <b>Downloads</b> folder:</p>
  <ul>
    <li><code>enhanced_sentiment_pie_chart.png</code></li>
    <li><code>enhanced_sentiment_bar_chart.png</code></li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li><b>Python 3.x</b></li>
    <li><b>Pandas</b> – data handling</li>
    <li><b>Matplotlib</b> – charting</li>
    <li><b>Seaborn</b> – advanced styling</li>
  </ul>
