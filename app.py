from flask import Flask, request, render_template_string
from analyzer import analyze_url

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>URL Safety Analyzer</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
        input[type=text] { width: 100%; padding: 10px; margin: 10px 0; }
        input[type=submit] { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; border: 1px solid #ccc; }
        .safe { background: #d4edda; }
        .unsafe { background: #f8d7da; }
    </style>
</head>
<body>
    <h2>URL Safety Analyzer - IBM Project</h2>
    <form method=post>
        <input type=text name=url placeholder="https://example.com" required>
        <input type=submit value="Analyze URL">
    </form>
    
    {% if result %}
    <div class="result {{ 'safe' if result.verdict == 'SAFE' else 'unsafe' }}">
        <h3>Verdict: {{ result.verdict }}</h3>
        <p><b>Risk Score:</b> {{ result.score }}/100</p>
        <p><b>Reasons:</b> {{ result.reasons }}</p>
    </div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = analyze_url(url)  # ye tera analyzer.py ka function hai
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)