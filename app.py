import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Google Fit Configuration
GOOGLE_FIT_SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']
GOOGLE_CLIENT_SECRETS_FILE = "credentials.json"

GOOGLE_FLOW = Flow.from_client_secrets_file(
    GOOGLE_CLIENT_SECRETS_FILE,
    scopes=GOOGLE_FIT_SCOPES,
    redirect_uri='http://localhost:8000/callback'
)

# Route: Authorize Google OAuth
@app.route('/authorize/google')
def authorize_google():
    auth_url, _ = GOOGLE_FLOW.authorization_url(prompt='consent')
    return redirect(auth_url)

# Route: Google OAuth Callback
@app.route('/callback')
def callback_google():
    try:
        GOOGLE_FLOW.fetch_token(authorization_response=request.url)
        credentials = GOOGLE_FLOW.credentials
        session['google_credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
    except Exception as e:
        return f"Error during Google OAuth callback: {e}"
    return redirect(url_for('index'))

@app.route('/index')
def index():
    return redirect(url_for('fit', view='weekly'))

@app.route('/fit')
def fit():
    google_fit_data = []
    view = request.args.get('view', 'weekly')  # Default to weekly
    
    if 'google_credentials' in session:
        credentials = Credentials(**session['google_credentials'])
        service = build('fitness', 'v1', credentials=credentials)
        try:
            now = datetime.utcnow()

            if view == 'weekly':
                start_time = now - timedelta(days=7)
            elif view == 'monthly':
                start_time = now - timedelta(days=30)
            else:  # yearly
                start_time = now - timedelta(days=365)

            dataset = service.users().dataset().aggregate(
                userId="me",
                body={
                    "aggregateBy": [{"dataTypeName": "com.google.step_count.delta"}],
                    "bucketByTime": {"durationMillis": 86400000},  # Daily buckets
                    "startTimeMillis": int(start_time.timestamp() * 1000),
                    "endTimeMillis": int(now.timestamp() * 1000),
                }
            ).execute()
            
            google_fit_data = dataset.get('bucket', [])
        except Exception as e:
            print(f"Error fetching Google Fit data: {e}")

    # Convert data to a format suitable for Chart.js
    labels = []
    values = []
    for bucket in google_fit_data:
        for dataset in bucket.get('dataset', []):
            for point in dataset.get('point', []):
                for value in point.get('value', []):
                    if 'intVal' in value:
                        date = datetime.fromtimestamp(int(bucket['startTimeMillis']) / 1000).strftime('%Y-%m-%d')
                        labels.append(date)
                        values.append(value['intVal'])

    return render_template('fit.html', labels=labels, values=values, view=view)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
