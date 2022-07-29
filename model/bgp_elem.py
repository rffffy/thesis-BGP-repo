class BgpElement:
    def __init__(self,
                 new_record_type,
                 new_type,
                 new_time,
                 new_project,
                 new_collector,
                 new_router,
                 new_router_ip,
                 new_peer_asn,
                 new_peer_address
                 ):
        self.record_type = new_record_type
        self.type = new_type
        self.time = new_time
        self.project = new_project
        self.collector = new_collector
        self.router = new_router
        self.router_ip = new_router_ip
        self.peer_asn = new_peer_asn
        self.peer_address = new_peer_address
