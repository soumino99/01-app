from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url = None
    slope = 1  # Initial value
    intercept = 0  # Initial value
    if request.method == 'POST':
        slope = float(request.form.get('slope', 1))
        intercept = float(request.form.get('intercept', 0))
        x = np.linspace(-10, 10, 500)
        y = slope * x + intercept
        plt.figure()
        plt.plot(x, y, label=f"y = {slope}x + {intercept}")
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        plt.title("Linear Function Plot")  # Title in English
        plt.xlabel("x")  # x-axis label in English
        plt.ylabel("y")  # y-axis label in English
        plt.legend()
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'linear_function_plot.png')
        plt.savefig(path)
        plt.close()
        image_url = 'linear_function_plot.png'

    return render_template('index.html', image_url=image_url, slope=slope, intercept=intercept)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
