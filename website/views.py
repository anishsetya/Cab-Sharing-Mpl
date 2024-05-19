from flask import Blueprint, render_template, request,flash
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import User,Request
views= Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        flight_time=request.form.get('flight_time')
        date=request.form.get('date')
        vacancy= request.form.get('vacancy')

        print("data:",flight_time,date,vacancy)
        
        if(flight_time==''):
            flash('Enter Valid Time', category='error')
        elif(date==''):
            flash('Enter Valid Date', category='error')
        elif(vacancy==''):
            flash('Enter Valid Occupancy', category='error')
        else:
            
            flight_time_obj = datetime.strptime(flight_time, '%H:%M').time() 
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            new_request=Request(userid=current_user.id,flight_time=flight_time_obj,date=date_obj,vacancy=vacancy)
            db.session.add(new_request)
            db.session.commit()
            flash('Cab Request Sent', category='success')
    return render_template("home.html")