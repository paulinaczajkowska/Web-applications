from bs4 import BeautifulSoup
import requests

# Main page
bouldering_md_content = """# Bouldering

<p align="center">
  <img src="docs/images/image1.jpeg" height="100px">
  <img src="docs/images/image2.jpeg" height="100px">
  <img src="docs/images/image3.jpeg" height="100px">
</p>

## What is bouldering?
Bouldering is a form of rock climbing performed on small rock formations or artificial walls without the use of ropes or harnesses. Climbers rely on crash pads for protection and focus on short but challenging routes known as "problems".

## Equipment needed
- Climbing shoes
- Chalk and chalk bag
- Crash pads
- Brush for cleaning holds

## Basic Techniques
1. **Footwork** - precise foot placements improve balance and efficiency,
2. **Body positioning** - using body tension to stay on the wall,
3. **Dynos** - jumping from one hold to another,
4. **Crimping** - using fingertips to grip small holds,
5. **Mantling** - pushing down on a hold to move upward.

## Popular bouldering locations
- Fontainebleau, France,
- Rocklands, South Africa,
- Hueco Tanks, USA,
- Magic Wood, Switzerland.

## Bouldering Grading Systems
- **V-Scale (USA)**: ranges from V0 (easy) to V17+ (extreme),
- **Font Scale (Europe)**: starts at 3 and goes up to 9A+

## List Of The Hardest Boulders
[Routes so tough that even your father wouldn't have done them injury-free in '86.](boulders.md)
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
