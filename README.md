# FLASK

j'ai voulu tester rapidement. j'ai donc fait 5 pages web.
- Une page d'accueil avec un lien vers une autre page
- Une page avec un formulaire qui demande un prénom et un nom
- une page qui affiche le prénom et le nom
- Une page qui affiche qu'un texte
- Une page qui affiche un json


Rien d'extraordinaire mais c'est juste pour tester. Il n'y a pas vraiment de css.
j'ai mis un fichier style.css pour tester l'import d'un fichier static

pour lancer le projet:
```bash
python -m venv .venv
pip install -r requirements.txt
flask --app app run --port 5050
```