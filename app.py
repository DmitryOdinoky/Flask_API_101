import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from script import process_csv


my_absolute_dirpath = os.getcwd()
my_absolute_dirpath.replace('\\' ,'/')
my_absolute_dirpath = my_absolute_dirpath.replace('\\' ,'/')
input_target = f"{my_absolute_dirpath}/input/data_temp_in.csv"
output_target = f"{my_absolute_dirpath}/output/data_temp_out.csv"

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    if __name__ == "__main__":
        app.run(debug=True)
    #app.run(debug=True)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            file = request.files['file']
            if file and allowed_file(file.filename):
                #filename = secure_filename(file.filename)
                #new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
                #dt = str(datetime.now()).replace(" ", "_")
                #save_location = f"{my_absolute_dirpath}/input/data_{dt}.csv"
                
                file.save(input_target)
                output_file = process_csv(input_target)
                
                #return send_from_directory('output', output_file)
            return redirect(url_for('download'))
            #return 'uploaded'

        return render_template('upload.html')

    @app.route('/download')
    def download():
        return render_template('download.html', files=os.listdir('output'))

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('output', filename)

    return app