from ._abstract import AbstractScraper
from bs4 import BeautifulSoup


class BBCGoodFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "bbcgoodfood.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def prep_time(self):
        return self.schema.prep_time()

    def difficulty(self):
        container = self.soup.find("div", {"class": "masthead__skill-level"})
        if not container:
            return None
        difficulty = container.find("div", {"class": "icon-with-text__children"})
        return difficulty.text if difficulty else None

    def calories(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 1
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None
        
    def fat(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 2
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def saturated_fat(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 3
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def carbs(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 4
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def sugars(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 5
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def fiber(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 6
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def protein(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 7
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def salt(self):
        table = self.soup.find("table", {"class": "key-value-blocks hidden-print"})
        if not table:
            return None
        table_trs = table.find_all("tr")
        index = 8
        if len(table_trs) >= index + 1:
            k_cal_container = table_trs[index].find("td", {"class": "key-value-blocks__value"})
            return k_cal_container.text if k_cal_container else None
        else:
            return None

    def cook_time(self):
        return self.schema.cook_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        inst = str(self.schema.instructions())
        instSoup = BeautifulSoup(inst, features="html.parser")
        return instSoup.text
