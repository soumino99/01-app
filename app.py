from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    if request.method == 'POST':
        file = request.files['csv_file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)

            plt.figure()
            df.plot.box()
            plt.title("Boxplot from CSV")
            path = os.path.join(app.config['UPLOAD_FOLDER'], 'boxplot.png')
            plt.savefig(path)
            plt.close()
            image_url = 'boxplot.png'

    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
