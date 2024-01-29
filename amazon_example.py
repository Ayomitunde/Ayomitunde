import requests
from selectolax.parser import HTMLParser



carslist = []

# def extract_text(soup, selector):
#     try:
#         return soup.select_one(selector).get_text().strip()
#     except AttributeError as err:
#         print(err)
#         return None 
def get_cars(page):
    resp = requests.get(f"https://www.cars45.com/listing?page={page}")
    html = HTMLParser(resp.text)
    cars = html.css("a.car-feature.car-feature--wide-mobile")
    for car in cars:
        cars45 ={
            "name":car.css_first("p.car-feature__name").text(strip = True),
            "link" : car.css_first("a.car-feature.car-feature--wide-mobile").attrs['href'],
            "price" : car.css_first("p.car-feature__amount").text(strip = True),
            "condition" : car.css_first("span.car-feature__others__item").text(strip = True),
            "location" :car.css_first("p.car-feature__region").text(strip = True)
        }
        carslist.append(cars45)
    return

for x in range(1,15):
    get_cars(page)

    