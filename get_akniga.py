from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options

from subprocess import run
import re
import sys

def get_playlist_url(url):
    target_url = ''

    try:
        # Create a new instance of the Chrome driver
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless") # Comment for visualy debugging

        driver = webdriver.Chrome(options=chrome_options)

        def interceptor(request):
            # Block unneeded files: images, ads etc.
            if request.path.endswith(('.png', '.jpg', '.gif', '.webm', '.svg', '.ico', '.woff2', '.css')) or \
                request.path.startswith(('/get-direct', '/favicon')) or \
                    'yandex' in request.path:
                request.abort()

        driver.request_interceptor = interceptor
        driver.get(url)

        # Access requests via the `requests` attribute
        for request in driver.requests:
            if 'pl.m3u8?res=' in request.url:
                target_url = request.url
    finally:
        driver.close()
    return target_url

def main(url, file_name=''):

    # target_url = "https://h7.akniga.club/b/87151/pl.m3u8?res=m_GFHEHjXoY10onOFZzlTQ&expires=1701573814"
    target_url = get_playlist_url(url)
    if target_url:
        print(f"Play list url found: {target_url}")
    else:
        print('Cannot find a playlist url for provided book.')
        exit()
    if not file_name:
        file_name = url.split('/')[-1]+'.mp3'
    print(f'Streaming to file {file_name}')
    run(['vlc', target_url,
        f'--sout=#transcode{{acodec=mp3}}:std{{access=file,mux=ffmpeg,dst={file_name}}}',
        '--no-sout-video', '--sout-audio', 'vlc://quit'#, '-I', 'dummy'
        ])

if __name__ == "__main__":
    url = file_name = ''
    if len(sys.argv) > 1:
        url = sys.argv[1]
        if len(sys.argv) > 2:
            file_name = sys.argv[2]
    else:
        url = input('Enter target url:')
    # The url should be in format https://akniga.org/valenteeva-olga-vremya-ne-znaet-zhalosti
    r = re.compile("https://akniga.org/(\w+-)*\w+$", re.IGNORECASE)
    if r.match(url):
        main(url, file_name)
    else:
        print("Invalid url. Expected url in the format:\n\n\thttps://akinga.org/book-name")