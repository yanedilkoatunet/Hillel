import requests
from urllib.parse import urlparse

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"

search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 50
}

response = requests.get(search_url, params=search_params)
response.raise_for_status()

data = response.json()

items = data["collection"]["items"]

downloaded = 0

for item in items:

    nasa_id = item["data"][0]["nasa_id"]

    print(f"Checking: {nasa_id}")

    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    asset_data = asset_response.json()

    files = asset_data["collection"]["items"]

    jpg_url = None

    for file in files:
        url = file["href"]
        path = urlparse(url).path.lower()

        if path.endswith((".jpg", ".jpeg")):
            jpg_url = url
            break

    if jpg_url is None:
        print(f"No JPG found for {nasa_id}")
        continue

    image_response = requests.get(jpg_url)
    image_response.raise_for_status()

    downloaded += 1
    filename = f"mars_photo{downloaded}.jpg"

    with open(filename, "wb") as image:
        image.write(image_response.content)

    print(f"Downloaded: {filename}")

    if downloaded == 2:
        break

if downloaded == 2:
    print("Successfully downloaded 2 images!")
else:
    print(f"Only {downloaded} images downloaded.")
