import requests
from pathlib import Path
from urllib.parse import urlparse, quote

BASE_URL = "http://127.0.0.1:8080"

image_path = Path(__file__).parent / "mars_photo1.jpg"

upload_url = f"{BASE_URL}/upload"

with open(image_path, "rb") as image:
    files = {
        "image": (
            image_path.name,
            image,
            "image/jpeg"
        )
    }

    upload_response = requests.post(upload_url, files=files)

upload_response.raise_for_status()

print("POST status:", upload_response.status_code)

upload_data = upload_response.json()
image_url = upload_data["image_url"]

print("Uploaded image URL:", image_url)


filename = urlparse(image_url).path.split("/")[-1]

get_url = f"{BASE_URL}/image/{quote(filename)}"

get_response = requests.get(
    get_url,
    headers={"Content-Type": "text"}
)

get_response.raise_for_status()

get_data = get_response.json()

print("GET status:", get_response.status_code)
print("Image URL:", get_data["image_url"])


delete_url = f"{BASE_URL}/delete/{quote(filename)}"

delete_response = requests.delete(delete_url)

delete_response.raise_for_status()

print("DELETE status:", delete_response.status_code)
print("Delete response:", delete_response.json())

print("All operations completed successfully!")
