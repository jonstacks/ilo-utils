import socket
import threading
from xml.etree import ElementTree

import requests


class PortScan(threading.Thread):
    def __init__(self, ip, port, timeout=2):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.open = False

    def run(self):
        sock = socket.socket()
        sock.settimeout(self.timeout)
        try:
            sock.connect((self.ip, self.port))
        except socket.error:
            self.open = False
        else:
            sock.close()
            self.open = True


class ILOInfo(threading.Thread):
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host
        self.resp = None
        self.serial = None
        self.model = None
        self.ilo_version = None
        self.firmware = None

    def run(self):
        url = 'http://{}/xmldata?item=all'.format(self.host)
        self.resp = requests.get(url)
        if self.resp.status_code == requests.codes.ok:
            tree = ElementTree.fromstring(self.resp.content)
            hsi = tree.find('HSI')
            self.serial = hsi.find('SBSN').text.strip()
            self.model = hsi.find('SPN').text.strip()
            mp = tree.find('MP')
            self.ilo_version = mp.find('PN').text.strip()
            self.firmware = mp.find('FWRI').text.strip()
