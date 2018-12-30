import sqlite3
from os import listdir
from os.path import isfile, join

from flask import render_template

from app import app
from app import form_util
from app import roster


def generate_file_list():
    mypath = "./"
    filelist = []
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for _file in onlyfiles:
        # Remove extension from the filename
        _files = _file.split(".")
        filelist.append(_files[0])

    return filelist


def retrieve_church_roster_info(dbFile_name):
    sql_stmt = "SELECT date, event, speaker_chi, speaker_eng, presider, slide_ctrl from roster"
    result_set = []
    print("Attempt open sqlite3 database file: %s" % dbFile_name)
    conn = sqlite3.connect(dbFile_name)
    with conn:
        try:
            cur = conn.cursor()
            rows = cur.execute(sql_stmt)

            for row in rows:
                result_set.append(row)

        except sqlite3.Error as e:
            print("Database error: %s" % e)
        except Exception as e:
            print("Exception in _query: %s" % e)

    if conn:
        print("Close sqlite3 database file: %s" % dbFile_name)
        conn.close()

    return result_set


def render_roster_info(year):
    try:
        rows = retrieve_church_roster_info("/mnt/church_%s.db" % year)
        # rows = retrieve_church_roster_info("church.db")
        param_list = []
        for row in rows:
            param_list.append(roster.info(row[0], row[1], row[2], row[3], row[4], row[5]))

        return render_template('roster_template.html', year=int(year), table_params=param_list)
    except Exception as e:
        return str(e)


@app.route('/2018')
def render_2018_roster():
    return render_roster_info("2018")


@app.route('/2019')
def render_2019_roster():
    return render_roster_info("2019")


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
        form = form_util.NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''

        return render_template('input.html', form=form, name=name)

    except Exception as e:
        return str(e)


@app.route('/process', methods=['POST'])
def process_input():
    try:
        form = form_util.NameForm()
        print("Form data => " + form.name.data)

        return app
    except Exception as e:
        return str(e)
