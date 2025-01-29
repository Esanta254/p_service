# import os

# class Config:
#     SECRET_KEY = '00f95b7a114e80079d437e374854e9a317fb97f30dafb3e12d071307a2937707'
#     SESSION_TYPE = 'filesystem'
#     AUTH0_CLIENT_ID = 'wKvwHXE4gB1GfurhG7YWqlqhRTHGEd68'
#     AUTH0_CLIENT_SECRET = 'GVByiZyIuekYvRqTAcy4wPQUyH_6mhLdNzV1q1rV2lDVbCGGtHUSfXAYKaBHT3pJ'
#     AUTH0_DOMAIN = 'dev-26blcm0q4r8fjapq.us.auth0.com'
#     AUTH0_BASE_URL = f'https://{AUTH0_DOMAIN}'
#     AUTH0_CALLBACK_URL = 'http://localhost:5000/callback'
#     AUTH0_AUDIENCE = f'https://{AUTH0_DOMAIN}/userinfo'















import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '00f95b7a114e80079d437e374854e9a317fb97f30dafb3e12d071307a2937707')  
    AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID', 'wKvwHXE4gB1GfurhG7YWqlqhRTHGEd68')
    AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET', 'GVByiZyIuekYvRqTAcy4wPQUyH_6mhLdNzV1q1rV2lDVbCGGtHUSfXAYKaBHT3pJ')
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', 'dev-26blcm0q4r8fjapq.us.auth0.com')
    AUTH0_BASE_URL = f'https://{AUTH0_DOMAIN}'
    AUTH0_CALLBACK_URL = os.getenv('AUTH0_CALLBACK_URL', 'http://localhost:5000/callback')
    AUTH0_AUDIENCE = os.getenv('AUTH0_AUDIENCE', 'http://127.0.0.1:5000/customers')
