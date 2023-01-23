import os.path
import random
from PIL import Image
from io import BytesIO
import requests
from helpers import get_random_string


def test_create_and_get_by_id():
    """
    Tests post method.
    Tests get by id method
    """

    url = 'http://localhost:8001/api/images/'
    file = 'testimage.png'
    file = os.path.join(os.path.dirname(__file__), file)

    title = 'test' + get_random_string(10)
    width = random.randint(10, 1000)
    height = random.randint(10, 1000)

    data = {
        'title': title,
        'width': width,
        'height': height
    }

    with open(file, 'rb') as f:
        files = {'file': f}
        response = requests.post(url=url, files=files, data=data)

    assert response.status_code == 201
    assert all(list(map(lambda x: x in response.json().keys(), ['id', 'title', 'file', 'width', 'height'])))

    _id = response.json()['id']
    url = url + f'{_id}/'
    response = requests.get(url)
    assert response.status_code == 200
    assert all(list(map(lambda x: x in response.json().keys(), ['id', 'title', 'file', 'width', 'height'])))


def test_create_and_get_by_title():
    """
    Tests filtering by part of an image title.
    """

    url = 'http://localhost:8001/api/images/'
    file = 'testimage.png'
    file = os.path.join(os.path.dirname(__file__), file)

    title = get_random_string(20)
    subtitle = title[3:14]  # part of a title, to look for it
    title = 'test' + title

    width = random.randint(10, 1000)
    height = random.randint(10, 1000)

    data = {
        'title': title,
        'width': width,
        'height': height
    }
    with open(file, 'rb') as f:
        files = {'file': f}
        response = requests.post(url=url, files=files, data=data)
    assert response.status_code == 201

    response = requests.get(url, data={"title": subtitle})
    assert response.status_code == 200
    print(response.json())
    assert response.json()['results'][0]['title'] == title


def test_resized():
    """
    Tests if returned image's width and height are equal to requested.
    """

    url = 'http://localhost:8001/api/images/'
    file = 'testimage.png'
    file = os.path.join(os.path.dirname(__file__), file)

    title = 'test' + get_random_string(10)
    new_width = random.randint(10, 1000)
    new_height = random.randint(10, 1000)

    data = {
        'title': title,
        'width': new_width,
        'height': new_height
    }

    with open(file, 'rb') as f:
        files = {'file': f}
        response = requests.post(url=url, files=files, data=data)

    img_url = response.json()['file']
    resized_image = requests.get(img_url).content
    resized_image = Image.open(BytesIO(resized_image))

    assert resized_image.height == new_height
    assert resized_image.width == new_width