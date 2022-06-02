from website import create_app

app = create_app()
if __name__ == '__main__':
    # automatically changes the site when changes are made here
    app.run(debug=True)


