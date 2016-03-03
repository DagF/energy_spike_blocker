# -*- coding: utf-8 -*-
import json
import os

from flask import Flask, request, render_template

APPARATER_FIL_NAVN = os.path.dirname(os.path.realpath(__file__)) + '/apparater.json'
STATUSER =[u"av", u"på", u"auto"]
PROSENTER=[50, 60, 70, 80, 90, 100]
APPARAT_MAL = {
                "apparat_navn": "",
                "apparat_beskrivelse": "",
                "apparat_slaes_av_ved": "",
                "apparat_status": "",
            }

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    stromforbruk_i_prosent = 40
    stromforbruk_i_kw = 123

    if request.method == 'POST':
        apparat_navn = request.form.getlist("apparat_navn")
        apparat_beskrivelse = request.form.getlist("apparat_beskrivelse")
        apparat_status = request.form.getlist("apparat_status")
        apparat_slaes_av_ved = request.form.getlist("apparat_slaes_av_ved")
        print(apparat_navn)
        print(apparat_beskrivelse)
        print(apparat_status)
        print(apparat_slaes_av_ved)

        apparater = []
        for i in range(0, len(apparat_navn)):
            if apparat_navn[i]:
                apparat = {
                            "navn": apparat_navn[i],
                            "beskrivelse": apparat_beskrivelse[i],
                            "status": apparat_status[i],
                            "slaes_av_ved": int(apparat_slaes_av_ved[i]),
                        }
                apparater.append(apparat)

        with open(APPARATER_FIL_NAVN , 'w') as outfile:
            json.dump({"apparater":apparater}, outfile, sort_keys=True, indent=4, separators=(',', ': '))

    try:
        with open(APPARATER_FIL_NAVN) as data_file:
            data = json.load(data_file)
            apparater = data.get("apparater")
    except:
        with open(APPARATER_FIL_NAVN , 'w') as outfile:
            json.dump({"apparater":[]}, outfile)
        with open(APPARATER_FIL_NAVN ) as data_file:
            data = json.load(data_file)
            apparater =  data.get("apparater")

    apparater.append(APPARAT_MAL)

    return render_template('index.html', statuser=STATUSER, prosenter=PROSENTER, apparater=apparater, stromforbruk_i_prosent=stromforbruk_i_prosent, stromforbruk_i_kw=stromforbruk_i_kw)



if __name__ == '__main__':
    app.debug = True
    app.run()
