from bs4 import BeautifulSoup
import requests

# Main page
bouldering_md_content = """# Bouldering

## What is Bouldering?
Bouldering is a form of rock climbing performed on small rock formations or artificial walls without the use of ropes or harnesses. Climbers rely on crash pads for protection and focus on short but challenging routes known as "problems."

## Equipment Needed
- Climbing Shoes
- Chalk and Chalk Bag
- Crash Pads
- Brush for Cleaning Holds

## Basic Techniques
1. **Footwork** - Precise foot placements improve balance and efficiency.
2. **Body Positioning** - Using body tension to stay on the wall.
3. **Dynos** - Jumping from one hold to another.
4. **Crimping** - Using fingertips to grip small holds.
5. **Mantling** - Pushing down on a hold to move upward.

## Popular Bouldering Locations
- Fontainebleau, France
- Rocklands, South Africa
- Hueco Tanks, USA
- Magic Wood, Switzerland

## Bouldering Grading Systems
- **V-Scale (USA)**: Ranges from V0 (easy) to V17+ (extreme)
- **Font Scale (Europe)**: Starts at 3 and goes up to 9A+

## Safety Tips
- Always use a spotter.
- Position crash pads correctly.
- Warm up before climbing.
- Know your limits and listen to your body.

<p align="center">
  <img src="docs/images/image1.png" width="30%">
  <img src="docs/images/image2.png" width="30%">
  <img src="docs/images/image3.png" width="30%">
</p>
"""

with open("index.md", "w") as file:
    file.write(bouldering_md_content)


# List page
link = "https://climbing-history.org/list/26/the-hardest-boulder-problems-in-the-world"
response = requests.post(link)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='table')
climbs = [a.get_text(strip=True) for a in soup.find_all('a', href=True) if a['href'].startswith('/climb/')]
climbs = climbs[:13]
md_string = "\n".join(f"- {climb}" for climb in climbs)

with open('boulders.md', 'w') as file:
    file.write(md_string)