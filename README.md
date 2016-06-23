jwttut
======

GET request to http://0.0.0.0:3001/secured/ping

with header (via postman):

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJlZCJ9.ELVoRHbVTv77CM7ShylFmlfbK4maI3N6P9wqhOFBcaM

local install
-------------

With conda:

    conda install flask flask-cors
    pip install pyjwt dotenv

Just pip:

    pip install -r requirements.txt


docker
------

Build:

    docker build -t username/jwttut:latest .

Run:

    docker run -p 3001:3001 --env-file .env username/jwttut





