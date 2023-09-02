from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import subprocess

class ScreenRecorder:
    def __init__(self, output_file):
        self.output_file = output_file
        self.proc = None

    def start_recording(self):
        # Command to start recording using ffmpeg
        command = [
            'ffmpeg',
            '-f', 'gdigrab',
            '-framerate', '30',
            '-i', 'desktop',
            '-c:v', 'libx264',
            '-r', '30',
            '-preset', 'ultrafast',
            '-crf', '0',
            self.output_file
        ]

        # Start the ffmpeg process
        self.proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for a second to ensure the recording has started
        time.sleep(1)

    def stop_recording(self):
        if self.proc is not None:
            # Terminate the ffmpeg process
            self.proc.terminate()
            self.proc = None

# Path to your ChromeDriver executable
webdriver_service = Service('C:/Users/admin/Downloads/Chrome/chromedriver.exe')

# Path to ffmpeg executable
#ffmpeg_path ="C:\Users\admin\Downloads\Chrome"

# Set the output file for screen recording
output_file = 'screen_recording.mp4'

# Create a ScreenRecorder instance
recorder = ScreenRecorder(output_file)

# Start recording
recorder.start_recording()
print('Recording started...')

# Create ChromeOptions and set necessary arguments
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# Create the WebDriver instance
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Perform your automation steps
driver.get('https://www.example.com')
driver.maximize_window()
# ... perform other actions ...

# Stop recording
recorder.stop_recording()
print('Recording stopped. File saved as', output_file)

# Close the WebDriver
driver.quit()
