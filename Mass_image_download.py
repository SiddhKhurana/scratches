import requests
from bs4 import BeautifulSoup
import os

web_pages = ['https://www.google.com/search?q=aqua+konosuba&tbm=isch&chips=q:aqu'+\
'a+konosuba,g_1:cute:ZWuxldQwZFQ%3D&hl=en&sa=X&ved=2ahUKEwiI9u6XsZTuAhX7kUsFHfO-Cz'+\
'wQ4lYoAnoECAEQHA&biw=1349&bih=625']

url_list = []
for page in web_pages:
    url_dictionary = {}
for page in web_pages:    
    # 2. Request the web page:
    r = requests.get(page)
    # 3. Check to see if the web page returned a status_200:
    if r.status_code == 200:

        # 4. Create a URL dictionary entry for future use:
        url_dictionary[page] = []

        # 5. Parse the HTML content with BeautifulSoup and look for image tags:
        soup = BeautifulSoup(r.content, 'html.parser')

        # 6. Find all of the images per web page:
        images = soup.findAll('img')

        # 7. Store all of the images 
        url_dictionary[page].extend(images)

    else:
        print('failed!')

cleaned_dictionary = {key: value for key, value in url_dictionary.items() if len(value) > 0}
for key, images in cleaned_dictionary.items():
    for image in images:
        print(image.attrs['src'])

all_images = []

for key, images in cleaned_dictionary.items():
    # 1. Creating a clean_urls and domain name for every page:
    clean_urls = []
    # 2. Looping over every image per url:
    for image in images:
        # 3. Extracting the source (src) with .attrs:
        source_image_url = image.attrs['src']
        # 4. Clean The Data
        if source_image_url.startswith(('/')):
            pass
        else:
            all_images.append(source_image_url)


def extract_images(image_urls_list:list, directory_path):

    # Changing directory into a specific folder:
    os.chdir(directory_path)

    # Downloading all of the images
    for i,img in enumerate(image_urls_list):
        file_name = f'{i}.jpg'
        print(file_name)

        # Let's try both of these versions in a loop [https:// and https://www.]
        url_paths_to_try = [img, img.replace('https://', 'https://www.')]
        for url_image_path in url_paths_to_try:
            print(url_image_path)
            try:
                r = requests.get(img, stream=True)
                if r.status_code == 200:
                    with open(file_name, 'wb') as f:
                        for chunk in r:
                            f.write(chunk)
            except Exception as e:
                print('There was a ',e) 
                quit()

extract_images(all_images,r'D:\Data')

