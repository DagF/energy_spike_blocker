# -*- coding: utf-8 -*-
import json
import os

from flask import Flask, request, render_template

SETTINGS_FIL_NAVN = os.path.dirname(os.path.realpath(__file__)) + '/settings.json'
STATUS_FIL_NAVN = os.path.dirname(os.path.realpath(__file__)) + '/status.json'

STATUSER =[u"av", u"på", u"auto"]
PROSENTER=[70, 75, 80, 85, 90, 100]
SETTINGS_MAL = {
    "navn": "",
    "id": "",
    "trigg": "",
    "modus": "",
}

STATUS_MAL = {
    "status": "",
    "forbruk": ""
}

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():

    if request.method == 'POST':
        navn = request.form.getlist("navn")
        ids = request.form.getlist("id")
        modus= request.form.getlist("modus")
        trigg= request.form.getlist("trigg")

        apparater = []
        for i in range(0, len(navn)):
            if navn[i]:
                apparat = {
                    "navn": navn[i],
                    "id": ids[i],
                    "modus": modus[i],
                    "trigg": int(trigg[i]),
                }
                apparater.append(apparat)

        with open(STATUS_FIL_NAVN , 'w') as outfile:
            json.dump({"apparater":apparater}, outfile, sort_keys=True, indent=4, separators=(',', ': '))

    try:
        with open(STATUS_FIL_NAVN) as data_file:
            data = json.load(data_file)
            apparater = data.get("apparater")
    except:
        with open(STATUS_FIL_NAVN , 'w') as outfile:
            json.dump({"apparater":[]}, outfile)
        with open(STATUS_FIL_NAVN ) as data_file:
            data = json.load(data_file)
            apparater =  data.get("apparater")

    try:
        with open(STATUS_FIL_NAVN) as data_file:
            data = json.load(data_file)
            status = data.get("status")
            forbruk = data.get("forbruk")
    except:
        print(STATUS_FIL_NAVN + "not found")


    return render_template('index.html', statuser=STATUSER, prosenter=PROSENTER, apparater=apparater, status=status , forbruk=forbruk )



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')