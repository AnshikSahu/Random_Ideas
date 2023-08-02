class Internet:
    class User:
        def __init__(self, name,IP,tower,wireless):
            self.name = name
            self.IP = IP
            self.tower = tower
            self.wireless = wireless

        def __str__(self):
            return self.name
        
        def transfer_wireless(self, data,packet_size,destination):
            pass

    class Server:
        def __init__(self, name,IP,router,cable):
            self.name = name
            self.IP = IP
            self.router = router
            self.cable = cable

        def __str__(self):
            return self.name

        def transfer(self, data,packet_size,destination):
            pass

    class Tower:
        def __init__(self, name,IP,users,wireless,router,cable):
            self.name = name
            self.IP = IP
            self.users = users
            self.wireless = wireless
            self.router = router
            self.cable = cable

        def __str__(self):
            return self.name

        def transfer(self, data,packet_size,destination):
            pass

        def transfer_wireless(self, data,packet_size,destination):
            pass
    
    class Router:
        buffer=[]
        lookup={}
        routers=[]
        cables=[]
        def __init__(self, name,IP,routers,cables):
            self.name = name
            self.IP = IP
            self.routers=routers
            self.cables=cables

        def __str__(self):
            return self.name

        def transfer(self, data,packet_size,destination):
            pass

        def collect(self, data,packet_size,source,destination):
            pass

    class InterConnection_Router(Router):
        def __init__(self, name,IP,routers,cables):
            super().__init__(name,IP,routers,cables)

        def __str__(self):
            return self.name

    class Tower_Router(Router):
        def __init__(self, name,IP,routers,cables,tower,cable):
            super().__init__(name,IP,routers,cables)
            self.tower = tower
            self.cable = cable

        def collect_from_tower(self, data,packet_size,source,destination):
            pass

    class Cable:
        def __init__(self, name,IP,capacity,source,destination):
            self.name = name
            self.IP = IP
            self.capacity = capacity
            self.source = source
            self.destination = destination

        def __str__(self):
            return self.name

        def transfer_forward(self, data,packet_size,destination):
            pass

        def transfer_backward(self, data,packet_size,source):
            pass

    class Wireless:
        def __init__(self, name,IP,capacity,source,destination):
            self.name = name
            self.IP = IP
            self.capacity = capacity
            self.source = source
            self.destination = destination

        def __str__(self):
            return self.name
        
        def transfer_forward(self, data,packet_size,destination):
            pass

        def transfer_backward(self, data,packet_size,source):
            pass

    class Regional_ISP:
        def __init__(self, name,IP,routers,towers,users,servers):
            self.name = name
            self.IP = IP
            self.routers = routers
            self.towers = towers
            self.users = users
            self.servers = servers

        def __str__(self):
            return self.name
        
        def subscribe(self, user):
            pass

        def unsubscribe(self, user):
            pass

    class Global_ISP:
        def __init__(self, name,IP,routers,servers,regional_ISPs,interconnection_routers):
            self.name = name
            self.IP = IP
            self.routers = routers
            self.servers = servers
            self.regional_ISPs = regional_ISPs
            self.interconnection_routers = interconnection_routers

        def __str__(self):
            return self.name
        
        def subscribe(self, regional_ISP):
            pass

        def unsubscribe(self, regional_ISP):
            pass

    def __init__(self,globals):
        self.name="Internet of Things"
        self.globals=globals

    def __str__(self):
        return self.name
    
    def subscribe(self, global_ISP):
        pass

    def unsubscribe(self, global_ISP):
        pass

    def transfer(self, data,packet_size,source,destination):
        pass