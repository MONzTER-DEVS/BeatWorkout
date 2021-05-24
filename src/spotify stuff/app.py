from flask import Flask,request,url_for,redirect,session
import spotipy
from spotipy.oauth2 import SpotifyOAuth


app = Flask(__name__)
app.secret_key = "mad_is_mad"
app.config['SESSION_COOKIE_NAME'] = 'vatz cookie'

@app.route('/')
def Login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    return 'redirect'
@app.route('/getTracks')
def getTracks():
    return "Songs"
Client_ID = '2ad24126d2254863ba426d3e6b0bf330'
Client_Secret = 'adca97f9a0114077a0e4e6a343b29e'
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id= Client_ID,
        client_secret=Client_Secret,
        redirect_uri=url_for('redirectPage',_external=True),
        scope = "user-library-read"
    )


