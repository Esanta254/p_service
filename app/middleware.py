

# from functools import wraps
# from flask import request, jsonify, session
# from jose import jwt  # For decoding JWTs
# from config import Config  # Assuming Config contains Auth0 domain and audience
# from urllib.request import urlopen
# import json
# import os  # To check for test environment


# def get_jwks():
#     """
#     Fetch the JSON Web Key Set (JWKS) from the OpenID Connect provider.
#     """
#     try:
#         jwks_url = f"https://{Config.AUTH0_DOMAIN}/.well-known/jwks.json"
#         response = urlopen(jwks_url)
#         return json.loads(response.read())
#     except Exception as e:
#         raise RuntimeError(f"Failed to fetch JWKS: {e}")


# def get_public_key(jwks, kid):
#     """
#     Retrieve the public key from JWKS using the Key ID (kid).
#     """
#     for key in jwks['keys']:
#         if key['kid'] == kid:
#             return {
#                 "kty": key["kty"],
#                 "kid": key["kid"],
#                 "use": key["use"],
#                 "n": key["n"],
#                 "e": key["e"],
#             }
#     raise ValueError("Public key not found for the provided Key ID (kid).")


# def login_required(func):
#     """
#     Decorator to validate the JWT and ensure the user is authenticated.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Check for test environment
#         if os.getenv('FLASK_ENV') == 'testing':
#             # Mock token validation for tests
#             auth_header = request.headers.get('Authorization', None)
#             if auth_header == "Bearer mocked_valid_token":
#                 session['user'] = {"sub": "testuser", "roles": ["admin"]}
#                 return func(*args, user=session['user'], **kwargs)
#             return jsonify({"error": "Unauthorized in test environment."}), 401

#         # Get Authorization header
#         auth_header = request.headers.get('Authorization', None)
#         if not auth_header:
#             return jsonify({"error": "Authorization header is missing."}), 401

#         # Ensure Bearer token format
#         parts = auth_header.split()
#         if parts[0].lower() != 'bearer' or len(parts) != 2:
#             return jsonify({"error": "Invalid Authorization header format. Expected 'Bearer <token>'."}), 401

#         token = parts[1]
#         try:
#             # Fetch JWKS and decode the token
#             jwks = get_jwks()
#             unverified_header = jwt.get_unverified_header(token)

#             # Ensure the Key ID (kid) exists
#             if 'kid' not in unverified_header:
#                 return jsonify({"error": "Invalid token header. Missing 'kid'."}), 401

#             rsa_key = get_public_key(jwks, unverified_header['kid'])

#             # Decode the JWT
#             payload = jwt.decode(
#                 token,
#                 rsa_key,
#                 algorithms=["RS256"],
#                 audience=Config.AUTH0_AUDIENCE,
#                 issuer=f"https://{Config.AUTH0_DOMAIN}/"
#             )

#             # Store user info in session
#             session['user'] = payload

#             # Pass the decoded payload to the endpoint
#             return func(*args, user=payload, **kwargs)

#         except jwt.ExpiredSignatureError:
#             return jsonify({"error": "Token has expired."}), 401
#         except jwt.JWTClaimsError:
#             return jsonify({"error": "Incorrect claims. Please check the audience and issuer."}), 401
#         except Exception as e:
#             return jsonify({"error": f"Unable to parse authentication token: {str(e)}"}), 401

#     return wrapper














#Bypassing authentication

# import os
# from functools import wraps
# from flask import request, jsonify, session
# from jose import jwt  # For decoding JWTs
# from config import Config  # Assuming Config contains Auth0 domain and audience
# from urllib.request import urlopen
# import json
# from app.middleware import jwt


# def login_required(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Skip authentication in testing
#         if os.getenv('FLASK_ENV') == 'testing':
#             return func(*args, user={"sub": "test_user"}, **kwargs)

#         # Normal authentication process
#         auth_header = request.headers.get('Authorization', None)
#         if not auth_header:
#             return jsonify({"error": "Authorization header is missing."}), 401

#         parts = auth_header.split()
#         if parts[0].lower() != 'bearer' or len(parts) != 2:
#             return jsonify({"error": "Invalid Authorization header format. Expected 'Bearer <token>'."}), 401

#         token = parts[1]
#         try:
#             # Fetch JWKS and decode the token
#             jwks = get_jwks()
#             unverified_header = jwt.get_unverified_header(token)

#             if 'kid' not in unverified_header:
#                 return jsonify({"error": "Invalid token header. Missing 'kid'."}), 401

#             rsa_key = get_public_key(jwks, unverified_header['kid'])

#             payload = jwt.decode(
#                 token,
#                 rsa_key,
#                 algorithms=["RS256"],
#                 audience=Config.AUTH0_AUDIENCE,
#                 issuer=f"https://{Config.AUTH0_DOMAIN}/"
#             )

#             return func(*args, user=payload, **kwargs)

#         except jwt.ExpiredSignatureError:
#             return jsonify({"error": "Token has expired."}), 401
#         except jwt.JWTClaimsError:
#             return jsonify({"error": "Incorrect claims. Check the audience and issuer."}), 401
#         except Exception as e:
#             return jsonify({"error": f"Unable to parse token: {str(e)}"}), 401

#     return wrapper












import os
from functools import wraps
from flask import request, jsonify
from jose import jwt  # For decoding JWTs
from urllib.request import urlopen
import json
from config import Config  # Ensure this contains Auth0 domain and audience


def get_jwks():
    """
    Fetch the JSON Web Key Set (JWKS) from the Auth0 domain.
    """
    jwks_url = f"https://{Config.AUTH0_DOMAIN}/.well-known/jwks.json"
    try:
        with urlopen(jwks_url) as response:
            return json.load(response)
    except Exception as e:
        raise RuntimeError(f"Unable to fetch JWKS: {str(e)}")


def get_public_key(jwks, kid):
    """
    Retrieve the public key from JWKS using the 'kid' in the token header.
    """
    for key in jwks['keys']:
        if key['kid'] == kid:
            return {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    raise ValueError("Public key not found in JWKS for the given 'kid'")


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Skip authentication in testing
        if os.getenv('FLASK_ENV') == 'testing':
            return func(*args, user={"sub": "test_user"}, **kwargs)

        # Normal authentication process
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"error": "Authorization header is missing."}), 401

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return jsonify({"error": "Invalid Authorization header format. Expected 'Bearer <token>'."}), 401

        token = parts[1]
        try:
            # Fetch JWKS and decode the token
            jwks = get_jwks()
            unverified_header = jwt.get_unverified_header(token)

            if 'kid' not in unverified_header:
                return jsonify({"error": "Invalid token header. Missing 'kid'."}), 401

            rsa_key = get_public_key(jwks, unverified_header['kid'])

            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                audience=Config.AUTH0_AUDIENCE,
                issuer=f"https://{Config.AUTH0_DOMAIN}/"
            )

            # Pass the decoded payload (user info) to the wrapped function
            return func(*args, user=payload, **kwargs)

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired."}), 401
        except jwt.JWTClaimsError:
            return jsonify({"error": "Incorrect claims. Check the audience and issuer."}), 401
        except ValueError as e:
            return jsonify({"error": str(e)}), 401
        except Exception as e:
            return jsonify({"error": f"Unable to parse token: {str(e)}"}), 401

    return wrapper
