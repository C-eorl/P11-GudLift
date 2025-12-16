from locust import HttpUser, task, between
import random


class ClubSecretaryUser(HttpUser):
    """Simulates secretary behavior using app"""

    wait_time = between(1, 3)

    def on_start(self):
        self.client.get("/purchasePlaces")

        self.emails = [
            'john@simplylift.co',
            'admin@irontemple.com',
            'kate@shelifts.co.uk'
        ]
        self.email = random.choice(self.emails)
        self.client.post('/showSummary', data={'email': self.email})

    @task(3)
    def view_competitions(self):

        with self.client.get('/showSummary',
                             data={'email': self.email},
                             catch_response=True) as response:
            if response.elapsed.total_seconds() > 5:
                response.failure(f"Page took {response.elapsed.total_seconds()}s to load (max: 5s)")
            else:
                response.success()

    @task(2)
    def view_booking_page(self):

        competitions = ['Spring Festival', 'Fall Classic']
        clubs = ['Simply Lift', 'Iron Temple', 'She Lifts']

        import random
        comp = random.choice(competitions)
        club = random.choice(clubs)

        self.client.get(f'/book/{comp}/{club}')

    @task(1)
    def purchase_places(self):

        import random

        clubs = ['Simply Lift', 'Iron Temple', 'She Lifts']
        competitions = ['Spring Festival', 'Fall Classic']

        # Réserver entre 1 et 5 places
        places = random.randint(1, 5)

        with self.client.post('/purchasePlaces',
                              data={
                                  'club': random.choice(clubs),
                                  'competition': random.choice(competitions),
                                  'places': str(places)
                              },
                              catch_response=True) as response:

            # Vérifier le temps de réponse
            if response.elapsed.total_seconds() > 2:
                response.failure(f"Update took {response.elapsed.total_seconds()}s (max: 2s)")
            else:
                response.success()

    @task(1)
    def view_points_board(self):

        self.client.get('/points')

    @task(1)
    def logout(self):

        self.client.get('/logout')


class PublicUser(HttpUser):
    """
    Simule public user
    """

    wait_time = between(2, 5)

    @task
    def view_public_points(self):

        self.client.get('/points')
