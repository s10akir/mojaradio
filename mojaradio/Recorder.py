import re
import urllib.request
import xml.etree.ElementTree as ElementTree

from mojaradio.Station import Station
from mojaradio.Program import Program


class Recorder:
    def __init__(self):
        self.stations = []

    def fetch_timetable(self):
        url = 'http://radiko.jp/v2/api/program/today?area_id=JP13'
        response = urllib.request.urlopen(url)
        data = response.read()
        decoded_data = data.decode('utf-8')  # 明示的にデコードしないと日本語は化ける

        root = ElementTree.fromstring(decoded_data)
        stations = root[2]

        for station in stations:
            station_id = station.attrib['id']
            name = station[0].text

            programs = self.__parse_progs(station[1][0])
            # create Station instance
            station = Station(station_id, name, programs)
            self.stations.append(station)

    @staticmethod
    def __parse_progs(progs):
        programs = []

        for prog in progs:
            if prog.tag == 'prog':
                title = prog[0].text
                pfm = prog[3].text
                ft = prog.attrib['ft']
                dur = prog.attrib['dur']

                if not re.match('(放送|番組)休止中', title):
                    # create Program instance
                    program = Program(title, pfm, ft, dur)
                    programs.append(program)

        return programs

    @staticmethod
    def reserve(program):
        # TODO
        print('reserved:', vars(program))  # dummy

    def reserve_all(self):
        for station in self.stations:
            for program in station.programs:
                self.reserve(program)

    def show_timetable(self):
        for station in self.stations:
            station.show_info()
            station.show_programs()
            print()
