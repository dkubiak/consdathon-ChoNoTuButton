import PySimpleGUIQt as sg
import requests
import sys
from flask import Flask, request
from threading import Thread
from tkinter import *

from call_me_handler import call_me_handler, CallMeRequest

IP_MAPS = {'Dawid': '172.19.200.109', 'Staszek': '172.19.200.207', 'Monika': '172.19.200.27'}

def tray_th():
    menu_def = ['BLANK', ['&CallTo', ['Monika', 'Staszek', 'Dawid'], '---', 'E&xit']]

    tray = sg.SystemTray(menu=menu_def, filename=r'icon.png')

    while True:  # The event loop
        menu_item = tray.Read()

        selfId = sys.argv[1]
        if menu_item in IP_MAPS:
            try:
                requests.post(f'http://{IP_MAPS[menu_item]}:8080/callMe', json={"sender": selfId}, timeout=1.5)
            except:
                pass
        if menu_item == 'Exit':
            break


def main():
    def flask_th():
        flask_app = Flask(__name__)

        @flask_app.route("/callMe", methods=['POST'])
        def call_me_route():
            json = request.get_json()
            Thread(target=lambda: call_me_handler(CallMeRequest(**json))).start()
            return ""

        flask_app.run(host="0.0.0.0", port=8080)

    Thread(target=flask_th).start()
    Thread(target=tray_th).start()


if __name__ == '__main__':
    main()
