
---
# gudlift-registration
![logo GudLift](https://user.oc-static.com/upload/2020/09/22/16007798203635_P9.png)

[[FR]](#français) - [[EN]](#english)
---
## Français

1. **Pourquoi**


Il s'agit d'un projet de validation de concept (POC) visant à présenter une version allégée de notre plateforme de réservation de compétitions. L'objectif est de rester aussi léger que possible et d'utiliser les commentaires des utilisateurs pour itérer.

2. **Pour commencer**

Ce projet utilise les technologies suivantes :

* Python v3.x+

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

    Alors que Django fait beaucoup de choses pour nous dès le départ, 
  Flask nous permet d'ajouter uniquement ce dont nous avons besoin.
* [Environnement virtuel](https://virtualenv.pypa.io/en/stable/installation.html)

Cela vous permet d'installer les bons paquets sans interférer avec Python sur votre machine.
Avant de commencer, assurez-vous que cela est installé globalement. 


3. **Installation**
    - lien du repo github pour clonage: ```https://github.com/C-eorl/P11-GudLift.git```
    - Après le clonage, passez dans le répertoire ```cd P11-GudLift``` et tapez <code>python -m venv .venv</code>. Cela permettra de configurer un environnement Python virtuel dans ce répertoire.

    - Ensuite, tapez <code>source .venv/bin/activate</code>. Vous devriez voir que votre invite de commande a changé pour le nom du dossier. Cela signifie que vous pouvez installer des paquets ici sans affecter les fichiers extérieurs. Pour désactiver, tapez <code>deactivate</code>

    - Plutôt que de rechercher les paquets dont vous avez besoin, vous pouvez les installer en une seule étape. Tapez <code>pip install -r requirements.txt</code>. Cela installera tous les paquets répertoriés dans le fichier correspondant. Si vous installez un paquet, assurez-vous d'en informer les autres en mettant à jour le fichier


4. **Mise en route serveur**
    
    Démarrer le serveur : 
   ```bash
   export FLASK_APP=server.py 
   flask run
   ```
   
    Acceder au serveur a l'aide ce cette adresse : http://127.0.0.1:5000


5. **Configuration actuelle**

L'application fonctionne à l'aide de fichiers JSON. Cela permet d'éviter d'avoir recours à une base de données tant que nous n'en avons pas réellement besoin. Les principaux fichiers sont les suivants :

- competitions.json - liste des compétitions
- clubs.json - liste des clubs avec les informations pertinentes. 

Vous pouvez consulter cette liste pour voir quelles adresses e-mail l'application accepte pour la connexion.

7. **Tests**

Vous êtes libre d'utiliser le cadre de test de votre choix, l'essentiel étant que vous puissiez montrer les tests que vous utilisez.

Nous aimons également montrer l'efficacité de nos tests, c'est pourquoi nous vous recommandons d'ajouter à votre projet un module appelé « coverage ».


    
---

---
## English

1. **Why**

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.


2. **Getting Started**

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     
   * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.
Before you begin, please ensure you have this installed globally. 


3. **Installation**
    - GitHub repo link for cloning: ```https://github.com/C-eorl/P11-GudLift.git```
    - After cloning, change into the directory ```cd P11-GudLift``` and type <code>python -m venv .venv</code>. This will then set up a a virtual python environment within that directory.

    - Next, type <code>source .venv/bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.


4. **Mise en route serveur**
    
    Démarrer le serveur : 
   ```bash
   export FLASK_APP=server.py 
   flask run
   ```
   
    Acceder au serveur a l'aide ce cette adresse : http://127.0.0.1:5000



5. **Current Setup**

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.


6. **Testing**

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

---
_Projet réalisé dans le contexte de la formation Developpeur Python - OpenClassRoom_