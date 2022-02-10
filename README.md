# player
This project. reads the contents of the file named "People.csv" and serves the content of the file on the postgresql database and also exposes the contents through
the CRUD operations viz:
    1. GET Request 
    2. PUT Request 
      GET /api/players` - returns the list of all players
      GET /api/players/{playerID}` - returns a single player by it's ID
      PUT /api/players/{playerID}/weight
      PUT /api/players/{playerID}/height
