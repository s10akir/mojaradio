#! /usr/bin/env python

from mojaradio.Recorder import Recorder

recorder = Recorder()
recorder.fetch_timetable()
recorder.reserve_all()
