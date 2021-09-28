import requests

def endpoint(path):
    return f'http://localhost:8000{path}'

# POST request to /login with a username, password body. Returns the JSON Web token (JWT) upon successful login.
def login(user, password):
    r = requests.post(endpoint('/login'), json={'username': user, 'password': password})
    return r.json()['user']['authToken']

# POST request to (fuzzy) search images.
# If the 'search' param is just one word, it searches images which have that word in their description OR location OR AI-generated tags. 
# If the 'search' param is a comma-seperated list of words, it searches for images with at least one tag matching one of the words in the list.
# Can include/exclude public images (other users' images), and also needs the JWT as header to process the request.
# Returns a list of image metadata, e.g:
# [ {'ID': 1, 'CreatedAt': '2021-01-17T21:11:47.1045165-05:00', 'UpdatedAt': '2021-01-17T21:11:48.1832869-05:00', 'UserID': 1, 
# 'Name': 'hagia-sophia.jpg', 'Format': 'image/jpeg', 'FileStore': '8ltujhz7SrXUK5PP6yCgdW0vkTBFsk5x.jpg', 'Description': '', 
# 'Geolocation': '', 'MLTags': 'mosque,place of worship,building,structure,minaret,architecture,dome,religion,travel,landmark', 'Private': True}, ....]
def query_metadata(search, include_public, auth):
    body = {
        'query': search,
        'includePublic': include_public,
    }
    headers = {
        'Authorization': auth,
    }
    r = requests.post(endpoint('/images'), json=body, headers=headers)
    return r.json()['images']

# GET request to write image file (by id) to the specified destination path.
# Image IDs are retrieved from the 'query_metadata' function above.
def get_image(id, destination, auth):
    url = endpoint(f'/image/{id}')
    r = requests.get(url, headers={'Authorization': auth})
    with open(destination, 'wb') as f:
        f.write(r.content)
    return True


# Login as admin. (Password is actually salted and hashed before its persisted to the db, but for demo purposes its visible here.
# On a webapp, the characters would not be shown as they are typed).
token = login('admin', 'password')

# Print auto-generated JWT token
print(f'Auth token: {token}')

# Get images with the word "building" in their description/location/AI-generated tags.
building_images = query_metadata('building', True, token)
print(f'image metadata: {building_images}')

# For the "building" images found from the above query, write them to where this file is.
for image in building_images:
    image_id = image['ID']
    get_image(image_id, f'retrieved-image-{image_id}.jpg', token)


# NOTE:
# Below is the API for uploading an image by its metadata and image file.
# Currently experiencing a bug but will fix it ASAP.
# Will also include the example API for account creation, account logout, 
# getting image tags by id, and update image metadata.

'''
def upload_image(metadata, image, auth):
    r = requests.post(endpoint('/upload'), json={'meta': metadata}, files=image, headers={'Authorization': auth})
    print(r.json())
'''


'''
with open('ape.jpg', 'rb') as file:
    metadata =  [{
        'name': 'ape.jpg',
        'format': 'image/jpeg',
        'description': 'A cool ape!',
        'location': 'Southeast Asia',
        'private': True,
        'type': 'image',
    }]
    image = {
        'ape.jpg': file
    }
    upload_image(metadata, image, token)
'''