import os
import csv
from datetime import datetime
from recipe_scrapers import scrape_me

path = os.path.dirname(os.path.abspath(__file__))

print(path)
array = []
with open(path + '/bbcgoodfood.csv', newline='', encoding='utf-8') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in reader:
      array.append(row)


output_filename = '/bbcgoodfood_output_' + str(datetime.now().microsecond) + '.csv'

with open(path + output_filename, 'w', newline='', encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['CALS', 'LINK', 'TITLE', 'DIFFICULTY', 'TOTAL_TIME', 'PREP_TIME', 'COOK_TIME', 'YIELDS', 'INGREDIENTS', 'INSTRUCTIONS', 'IMAGE', 'HOST', 'CALS', 'FAT', 'SATURATED_FAT', 'CARBS', 'SUGARS', 'FIBER', 'PROTEIN', 'SALT'])
  for row in array:
    scraper = scrape_me(row[0])
    # print([row[0], scraper.title().replace(',', ';'), scraper.total_time(), scraper.yields().replace(',', ';'), str(scraper.ingredients()).replace(',', ';'), str(scraper.instructions()).replace(',', '*').replace('\n', ''), scraper.image(), scraper.host()])
    print(row[0])
    writer.writerow([row[0], scraper.title().replace(',', ';'), scraper.difficulty(), scraper.total_time(), scraper.prep_time(), scraper.cook_time(), scraper.yields().replace(',', ';'), str(scraper.ingredients()).replace(',', ';'), str(scraper.instructions()).replace(',', '*').replace('\n', ''), scraper.image(), scraper.host(),
    scraper.calories(), scraper.fat(), scraper.saturated_fat(), scraper.carbs(), scraper.sugars(), scraper.fiber(), scraper.protein(), scraper.salt()])

print("COMPLETE!")
print(output_filename)