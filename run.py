# from app.create_app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)



from app.create_app import create_app

app = create_app()

if __name__ == "__main__":
    # Do not use app.run() in serverless environments
    pass



