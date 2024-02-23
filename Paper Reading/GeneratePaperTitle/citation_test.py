import requests

# Get the paper's DOI
doi = "10.1109/CVPR.2023.8345487"

# Make a request to Google Scholar
response = requests.get("https://scholar.google.com/scholar?cites={}".format(doi))

# Parse the response
soup = BeautifulSoup(response.content, "html.parser")

# Get the citation number
citation_number = soup.find("div", class_="gs_ri").find("span", class_="gs_ri_c").text

print(citation_number)