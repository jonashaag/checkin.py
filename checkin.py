from __future__ import division
import os
import json
from datetime import datetime, date

from bottle import route, view, request

from config import HOURS_PER_DAY


DATETIME_FMT = '%Y-%m-%d %H:%M:%S'
DATETIME_KEYS = ['checkin', 'checkout']


def get_day_of_year():
    return (date.today() - date(date.today().year, 1, 1)).days


def load_db():
    def decode_datetime(attendance):
        for key in DATETIME_KEYS:
            if key in attendance:
                attendance[key] = datetime.strptime(attendance[key], DATETIME_FMT)
        return attendance

    if os.path.exists('db.json'):
        return map(decode_datetime, json.load(open('db.json')))
    else:
        return []


def save_db(data):
    def encode_datetime(attendance):
        for key in DATETIME_KEYS:
            if key in attendance:
                attendance = dict(attendance, **{key: attendance[key].strftime(DATETIME_FMT)})
        return attendance

    json.dump(
        map(encode_datetime, data),
        open('db.json', 'w'),
        indent=2
    )


@route('/', ['GET', 'POST'])
@view('index')
def index():
    db = load_db()
    checked_out_after = None
    checked_out = not db or 'checkout' in db[0]

    if request.method == 'POST':
        if checked_out:
            # Check in
            db.insert(0, {'checkin': datetime.now()})
        else:
            # Check out
            db[0]['checkout'] = datetime.now()
            checked_out_after = (db[0]['checkout'] - db[0]['checkin']).total_seconds() / 60 / 60

        checked_out = not checked_out
        save_db(db)

    if checked_out:
        current_checkin = None
        past_attendances = db
    else:
        current_checkin = db[0]
        past_attendances = db[1:]

    for attendance in past_attendances:
        attendance['delta'] = attendance['checkout'] - attendance['checkin']

    THIS_YEAR = date.today().year
    hours_worked_this_year = sum(attendance['delta'].total_seconds() / 60 / 60
                                 for attendance in past_attendances
                                 if attendance['checkin'].year == THIS_YEAR)

    return {'current_checkin': current_checkin,
            'past_attendances': past_attendances,
            'checked_out_after': checked_out_after,
            'should_have_worked': get_day_of_year() * HOURS_PER_DAY,
            'have_worked': hours_worked_this_year}
