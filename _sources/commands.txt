========
Commands
========

After you install `ilo-utils`, the following commands are automatically
made available to you:


---------
ilo-sweep
---------

The `ilo-sweep` command can be used to sweep a network for ILO Devices.
It does this by first sweeping the given subnet for IPs that are listening
on port 17988. `This <http://techibee.com/hardware/how-to-find-the-ilo-details-of-remote-server/155>`_
article provided that information along with other details. Once we have
narrowed down the list of IP address that are listening, we try to get the
ILO inventory for each host like so::

    GET /xmldata?item=all

Once we have the data, we parse out the relative fields and then display the
data in a nicely formatted table.

Usage::

    ilo-sweep 192.168.1.0/24
    ilo-sweep 192.168.1.0/24 --timeout 10
    ilo-sweep 192.168.1.0/24 --skip-port-check