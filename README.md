# Image Repository
The Shopify challenge for Backend Developer Intern (Remote) - Winter 2022 application.

## Install Dependencies
This app requires Go 1.15, in order to install dependencies, run `go mod download` in the `/backend` directory.

## How to Run
To deploy the backend, run `go run main.go` in the `/backend` directory.

To try out the following features, look at the `demo.py` to see examples of API queries that can be made and edit it as you wish. (The backend must be running before running `demo.py`).
Note that this `demo.py` script interacts with the `/database` directory, which has the preloaded database (with users and images) to faciliate an easier demo process. 

## Features
- user account sign-up/sign-in (with authentication)
- JWT authorization
- access control
- upload one or multiple images (with description, location, privacy flag etc.)
- delete images
- search for images from text (description and location)
- search for images by classes (AI-generated image tags)
- image visibility (public or private to other users)

## The tech stack
Go, Gin (HTTP framework), SQLite, GORM. 

## Areas for Improvement
- The SQLite database is convenient for a demo but for a scalable database with better concurrency control, a MySQL or PostgreSQL database could be used. The images can also be stored remotely in a NoSQL database.
- The Imagga API (Image recognition/tagger) key and secret are stored in `backend/.env` to make this repository self contained, however they should be kept a secret.
