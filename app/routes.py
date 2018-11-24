from os import listdir
from os.path import isfile, join

from flask import Flask, render_template

from app import app
from app import utilities


def generate_file_list():
    mypath = "./"
    filelist = []
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for _file in onlyfiles:
        # Remove extension from the filename
        _files = _file.split(".")
        filelist.append(_files[0])

    return filelist


@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)


@app.route('/filelist')
def create_file_list():
    try:
        filel = generate_file_list()
        return render_template('table.html', filelist=filel)
    except Exception as e:
        return str(e)


@app.route('/input')
def input_practice():
    try:
        name = None
        form = utilities.NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''

        return render_template('input.html', form=form, name=name)

    except Exception as e:
        return str(e)


@app.route('/process', methods=['POST'])
def process_input():
    try:
        form = utilities.NameForm()
        print("Form data => " + form.name.data)

        return app
    except Exception as e:
        return str(e)
