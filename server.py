import json
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    """Load clubs from json file"""
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def save_clubs(clubs):
    """Save clubs to json file"""
    with open('clubs.json', 'w') as c:
        json.dump({'clubs' : clubs}, c, indent=4)

def find_club(value: str):
    """Find club by name"""
    for club in clubs:
        if value in club.values():
            return club
    return None

def load_competitions():
    """Load competitions from json file"""
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

def save_competitions(competitions):
    """Save competitions to json file"""
    with open('competitions.json', 'w') as c:
        json.dump({'competitions' : competitions}, c, indent=4)

def find_competition(value: str):
    """Find competition by name"""
    for competition in competitions:
        if value in competition.values():
            return competition
    return None

app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = loadClubs()

@app.route('/')
def index():
    """View homepage"""
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def show_summary():
    """View summary page"""
    email = request.form['email']
    matching_club = find_club(email)

    if not matching_club:
        flash('Aucun compte lié à cette adresse mail')
        return redirect(url_for('index'))

    flash(f'Vous êtes connecté au club {matching_club["name"]}')
    return render_template('welcome.html',club=matching_club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """View book page"""
    foundClub = find_club(club)
    foundCompetition = find_competition(competition)

    if not foundClub and not foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)

    flash("Something went wrong-please try again")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchase_places():
    """View purchase places page"""
    matching_competition = find_competition(request.form['competition'])
    matching_club = find_club(request.form['club'])

    places_raw = request.form['places']
    # validation
    try:
        placesRequired = int(places_raw)
    except ValueError:
        flash('Veuillez rentrer un nombre')
        return render_template('welcome.html', club=matching_club, competitions=competitions)

    if placesRequired <= 0:
        flash('Veuillez rentrer un nombre de place positif')
        return render_template('welcome.html', club=matching_club, competitions=competitions)
    if placesRequired > 12:
        flash('Vous ne pouvez pas réserver plus de 12 places')
        return render_template('welcome.html', club=matching_club, competitions=competitions)

    if placesRequired > int(matching_club['points']):
        flash("Vous n'avez pas assez de points")
        return render_template('welcome.html', club=matching_club, competitions=competitions)

    if placesRequired > int(matching_competition['numberOfPlaces']):
        flash("Il n'a pas assez de place")
        return render_template('welcome.html', club=matching_club, competitions=competitions)

    matching_competition['numberOfPlaces'] = str(int(matching_competition['numberOfPlaces'])-placesRequired)
    matching_club['points'] = str(int(matching_club['points'])-placesRequired)

    save_competitions(competitions)
    save_clubs(clubs)

    flash('Réservation réussie')
    return render_template('welcome.html', club=matching_club, competitions=competitions)

@app.route('/points')
def display_points():
    """View points page"""
    return render_template('points.html', clubs=clubs)

@app.route('/logout')
def logout():
    """View logout page"""
    return redirect(url_for('index'))