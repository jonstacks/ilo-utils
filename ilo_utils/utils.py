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
    def __init__(self, host, timeout=2):
        threading.Thread.__init__(self)
        self.host = host
        self.timeout = timeout
        self.resp = None
        self.serial = None
        self.model = None
        self.ilo_version = None
        self.firmware = None
        self.success = False

    def run(self):
        url = 'http://{}/xmldata?item=all'.format(self.host)
        try:
            self.resp = requests.get(url, timeout=self.timeout)
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        else:
            if self.resp.status_code == requests.codes.ok:
                self.success = True
                tree = ElementTree.fromstring(self.resp.content)
                hsi = tree.find('HSI')
                if hsi is not None:
                    self.serial = hsi.find('SBSN').text.strip()
                    self.model = hsi.find('SPN').text.strip()
                mp = tree.find('MP')
                if mp is not None:
                    self.ilo_version = mp.find('PN').text.strip()
                    self.firmware = mp.find('FWRI').text.strip()
