import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import base64
@app.route('/fit')
def fit():
    google_fit_data = []
    view = request.args.get('view', 'weekly')  # Default to weekly
    
    if 'google_credentials' in session:
        credentials = Credentials(**session['google_credentials'])
        service = build('fitness', 'v1', credentials=credentials)
        try:
            now = datetime.datetime.utcnow()

            if view == 'weekly':
                start_time = now - datetime.timedelta(days=7)
            elif view == 'monthly':
                start_time = now - datetime.timedelta(days=30)
            else:  # yearly
                start_time = now - datetime.timedelta(days=365)

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
                        date = datetime.datetime.fromtimestamp(int(bucket['startTimeMillis']) / 1000).strftime('%Y-%m-%d')
                        labels.append(date)
                        values.append(value['intVal'])

    return render_template('fit.html', labels=labels, values=values, view=view)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
