from flask import Flask, request, url_for, render_template
import os
app =Flask(__name__)

    
@app.route('/')
def index():
    images = os.listdir('./static')
    return render_template('image_data.html', data=images)
if __name__ == '__main__':
    app.run(debug=True)
