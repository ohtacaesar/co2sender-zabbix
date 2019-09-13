import logging
import socket
import time
from argparse import ArgumentParser, Namespace

from pyzabbix import ZabbixMetric, ZabbixSender

from CO2Meter import CO2Meter

FORMAT = 'time:%(asctime)s\tlevel:%(levelname)s\t%(message)s'
logger = logging.getLogger('co2monitor')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(handler)


def main():
  parser = ArgumentParser('co2monitor')
  parser.set_defaults(handler=_zabbix)
  parser.add_argument('--device', type=str, default='/dev/hidraw0')
  parser.add_argument('--host', type=str, default=socket.gethostname())
  parser.add_argument('--zabbix-server', type=str, required=True)
  parser.add_argument('-n', type=int)

  args = parser.parse_args()
  if 'handler' in args:
    args.handler(args)
  else:
    parser.print_help()


def _zabbix(args: Namespace):
  host = args.host
  sender = ZabbixSender(args.zabbix_server)
  meter = CO2Meter(args.device)
  n = args.n

  logger.info('zabbix-server:{}\thost:{}\tn:{}'.format(
      args.zabbix_server, host, n
  ))

  def send(data):
    packet = [] 
    for key in ['co2', 'temperature']:
      if key in data:
        packet.append(ZabbixMetric(host, 'co2monitor[{}]'.format(key), data[key]))

    r = sender.send(packet)
    logger.info(r)


  if n:
    for i in range(n):
      data = meter.get_data()
      send(data)
      if i < n - 1: time.sleep(10)
  else:
    while True:
      data = meter.get_data()
      send(data)
      time.sleep(10)

