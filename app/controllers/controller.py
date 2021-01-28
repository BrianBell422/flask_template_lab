from flask import render_template, request, redirect
from app import app
from app.models.event_list import events
from app.models.event import *


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)


@app.route('/events', methods=['POST'])
def add_event():
    event_date = (request.form["date"])
    event_name_of_event = (request.form["name_of_event"])
    event_guests = (request.form["number_of_guests"])
    event_location = (request.form["room_location"])
    event_description = (request.form["description"])
    new_event = Event(event_date, event_name_of_event, event_guests, event_location, event_description, False)
    events.append(new_event)
    return redirect('/events')
    
    