from abc import ABC, abstractmethod
from grab import Grab
from bs4 import BeautifulSoup as BSHTML
import logging
import os

FULLPATH = "/Users/ilchel/Desktop/projects/agregator/"


""" Абстрактный класс для реализации адаптеров курортов. """


class Courort(ABC):
    @abstractmethod
    def getCourortName():
        pass

    @abstractmethod
    def _getData():
        pass

    @abstractmethod
    def parseDoc():
        pass


""" Красная поляна """


class Polyana(Courort):
    def __init__(self):
        self.webpage = "https://krasnayapolyanaresort.ru/slopes_new"
        self.nameRus = "Горнолыжный курорт Красная Поляна"
        self.nameEng = "Polyana"
        self.filePath = "log/polyana/page.txt"
        self.fullFilePath = FULLPATH + self.filePath

    def getCourortName(self):
        return [self.nameRus, self.nameEng]

    def _getData(self):
        error_code = 0
        try:
            os.system("curl " + self.webpage + " -o " + self.fullFilePath)
        except:
            error_code = 1
        return error_code

    def parseDoc(self):
        # Try download page (Check if errors)
        if self._getData() != 0:
            print("Error downloading webpage")
            return
        return self._parseDocLiftsXTrails()

    def _parseDocLiftsXTrails(self):
        # Try open file (check if errors)
        try:
            file = open(self.fullFilePath, "r")
        except IOError:
            print("Rosa file did not found")

        trailsFinal = []
        trailsData = file.read()
        soup = BSHTML(trailsData, "lxml")
        trails = soup.findAll(
            "a", {"class": "panel__item pointer js-slopes-el panel__item--off"}
        )

        for i in range(len(trails)):
            soup = BSHTML(str(trails[i]), "lxml")
            trail = soup.find("a", {"class": "panel__item"})
            trailsFinal.append(
                [
                    polyanaCheckIfTrail(str(soup.a["data-id"])),
                    trail.contents[0].strip(),
                    polyanaCheckIfOpen(int(soup.a["data-status"])),
                ]
            )

        file.close()
        return trailsFinal


""" Горнолыжный курорт Лаура. """


class Laura(Courort):
    def __init__(self):
        self.webpage = "https://polyanaski.ru/ski-resort/track/"
        self.nameRus = "Горно-туристический центр Газрпром (Лаура)"
        self.nameEng = "Laura"
        self.filePath = "log/laura/page.txt"
        self.fullFilePath = FULLPATH + self.filePath

    def getCourortName(self):
        return [self.nameRus, self.nameEng]

    def _getData(self):
        error_code = 0
        try:
            os.system("curl " + self.webpage + " -o " + self.fullFilePath)
        except:
            error_code = 1
        return error_code

    # TODO: parse lifts(ul on site)
    def parseDoc(self):
        # Try download page (Check if errors)
        if self._getData() != 0:
            print("Error downloading webpage")

        # Try open file (check if errors)
        try:
            file = open(self.fullFilePath, "r")
        except IOError:
            print("Rosa file did not found")

        trailsFinal = []
        trailsData = file.read()
        soup = BSHTML(trailsData, "lxml")
        trails = soup.findAll("tr")

        for i in range(1, len(trails)):
            soup = BSHTML(str(trails[i]), "lxml")
            name = soup.find("div", {"class": "lift_name"})
            route = soup.find("div", {"class": "lift_route"})
            time = soup.find("a")
            work = soup.findAll("td")[-1].get_text().strip()
            trailsFinal.append(
                [
                    "lift",
                    name.get_text(),
                    route.get_text(),
                    time.get_text(),
                    lauraCheckWork(work),
                ]
            )

        file.close()
        return trailsFinal

    def parseDocTrails():
        print("Parse")


""" Курорт 'Роза Хутор'. """


class RosaChutor(Courort):
    def __init__(self):
        self.webpage_trails = "https://rosakhutor.com/skiing/trails/"
        self.webpage_lifts = "https://rosakhutor.com/skiing/lifts/"
        self.nameRus = "Роза Хутор"
        self.nameEng = "Rosa Khutor"
        self.filePathLifts = "log/rosa/page_lifts.txt"
        self.filePathTrails = "log/rosa/page_trails.txt"
        self.fullFilePathLifts = FULLPATH + self.filePathLifts
        self.fullFilePathTrails = FULLPATH + self.filePathTrails

    def getCourortName(self):
        return [self.nameRus, self.nameEng]

    def parseDoc(self):
        print(self.fullFilePathLifts)
        # Try download page (Check if errors)
        if self._getData() != 0:
            print("Error downloading webpage")
        return self._parseDocLifts() + self._parseDocTrails()

    # Download page
    def _getData(self):
        error_code = 0
        try:
            os.system("curl " + self.webpage_trails + " -o " + self.fullFilePathTrails)
            os.system("curl " + self.webpage_lifts + " -o " + self.fullFilePathLifts)
        except:
            error_code = 1
        return error_code

    # Parse page
    def _parseDocTrails(self):
        # Try open file (check if errors)
        try:
            file = open(self.fullFilePathTrails, "r")
        except IOError:
            print("Rosa file did not found")

        trailsFinal = []
        trailsData = file.read()
        soup = BSHTML(trailsData, "lxml")
        trails = soup.findAll("div", {"class": "trails_row"})
        
        for i in range(1, len(trails) - 1):
            soup = BSHTML(str(trails[i]), "lxml")
            name = soup.find("div", {"class": "trails_cell--title"})
            complexity = soup.find("div", {"class": "trails_cell--complexity"})
            distance = soup.find("div", {"class": "trails_cell--width"})
            height = soup.find("div", {"class": "trails_cell--height"})
            status = soup.find("div", {"class": "trails_cell--status"})
            
            trailsFinal.append(
                [
                    "trail",
                    str(name.contents[2]).strip(),
                    rosaGetComplexity(str(complexity.contents[1])),
                    distance.contents[3].get_text(),
                    height.contents[3].get_text(),
                    rosaChekIfOpen(str(status.contents).strip()),
                ]
            )

        file.close()
        return trailsFinal

    def _parseDocLifts(self):
        # Try open file (check if errors)
        try:
            file = open(self.fullFilePathLifts, "r")
        except IOError:
            print("Rosa file did not found")

        # Parse file
        liftsFinal = []
        liftData = file.read()
        soup = BSHTML(liftData, "lxml")
        lifts = soup.findAll("div", {"class": "lifts_row"})

        for i in range(1, len(lifts)):
            soup = BSHTML(str(lifts[i]), "lxml")
            name = soup.find("span", {"class": "lifts_title"})
            status = soup.find("div", {"class": "lifts_cell--status"})
            distance = soup.find("div", {"class": "lifts_cell--first-numbers"})
            people = soup.find("div", {"class": "lifts_cell--second-numbers"})
            time = soup.find("div", {"class": "lifts_cell--time"})

            liftsFinal.append(
                [
                    "lift",
                    str(name.contents[2]).strip(),
                    distance.contents[3].get_text(),
                    people.contents[3].get_text(),
                    str(time.contents[1].get_text().strip()),
                    rosaChekIfOpen(str(status.contents).strip())
                ]
            )

        file.close()
        return liftsFinal




def polyanaCheckIfTrail(s):
    if "K" in s or "T" in s:
        return "lift"
    else:
        return "trail"


def polyanaCheckIfOpen(s):
    if s > 0:
        return 0
    else:
        return 1


def rosaChekIfOpen(s):
    a = [s.find("green"), s.find("yellow"), s.find("red"), s.find("grey")]
    return a.index(max(a))


def rosaGetComplexity(s):
    if s.find("--") < 0:
        return "Летние активности"
    return s[s.find("--") + 2 : s.find('">')]


def lauraCheckWork(s):
    if s == "Работает":
        return 0
    else:
        return 1


""" Фабрика. """
class ServiceFactory:
    def __init__(self):
        self.rosa = RosaChutor()
        self.laura = Laura()
        self.polyana = Polyana()

    def getRosa(self):
        return self.rosa.parseDoc()

    def getLaura(self):
        return self.laura.parseDoc()

    def getPolyana(self):
        return self.polyana.parseDoc()


if __name__ == "__main__":
    obj = ServiceFactory()
    data = obj.getLaura()
    for i in range(len(data)):
        print(data[i])
