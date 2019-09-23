#!/usr/bin/env python3
# coding: utf-8

"""
Bing Image Archive Spider
“必应美图归档”爬虫

https://istartedsomething.com/bingimages/
2009-05-25 – Now
"""

import calendar
import configparser
import datetime
import os.path
import pyquery
import re
import requests
import threading
import time
import tkinter
import tkinter.scrolledtext
import tkinter.ttk

#: countries code and name
COUNTRIES = \
    {'au': 'Australia', 'br': 'Brazil', 'ca': 'Canada', 'cn': 'China',
     'de': 'Germany', 'fr': 'France', 'jp': 'Japan', 'nz': 'New Zealand',
     'gb': 'United Kingdom', 'us': 'United States'}

#: earliest day
EARLIEST_DAY = datetime.date(2009, 5, 25)


def _gen_bia_html_url(date):
    """Generate BIA HTML URL"""
    assert isinstance(date, datetime.date)
    assert EARLIEST_DAY < date
    assert date < datetime.date.today()
    return 'https://www.istartedsomething.com/bingimages/?m=%02d&y=%04d' % (date.month, date.year)


def _find_bia_img_name(html, date, cnty):
    """Find BIA Image Name"""
    assert isinstance(html, pyquery.PyQuery)
    assert isinstance(date, datetime.date)
    assert EARLIEST_DAY < date
    assert date < datetime.date.today()
    assert cnty in COUNTRIES
    href = '#%04d%02d%02d-%s' % (date.year, date.month, date.day, cnty)
    orig = html.find("[href='%s']" % href).find('.lazy').attr('data-original')
    if orig is None:
        return None
    return orig[13:-6]


def _gen_bia_img_url(imgname):
    """Genarate BIA Image URL"""
    assert isinstance(imgname, str)
    return 'http://www.istartedsomething.com/bingimages/cache/' + imgname


def _save_bia_img(imgurl, imgpath):
    """Save BIA Image"""
    assert isinstance(imgurl, str)
    assert isinstance(imgpath, str)
    with open(imgpath, 'wb') as file:
        resp = requests.get(imgurl, stream=True)
        if not resp.ok:
            return resp.status_code

        for block in resp.iter_content(1024):
            if not block:
                break
            file.write(block)
        return resp.status_code


def save_bia_img_to_flr(date, cntys, flrpath):
    """Save BIA Image to Folder"""
    if not isinstance(date, datetime.date):
        raise TypeError
    if date < EARLIEST_DAY or datetime.date.today() < date:
        raise ValueError
    if not isinstance(cntys, set):
        raise TypeError
    if not cntys.issubset(COUNTRIES):
        raise ValueError
    if not isinstance(flrpath, str):
        raise TypeError
    if not os.path.isdir(flrpath):
        raise OSError

    rslt = dict()

    html = pyquery.PyQuery(url=_gen_bia_html_url(date))
    for cnty in cntys:
        imgname = _find_bia_img_name(html, date, cnty)
        if imgname is None:
            rslt[cnty] = 404
            continue

        rslt[cnty] = _save_bia_img(_gen_bia_img_url(imgname), os.path.join(flrpath, imgname))

    return rslt


class BiaSpiderApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        #
        #
        # VIEW, set data from here
        #

        #
        # TOP & SUB-1

        self.title('Bing Image Archive Spider')

        #: (main) pane
        self.pane = tkinter.ttk.PanedWindow(self, orient=tkinter.VERTICAL)
        self.pane.pack(padx=7, pady=7)

        #
        # SUB-2

        #: string pane
        self.str_pane = tkinter.ttk.PanedWindow(self.pane, orient=tkinter.HORIZONTAL)
        self.pane.add(self.str_pane)
        #: button pane
        self.btn_pane = tkinter.ttk.PanedWindow(self.pane, orient=tkinter.HORIZONTAL)
        self.pane.add(self.btn_pane)
        #: message box
        self.msgbox = tkinter.scrolledtext.ScrolledText(self.pane)
        self.pane.add(self.msgbox)
        #: progress variables
        self.prog_var = tkinter.IntVar()
        #: progress bar
        self.prog_bar = tkinter.ttk.Progressbar(self.pane, variable=self.prog_var)
        self.pane.add(self.prog_bar)

        #
        # SUB-3

        #: start date pane
        self.start_date_pane = tkinter.ttk.PanedWindow(self.str_pane, orient=tkinter.HORIZONTAL)
        self.str_pane.add(self.start_date_pane)
        #: end date pane
        self.end_date_pane = tkinter.ttk.PanedWindow(self.str_pane, orient=tkinter.HORIZONTAL)
        self.str_pane.add(self.end_date_pane)
        #: folder path pane
        self.flr_path_pane = tkinter.ttk.PanedWindow(self.str_pane, orient=tkinter.HORIZONTAL)
        self.str_pane.add(self.flr_path_pane)

        #: country variables
        self.cnty_vars = dict()
        #: country check buttons
        self.cnty_ckbtns = dict()
        for code, name in COUNTRIES.items():
            self.cnty_vars[code] = tkinter.BooleanVar()
            self.cnty_ckbtns[code] = tkinter.ttk.Checkbutton(self.btn_pane, text=name, variable=self.cnty_vars[code],
                                                             command=self.__on_cnty_ckbtns_com)
            self.btn_pane.add(self.cnty_ckbtns[code])
        #: download button
        self.dnld_btn = tkinter.ttk.Button(self.btn_pane, text='下载', command=self.__on_dnld_btn_com)
        self.btn_pane.add(self.dnld_btn)

        #
        # SUB-4

        #: start date label
        self.start_date_lbl = tkinter.ttk.Label(self.start_date_pane, text='开始时间')
        self.start_date_pane.add(self.start_date_lbl)
        #: start date variable
        self.start_date_var = tkinter.StringVar()
        #: start date entry
        self.start_date_ent = tkinter.ttk.Entry(self.start_date_pane, textvariable=self.start_date_var)
        self.start_date_ent.bind('<Cancel>', self.__on_start_date_ent_cancel)
        self.start_date_ent.bind('<Escape>', self.__on_start_date_ent_cancel)
        self.start_date_ent.bind('<Return>', self.__on_start_date_ent_normalize)
        self.start_date_ent.bind('<FocusOut>', self.__on_start_date_ent_normalize)
        self.start_date_pane.add(self.start_date_ent)

        #: end date label
        self.end_date_lbl = tkinter.ttk.Label(self.end_date_pane, text='结束时间')
        self.end_date_pane.add(self.end_date_lbl)
        #: end date variable
        self.end_date_var = tkinter.StringVar()
        #: end date entry
        self.end_date_ent = tkinter.ttk.Entry(self.end_date_pane, textvariable=self.end_date_var)
        self.end_date_ent.bind('<Cancel>', self.__on_end_date_ent_cancel)
        self.end_date_ent.bind('<Escape>', self.__on_end_date_ent_cancel)
        self.end_date_ent.bind('<Return>', self.__on_end_date_ent_normalize)
        self.end_date_ent.bind('<FocusOut>', self.__on_end_date_ent_normalize)
        self.end_date_pane.add(self.end_date_ent)

        #: folder path label
        self.flr_path_lbl = tkinter.ttk.Label(self.flr_path_pane, text='本地路径')
        self.flr_path_pane.add(self.flr_path_lbl)
        #: folder path variable
        self.flr_path_var = tkinter.StringVar()
        #: folder path entry
        self.flr_path_ent = tkinter.ttk.Entry(self.flr_path_pane, textvariable=self.flr_path_var)
        self.flr_path_ent.bind('<Cancel>', self.__on_flr_path_ent_cancel)
        self.flr_path_ent.bind('<Escape>', self.__on_flr_path_ent_cancel)
        self.flr_path_ent.bind('<Return>', self.__on_flr_path_ent_normalize)
        self.flr_path_ent.bind('<FocusOut>', self.__on_flr_path_ent_normalize)
        self.flr_path_pane.add(self.flr_path_ent)

        #
        #
        # MODEL, get date from here
        #

        self.start_date = EARLIEST_DAY
        self.end_date = datetime.date.today()
        self.flr_path = self.DEF_FLR_PATH

        self.read_ini()

        self.__dnld_thr_flag = False

    def __sort_start_end_date(self):
        if self.end_date < self.start_date:
            self.end_date, self.start_date = self.start_date, self.end_date
            self.start_date_var.set(self.start_date.isoformat())
            self.end_date_var.set(self.end_date.isoformat())

    def __on_start_date_ent_cancel(self, event=None):
        self.start_date_var.set(self.start_date.isoformat())

    def __on_start_date_ent_normalize(self, event=None):
        datestr = self.start_date_var.get()
        if datestr == self.start_date.isoformat():
            return

        date = self.strpdate(datestr)
        if date is None:
            self.__on_start_date_ent_cancel()
            return

        self.start_date = date
        self.start_date_var.set(self.start_date.isoformat())
        self.__sort_start_end_date()
        self.write_ini()

    def __on_end_date_ent_cancel(self, event=None):
        self.end_date_var.set(self.end_date.isoformat())

    def __on_end_date_ent_normalize(self, event=None):
        datestr = self.end_date_var.get()
        if datestr == self.end_date.isoformat():
            return

        date = self.strpdate(datestr)
        if date is None:
            self.__on_end_date_ent_cancel()
            return

        self.end_date = date
        self.end_date_var.set(self.end_date.isoformat())
        self.__sort_start_end_date()
        self.write_ini()

    def __on_flr_path_ent_cancel(self, event=None):
        pass

    def __on_flr_path_ent_normalize(self, event=None):
        pass

    def __on_cnty_ckbtns_com(self):
        """On Country Check-Buttons Command"""
        self.write_ini()

    def __on_dnld_btn_com(self):
        """On Download Button Command"""
        cntys = set()
        for code, var in self.cnty_vars.items():
            if var.get():
                cntys.add(code)
        if len(cntys) == 0:
            return

        self.dnld_btn.config(state=tkinter.DISABLED)
        self.prog_bar.config(maximum=((self.end_date - self.start_date).days + 1) * len(cntys))
        self.prog_var.set(0)

        self.__dnld_thr_flag = True
        thr = threading.Thread(target=self.__dnld_thr, name='LoopThread')
        thr.start()

    def __dnld_thr(self):
        cntys = set()
        for code, var in self.cnty_vars.items():
            if var.get():
                cntys.add(code)

        date = self.start_date
        while date <= self.end_date:
            html = pyquery.PyQuery(url=_gen_bia_html_url(date))
            for cnty in cntys:
                if not self.__dnld_thr_flag:
                    self.dnld_btn.config(state=tkinter.ACTIVE)
                    return
                imgname = _find_bia_img_name(html, date, cnty)
                if imgname is not None:
                    _save_bia_img(_gen_bia_img_url(imgname), os.path.join(self.flr_path, imgname))
                self.prog_var.set(self.prog_var.get() + 1)

            date += datetime.timedelta(days=1)
            time.sleep(5)

        self.dnld_btn.config(state=tkinter.ACTIVE)

    #: default .ini file path
    DEF_INI_PATH = os.path.splitext(__file__)[0] + '.ini'
    #: default (image save) folder path
    DEF_FLR_PATH = os.path.join(os.path.dirname(__file__), 'img')

    def read_ini(self, inipath=DEF_INI_PATH):
        if not isinstance(inipath, str):
            raise TypeError
        if not os.path.isfile(inipath):
            return ValueError

        cp = configparser.ConfigParser()
        cp.read(inipath)

        self.start_date_var.set(cp.get('CONFIG', 'start_date', fallback=EARLIEST_DAY.isoformat()))
        self.end_date_var.set(cp.get('CONFIG', 'end_date', fallback=datetime.date.today().isoformat()))
        self.flr_path_var.set(cp.get('CONFIG', 'flr_path', fallback=self.DEF_FLR_PATH))
        for code, var in self.cnty_vars.items():
            var.set(
                cp.getboolean('CONFIG', 'cnty_' + code, fallback=False))

        self.__on_start_date_ent_normalize()
        self.__on_end_date_ent_normalize()
        self.__on_flr_path_ent_normalize()

    def write_ini(self, inipath=DEF_INI_PATH):
        if not isinstance(inipath, str):
            raise TypeError
        try:
            with open(inipath, 'w') as file:
                cp = configparser.ConfigParser()
                cp['CONFIG'] = {}
                cp['CONFIG']['start_date'] = self.start_date.isoformat()
                cp['CONFIG']['end_date'] = self.end_date.isoformat()
                cp['CONFIG']['flr_path'] = self.flr_path
                for code, var in self.cnty_vars.items():
                    cp['CONFIG']['cnty_' + code] = str(var.get())
                cp.write(file)
        except IOError:
            raise

    @staticmethod
    def strpdate(datestr):
        """String Parse to Date"""
        if not isinstance(datestr, str):
            raise TypeError

        rslt = None
        for fmt in (r'^\s*(\d{4})(\d{2})(\d{2})\s*$',
                    r'^\s*(\d{2}|\d{4})[\s\-/]+(\d{1,2})[\s\-/]+(\d{1,2})\s*$'):
            rslt = re.match(fmt, datestr)
            if rslt is not None:
                break
        if rslt is None:
            return None

        today = datetime.date.today()

        year = int(rslt.group(1))
        if len(rslt.group(1)) == 2:
            year += today.year // 100 * 100
            year -= 100 if today.year < year else 0

        year = min(max(EARLIEST_DAY.year, year), today.year)
        month = min(max(1, int(rslt.group(2))), 12)
        day = min(max(1, int(rslt.group(3))), calendar.monthrange(year, month)[1])

        return min(max(EARLIEST_DAY, datetime.date(year, month, day)), today)


def _test():
    pass


def _main():
    app = BiaSpiderApp()
    app.mainloop()


if __name__ == '__main__':
    _main()
