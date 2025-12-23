from datetime import datetime
import json
from flask import Flask, render_template, request, redirect, flash, url_for

##########################################
#             Flask app                  #
##########################################
app = Flask(__name__)
app.secret_key = 'something_special'


##########################################
#             Data & utils               #
##########################################
def loadClubs():
    """Load clubs from json file"""
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def save_clubs(clubs):
    """Save clubs to json file"""
    with open('clubs.json', 'w') as c:
        json.dump({'clubs': clubs}, c, indent=4)


def find_club(value: str):
    """Find club by value club"""
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
        json.dump({'competitions': competitions}, c, indent=4)


def find_competition(value: str):
    """Find competition by value competition"""
    for competition in competitions:
        if value in competition.values():
            return competition
    return None


competitions = load_competitions()
clubs = loadClubs()


##########################################
#                Route                   #
##########################################
@app.route('/')
def index():
    """View homepage"""
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    """View summary page"""
    email = request.form['email']
    matching_club = find_club(email)

    if not matching_club:
        flash('Aucun compte lié à cette adresse mail')
        return redirect(url_for('index'))

    flash(f'Vous êtes connecté au club {matching_club["name"]}')
    return render_template('welcome.html', club=matching_club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    """View book page"""
    name_club = club
    foundClub = find_club(name_club)
    name_competition = competition
    foundCompetition = find_competition(name_competition)

    date_now = datetime.now()
    date_competition = datetime.strptime(foundCompetition["date"], "%Y-%m-%d %H:%M:%S")
    if date_competition < date_now:
        flash("Impossible de réserver des places pour une compétition passée")
        return render_template('welcome.html', club=foundClub, competitions=competitions)

    if not foundClub and not foundCompetition:
        return render_template('welcome.html', club=club, competitions=competitions)

    flash("Something went wrong-please try again")
    return render_template('booking.html', club=foundClub, competition=foundCompetition)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    """View purchase places page"""
    name_competition = request.form['competition']
    matching_competition = find_competition(name_competition)
    name_club = request.form['club']
    matching_club = find_club(name_club)

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

    matching_competition['numberOfPlaces'] = str(int(matching_competition['numberOfPlaces']) - placesRequired)
    matching_club['points'] = str(int(matching_club['points']) - placesRequired)

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
