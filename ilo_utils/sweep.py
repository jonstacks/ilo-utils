"""
ILO Sweep.

Usage:
  ilo-sweep <network> [--timeout=<seconds> --skip-port-check]
  ilo-sweep -h | --help
  ilo-sweep --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --skip-port-check    Skips the initial port check for ILO devices.
  --timeout=<seconds>  Timeout in seconds [default: 1].

"""
import socket
import sys

from docopt import docopt
from netaddr import IPNetwork, AddrFormatError
from prettytable import PrettyTable

from .constants import ILO_PORT
from .utils import PortScan, ILOInfo


class Sweeper(object):

    def __init__(self, network, timeout, workers=5, check_port=True):
        self.network = network
        self.timeout = timeout
        self.workers = workers
        self.check_port = check_port
        self.ilo_hosts = []
        self.table = PrettyTable(['IP', 'Serial', 'Model', 'ILO Version',
                                  'Firmware Version'])
        self.table.align = 'r'
        self.table.align['IP'] = 'l'
        self.table.sortby = 'IP'
        self.table.sort_key = lambda x: socket.inet_aton(x[0])

    def _determine_ilo_hosts(self):
        """
        Use a threaded port scan to find hosts that
        have the ILO port open.
        """
        threads = []
        for addr in self.network:
            thread = PortScan(str(addr), ILO_PORT, self.timeout)
            threads.append(thread)
            thread.start()

        for t in threads:
            t.join()
            if t.open:
                self.ilo_hosts.append(t.ip)

    def _fetch_ilo_info(self):
        threads = []
        for host in self.ilo_hosts:
            thread = ILOInfo(host, timeout=self.timeout)
            threads.append(thread)
            thread.start()

        for t in threads:
            t.join()
            if t.success:
                self.table.add_row([t.host, t.serial, t.model, t.ilo_version,
                                    t.firmware])

    def sweep(self):
        if self.check_port:
            self._determine_ilo_hosts()
        else:
            # Fall back to using every address in the subnet
            self.ilo_hosts.extend(str(x) for x in self.network)
        self._fetch_ilo_info()

    def print_summary(self):
        print self.table


def main():
    args = docopt(__doc__, version='ILO Sweep 0.1')
    timeout = args['--timeout']
    network = args['<network>']
    check_port = not args.get('--skip-port-check', False)
    errors = []
    try:
        timeout = int(timeout)
    except ValueError:
        errors.append(
            "Could not convert {} to an integer timeout value"
            "".format(timeout)
        )

    try:
        network = IPNetwork(network)
    except AddrFormatError as e:
        errors.append(str(e))

    if errors:
        print "\n".join(map(lambda x: "Error: {}".format(x), errors))
        sys.exit(1)

    sweeper = Sweeper(network, timeout, check_port=check_port)
    sweeper.sweep()
    sweeper.print_summary()

if __name__ == "__main__":
    main()
