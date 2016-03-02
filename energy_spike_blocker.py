# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = {
        u"stromforbruk_i_prosent": 40,
        u"stromforbruk_i_kw": 123,
        u"status" : [
            u"av",
            u"på",
            u"auto"
        ],
        u"slaes_av_ved":[
            50,60,70,80,90,100
        ],
        u"apparater": [
            {
                u"id":1,
                u"navn": "Test",
                u"slaes_av_ved" : 70,
                u"status": "auto"
            },
            {
                u"id":2,
                u"navn": "Test 2",
                u"slaes_av_ved" : 50,
                u"status": "av"
            },
            {
                u"id":3,
                u"navn": "Test",
                u"slaes_av_ved" : 80,
                u"status": "på"
            }
        ]
    }

    if request.method == 'POST':
        pass
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.debug = True
    app.run()
