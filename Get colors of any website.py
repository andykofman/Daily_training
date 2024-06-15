import requests
from bs4 import BeautifulSoup
import re

def extract_colors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all style tags and extract their content
    styles = soup.find_all('style')
    style_content = ' '.join([style.get_text() for style in styles])
    
    # Find all inline styles
    inline_styles = ' '.join([tag.get('style') for tag in soup.find_all(True, style=True)])
    
    # Combine all styles into one string
    all_styles = style_content + ' ' + inline_styles
    
    # Use regular expressions to find color codes
    hex_colors = re.findall(r'#[0-9a-fA-F]{6}', all_styles)
    rgb_colors = re.findall(r'rgb\(\d{1,3}, \d{1,3}, \d{1,3}\)', all_styles)
    
    return set(hex_colors + rgb_colors)

url = 'https://developer.spotify.com/'
colors = extract_colors(url)
print(colors)
