# from flask import Blueprint, render_template, request, jsonify, current_app
# from flask_login import login_required
# import requests

# main_bp = Blueprint('main', __name__)

# @main_bp.route('/')
# def index():
#     return render_template('index.html')

# @main_bp.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

# @main_bp.route('/contracts')
# @login_required
# def contracts():
#     return render_template('contracts.html')

# @main_bp.route('/ai-insights')
# @login_required
# def ai_insights():
#     ai_insights_data = get_ai_insights()
#     return render_template('ai_insights.html', insights=ai_insights_data)

# @main_bp.route('/market-analysis')
# @login_required
# def market_analysis():
#     market_analysis_data = perform_market_analysis()
#     return render_template('market_analysis.html', analysis=market_analysis_data)

# @main_bp.route('/api/search', methods=['GET'])
# def api_search():
#     api_key = current_app.config['SAM_API_KEY']
#     posted_from = request.args.get('postedFrom')
#     posted_to = request.args.get('postedTo')
#     limit = request.args.get('limit')
#     offset = request.args.get('offset')

#     url = f'https://api.sam.gov/opportunities/v2/search?api_key={api_key}&postedFrom={posted_from}&postedTo={posted_to}&limit={limit}&offset={offset}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         search_results = response.json().get('opportunitiesData', [])
#     else:
#         search_results = [{"error": f"Failed to fetch data from API. Status code: {response.status_code}. {response.text}"}]
    
#     return jsonify(search_results)

# def get_ai_insights():
#     return {"trend": "Government contracts are increasing in technology sector."}

# def perform_market_analysis():
#     return {"analysis": "The market is trending towards sustainable energy projects."}


###########
from flask import Blueprint, render_template, request, jsonify, current_app
from flask_login import login_required
import requests

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/contracts')
@login_required
def contracts():
    return render_template('contracts.html')

@main_bp.route('/api/search', methods=['GET'])
def api_search():
    api_key = current_app.config['SAM_API_KEY']
    posted_from = request.args.get('postedFrom')
    posted_to = request.args.get('postedTo')
    state = request.args.get('state')
    zip = request.args.get('zip')

    url = f'https://api.sam.gov/opportunities/v2/search?api_key={api_key}&postedFrom={posted_from}&postedTo={posted_to}&state={state}&zip={zip}'
    response = requests.get(url)

    if response.status_code == 200:
        search_results = response.json().get('opportunitiesData', [])
    else:
        search_results = [{"error": f"Failed to fetch data from API. Status code: {response.status_code}. {response.text}"}]
    print("\n \n \n Search_Results:", search_results)
    return jsonify(search_results)
# api_search()
