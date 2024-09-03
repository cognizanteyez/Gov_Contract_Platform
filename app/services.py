import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_mail import Message
from app import mail, db
from datetime import datetime
from app.models import Notification

def search_contracts(query):
    # Placeholder function to search federal, state, and county procurement data
    # Integrate actual data sources here and preprocess data
    sample_data = [
        {
            'title': 'Contract 1',
            'description': 'Description of contract 1',
            'agency': 'Agency 1',
            'state': 'State 1',
            'county': 'County 1',
            'posted_date': datetime.strptime('2024-01-01', '%Y-%m-%d'),
            'due_date': datetime.strptime('2024-02-01', '%Y-%m-%d')
        },
        {
            'title': 'Contract 2',
            'description': 'Description of contract 2',
            'agency': 'Agency 2',
            'state': 'State 2',
            'county': 'County 2',
            'posted_date': datetime.strptime('2024-01-15', '%Y-%m-%d'),
            'due_date': datetime.strptime('2024-02-15', '%Y-%m-%d')
        }
    ]

    # Implement AI-driven search
    documents = [contract['description'] for contract in sample_data]
    documents.insert(0, query)
    
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    
    results = []
    for i, score in enumerate(cosine_sim):
        if score > 0.1:  # Adjust threshold as needed
            sample_data[i]['score'] = score
            results.append(sample_data[i])
    
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results

def send_notification(user, message):
    notification = Notification(user_id=user.id, message=message)
    db.session.add(notification)
    db.session.commit()

    msg = Message('Notification', sender='noreply@demo.com', recipients=[user.email])
    msg.body = message
    mail.send(msg)
