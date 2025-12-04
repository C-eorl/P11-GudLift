import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def show_summary():
    email = request.form['email']
    matching_clubs = [club for club in clubs if club['email'] == email]

    if not matching_clubs:
        flash('Aucun compte lié à cette adresse mail')
        return redirect(url_for('index'))

    club = matching_clubs[0]
    flash(f'Vous êtes connecté au club {club["name"]}')
    return render_template('welcome.html',club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchase_places():

    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]

    places_raw = request.form['places']

    try:
        placesRequired = int(places_raw)
    except ValueError:
        flash('Veuillez rentrer un nombre')
        return redirect(url_for('purchase_places'))

    if placesRequired <= 0:
        flash('Veuillez rentrer un nombre de place positif')
        return redirect(url_for('purchase_places'))
    if placesRequired > 12:
        flash('Vous ne pouvez pas réserver plus de 12 places')
        return redirect(url_for('purchase_places'))

    if placesRequired > int(club['points']):
        flash("Vous n'avez pas assez de points")
        return redirect(url_for('purchase_places'))

    if placesRequired > int(competition['numberOfPlaces']):
        flash("Il n'a pas assez de place")
        return redirect(url_for('purchase_places'))

    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))