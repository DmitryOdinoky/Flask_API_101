import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from script_pandas import process_csv

# import logging

# logging.basicConfig(filename='record.log', level=logging.DEBUG)


my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')
input_target = f"{my_absolute_dirpath}/input/"
output_target = f"{my_absolute_dirpath}/output/"

ALLOWED_EXTENSIONS = set(['csv'])


pTimes = []

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    if __name__ == "__main__":
        app.run(debug=True, threaded=True)
    #app.run(debug=True)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                
                fn = secure_filename(file.filename)

                #fn = f'{fn.split(".")[0]}_{str(datetime.now())}.csv'
                dt = str(datetime.now()).replace(" ", "_")
                dt = str(datetime.now()).replace(":", "-") 
                fn = fn.split(".")[0]
                fn = f"{fn}_{dt}.csv"
                
                
                #save_location = f"{my_absolute_dirpath}/input/data_{dt}.csv"
                
                file.save(input_target+fn)
                output_file, elapsed_time = process_csv(fn)
                
                pTimes.append(elapsed_time)
                
                #return send_from_directory('output', output_file)
            return redirect(url_for('download'))
            #return 'uploaded'

        return render_template('upload.html')

    @app.route('/download')
    def download():
        return render_template('download.html', files=zip(os.listdir('output'), pTimes))

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('output', filename)

    return app