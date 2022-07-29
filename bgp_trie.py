import pygtrie
import pybgpstream
import re
import ipaddress
from model.bgp_elem import BgpElement

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check(ip):
    return re.search(regex, ip)


trie = pygtrie.CharTrie()

stream = pybgpstream.BGPStream(
    from_time="2017-07-07 00:00:00", until_time="2017-07-07 00:1:00 UTC",
    collectors=["route-views.sg", "route-views.eqix"],
    record_type="updates"
)

for elem in stream:
    if check(elem.peer_address):
        binary_ip_address = bin(int(ipaddress.IPv4Address(elem.peer_address)))
        trie[binary_ip_address] = BgpElement(elem.record_type,
                                             elem.type,
                                             elem.time,
                                             elem.project,
                                             elem.collector,
                                             elem.router,
                                             elem.router_ip,
                                             elem.peer_asn,
                                             elem.peer_address,
                                             )
        # print(trie0
        # print(elem.peer_address)

print(trie)
