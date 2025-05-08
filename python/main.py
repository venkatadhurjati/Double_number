import requests
from bs4 import BeautifulSoup

def print_character_grid(doc_url):
    # Fetch HTML content
    response = requests.get(doc_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract table rows
    rows = soup.find_all('tr')[1:]  # Skip header
    entries = []

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            try:
                x = int(cells[0].text.strip())
                char = cells[1].text.strip()
                y = int(cells[2].text.strip())
                entries.append((x, y, char))
            except ValueError:
                continue

    # Determine grid size
    max_x = max(x for x, _, _ in entries)
    max_y = max(y for _, y, _ in entries)

    # Create and populate grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in entries:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print(''.join(row))

# Run the function with the provided document
print_character_grid("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
