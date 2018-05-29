#!/usr/bin/env python3
#-*- coding : utf8 -*-
# 
# Author: Fuat Bölük <fuat@fuxproject.org>
# 

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")

from gi.repository import Gtk, Gio, WebKit2
import sys, os

class Messenger():
    def __init__(self):
        self.window = Gtk.Window()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.set_title("Fux Destek")
        self.window.set_icon_name("destek")
        self.window.set_default_size(1024, 768)

        self.view = Gtk.ScrolledWindow()
        self.webview = WebKit2.WebView()

        self.settings = self.webview.get_settings()
        self.settings.set_property("user-agent", "Mozilla/5.0 (X11; Fux; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0")
        self.settings.set_property("enable-offline-web-application-cache", True)
        self.settings.set_property("enable-javascript", True)
        self.settings.set_property("enable-page-cache", True)

        self.webview.set_settings(self.settings)
        self.webview.load_uri("http://fuxpentest-project.cf/login.php")

        self.view.add(self.webview)
        self.window.add(self.view)
        self.window.show_all()
        Gtk.main()

if __name__ == "__main__":
    Gtk.init(sys.argv)
    messenger = Messenger()

