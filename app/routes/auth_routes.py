
from flask import Blueprint, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from config import Config 

# Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Initialize OAuth
oauth = OAuth()

# Register Auth0 with OAuth
auth0 = oauth.register(
    'auth0',
    client_id=Config.AUTH0_CLIENT_ID,
    client_secret=Config.AUTH0_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid profile email',  # Scopes for OpenID Connect
    },
    server_metadata_url=f'https://{Config.AUTH0_DOMAIN}/.well-known/openid-configuration',
)

@auth_bp.route('/login')
def login():
    """
    Redirects the user to the Auth0 login page.
    """
    # Redirect to Auth0 login with the specified redirect URI
    return auth0.authorize_redirect(redirect_uri=Config.AUTH0_CALLBACK_URL)

@auth_bp.route('/callback')
def callback():
    """
    Handles the callback from Auth0 after authentication.
    """
    try:
        # Get the token and user info from Auth0
        token = auth0.authorize_access_token()
        user_info = auth0.parse_id_token(token)

        # Store user information in the session
        session['user'] = user_info

        # Redirect to the dashboard or desired page
        return redirect(url_for('main.dashboard'))

    except Exception as e:
        # Handle errors in the authentication flow
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/logout')
def logout():
    """
    Logs out the user and clears the session.
    Redirects to the Auth0 logout page.
    """
    session.clear()  # Clear the session
    # Redirect to Auth0 logout page with a returnTo URL
    return redirect(
        f'https://{Config.AUTH0_DOMAIN}/v2/logout?returnTo={Config.BASE_URL}'  # Use dynamic URL if needed
    )














