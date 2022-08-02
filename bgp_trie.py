import pygtrie
import pybgpstream
import re
import ipaddress
from model.bgp_elem import BgpElement

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def check_if_ip4(ip):
    """
    Checks for IPv4 address using regular expression

    Parameters:
        ip(str): The IP address that needs to be checked

    Returns:
         A boolean values deciding whether the ip argument is IPv4 or not

    """
    return re.search(regex, ip)


trie = pygtrie.CharTrie()

# create the stream with desired configurations
stream = pybgpstream.BGPStream(
    from_time="2017-07-07 00:00:00", until_time="2017-07-07 00:1:00 UTC",
    collectors=["route-views.sg", "route-views.eqix"],
    record_type="updates"
)

for elem in stream:
    if check_if_ip4(elem.peer_address):
        # Get binary representation of the peer_address
        binary_ip_address = bin(int(ipaddress.IPv4Address(elem.peer_address)))

        # Save in Trie structure with key as Binary IP Address and Value as BgpElement
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
        # print(trie)
        # print(elem.peer_address)

print(trie)
