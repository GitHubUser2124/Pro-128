from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

stars_data = []

def scrape_data(hyperlink):
    
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        all_tables = soup.find_all("table", attrs={"class": "wikitable sortable jquery-tablesorter"})

        for tr_tag in all_tables:
                td_tags = tr_tag.find_all("td")
                for td_tag in td_tags:
                    try:
                        temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                    except:
                        temp_list.append("")
                
    
        stars_data.append(temp_list)

    except:
        time.sleep(1)
        scrape_data(hyperlink)

star_df_1 = pd.read_csv("scraped_data.csv")

for index, row in star_df_1.iterrows():

    ## ADD CODE HERE ##
    for index, row in star_df_1.iterrows():
        print(row['hyperlink'])
        scrape_data(row['hyperlink'])
    
headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]

df = pd.DataFrame(stars_data, columns=headers)
df.to_csv("final_scraped_data")