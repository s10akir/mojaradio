class Program:
    def __init__(self, title, pfm, ft, dur):
        self.title = title
        self.pfm = pfm
        self.ft = ft
        self.dur = dur

    def show_info(self):
        print(' ', self.ft, self.dur, self.title, self.pfm)
